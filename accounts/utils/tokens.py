from django.core import signing


ACTIVATION_SALT = "user-activation-token"

def activation_token_generator(user_id: int) -> str:
    """Generate a signed activation token for a given user_id."""
    return signing.dumps({"user_id": user_id}, salt=ACTIVATION_SALT)

def valid_activation_token(token: str, max_age=60*60*24) -> int | None:
    """Validate the token and return user_id if valid, else None."""
    try:
        data = signing.loads(token, salt=ACTIVATION_SALT, max_age=max_age)
        return data["user_id"]
    except (signing.SignatureExpired, signing.BadSignature):
        return None