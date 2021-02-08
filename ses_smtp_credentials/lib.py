import hmac
import hashlib
import base64

from .constants import (
    SMTP_REGIONS,
    SIG_DATE,
    SIG_SERVICE,
    SIG_TERMINAL,
    SIG_MESSAGE,
    SIG_VERSION,
)


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def calculate_key(secret_access_key, region):
    assert region in SMTP_REGIONS, f"The {region} Region doesn't have an SMTP endpoint."

    signature = sign(("AWS4" + secret_access_key).encode("utf-8"), SIG_DATE)
    signature = sign(signature, region)
    signature = sign(signature, SIG_SERVICE)
    signature = sign(signature, SIG_TERMINAL)
    signature = sign(signature, SIG_MESSAGE)
    signature_and_version = bytes([SIG_VERSION]) + signature
    smtp_password = base64.b64encode(signature_and_version)
    return smtp_password.decode("utf-8")
