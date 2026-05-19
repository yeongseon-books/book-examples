from common import gcd, fast_power


def hash_mod(key, bucket_count):
    return key % bucket_count
