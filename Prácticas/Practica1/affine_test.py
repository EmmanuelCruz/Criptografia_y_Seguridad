#!/usr/local/bin/python
# latin-1
import os, sys
"""import pytest"""
from utils import CryptographyException
from utils import prime_relative
from affine_cipher import Affine

alphabet = "ABCDEFGHIJKLMN\xc3OPQRSTUVWXYZ"
message = "UNMENSAJEENESPA\xc3OL"

def test_must_fail():
    with pytest.raises(CryptographyException):
        a = Affine(alphabet, 3, 10)

def test_correct_key():
    a = Affine(alphabet)
    n = len(alphabet)
    assert prime_relative(n, a.A)

def test_basic():
    a = Affine(alphabet, 1, 27)
    assert a.cipher(message) == message
    assert a.decipher(message) == message
    a.B = 1
    crip = "V\xc3NF\xc3TBKFF\xc3FTQBOPM"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message

def test_normal():
    a = Affine(alphabet, 4, 10)
    crip = "NIEZIFKSZZIZFTKMPA"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message
    a.A = 5
    crip = "HUPDUXKBDDUDXJKZEL"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message
    a.B = 3
    crip = "A\xc3JW\xc3QDUWW\xc3WQCDSXE"
    assert a.cipher(message) == crip
    assert a.decipher(crip) == message
