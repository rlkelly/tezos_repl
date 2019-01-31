""" Taken From https://github.com/joeblackwaslike/base58check/blob/master/base58check/__init__.py """

from collections import deque
from hashlib import sha256, sha512, blake2b
from ecdsa import VerifyingKey, SECP256k1

DEFAULT_CHARSET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def blake2b_hash(val):
    return blake2b(bytes(val)).digest()


def sha256_hash(val):
    return sha256(bytes(val)).digest()


def sha512_hash(val):
    return sha512(bytes(val)).digest()


def check_signature(key, sig, message):
    vk = VerifyingKey.from_string(bytes.fromhex(key), curve=SECP256k1)
    return vk.verify(bytes.fromhex(sig), bytes.fromhex(message), sha256)


def b58encode(val, charset=DEFAULT_CHARSET):
    def _b58encode_int(int_, default=bytes([charset[0]])):
        if not int_ and default:
            return default
        output = b''
        while int_:
            int_, idx = divmod(int_, 58)
            output = charset[idx:idx+1] + output
        return output

    if not isinstance(val, bytes):
        raise TypeError(
            "a bytes-like object is required, not '%s', "
            "use .encode('ascii') to encode unicode strings" %
            type(val).__name__)

    if isinstance(charset, str):
        charset = charset.encode('ascii')

    pad_len = len(val)
    val = val.lstrip(b'\0')
    pad_len -= len(val)

    p, acc = 1, 0
    for char in deque(reversed(val)):
        acc += p * char
        p = p << 8

    result = _b58encode_int(acc, default=False)
    prefix = bytes([charset[0]]) * pad_len
    return prefix + result


def b58check (prefix, b) :
    x = bytes(prefix + b)
    checksum = sha256(sha256(x).digest()).digest()[0:4]
    return b58encode(x + checksum)
