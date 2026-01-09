from app import hash_to_bucket


def test_hash_to_bucket_range():
    b = hash_to_bucket("any", 100)
    assert 0 <= b < 100


def test_hash_to_bucket_changes_with_input():
    assert hash_to_bucket("a", 100) != hash_to_bucket("b", 100)


def test_hash_to_bucket_deterministic():
    assert hash_to_bucket("user123", 100) == hash_to_bucket("user123", 100)
