import bcrypt


def hash_password(password: str) -> bytes:
    password_bytes = password.encode("utf-8")

    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed_bytes
