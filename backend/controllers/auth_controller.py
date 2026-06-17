from backend.models.user_crud import create_user, get_user_by_email
import re
import bcrypt

def is_valid_email(email):
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

def is_valid_password(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{8,64}$', password))

def register(data):
    required_fields = ['email', 'password', 'first_name', 'last_name']
    missing = [field
               for field in required_fields
               if not data.get(field)]

    if missing:
        return {
            "status": "error",
            "message": f"Missing fields: {', '.join(missing)}"
        }, 400
    
    email = data['email']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']

    if not is_valid_email(email):
        return {
            "status": "error",
            "message": "Invalid email format"
        }, 400
    
    if not is_valid_password(password):
        return {
            "status": "error",
            "message": "Password must be 8-64 characters, include uppercase, lowercase, number, and special character"
        }, 400
    
    user = get_user_by_email(email)
    if user:
        return {
            "status": "error",
            "message": "Email already registered"
        }, 409
    
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    user_id = create_user(email, password_hash, first_name, last_name)

    return {
        "status": "success",
        "message": "User created successfully",
        "user_id": user_id,
        "email": email
    }, 201