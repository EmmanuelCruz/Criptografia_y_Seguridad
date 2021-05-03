#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import xor_cipher as XOR

def test_xor():
    xors = [("HOLA","INM@"),
            ("Do not spill the beans","En!onu!rqhmm!uid!cd`or"),
            ("Ésta es una frase en espa\xc3ol","Èru`!dr!to`!gs`rd!do!drq`ðnm")]
    for tup in xors:
        mess, crip = tup
        print(XOR.cipher(mess))
        print(crip)
        assert XOR.cipher(mess) == crip
        assert XOR.decipher(crip) == mess
