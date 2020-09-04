def is_acceptable_password(password:str) -> bool:
    return (lambda password : len(password) > 6)(password)