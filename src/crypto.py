import bcrypt
import json

# Function to hash a password and store the salt and hash in a file
def store_password(password, filename):
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Store salt and hash in a file
    with open(filename, 'w') as file:
        json.dump({
            'salt': salt.decode('utf-8'),  # Decode bytes to string for JSON compatibility
            'hash': hashed_password.decode('utf-8')
        }, file)

# Function to check if the provided password matches the stored hash
def check_password(stored_file, password):
    # Load the salt and hash from the file
    with open(stored_file, 'r') as file:
        data = json.load(file)

    # Extract salt and hash from the loaded data
    stored_salt = data['salt'].encode('utf-8')
    stored_hash = data['hash'].encode('utf-8')

    # Check if the provided password matches the stored hash
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

# Example Usage
if __name__ == "__main__":
    # # Store a password
    # store_password("my_secure_password", "password_data.json")
    
    # Check the password
    is_correct = check_password("password_data.json", "my_securfe_password")
    print(f"Password is correct: {is_correct}")