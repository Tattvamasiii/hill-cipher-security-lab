import numpy as np
from sympy import Matrix
from math import gcd

MOD = 26


def clean_text(text):

    return ''.join(
        c.upper()
        for c in text
        if c.isalpha()
    )


def text_to_numbers(text):

    text = clean_text(text)

    return [
        ord(c) - ord('A')
        for c in text
    ]


def numbers_to_text(numbers):

    return ''.join(
        chr((n % 26) + ord('A'))
        for n in numbers
    )


def pad_text(text, block_size):

    text = clean_text(text)

    while len(text) % block_size != 0:
        text += 'X'

    return text


def create_blocks(numbers, size):

    return [
        numbers[i:i + size]
        for i in range(0, len(numbers), size)
    ]


def is_invertible(matrix):

    det = int(round(np.linalg.det(matrix)))

    return gcd(det % MOD, MOD) == 1


def matrix_mod_inverse(matrix):

    sym_matrix = Matrix(matrix)

    inv = sym_matrix.inv_mod(MOD)

    return np.array(inv).astype(int)