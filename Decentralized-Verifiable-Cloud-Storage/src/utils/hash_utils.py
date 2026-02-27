import hashlib

def generate_hash(data: str, counter: int) -> str:
    """
    Generate SHA-256 hash commitment for data with freshness counter.
    """
    combined = f"{data}-{counter}".encode()
    return hashlib.sha256(combined).hexdigest()