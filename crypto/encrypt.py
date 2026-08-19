import numpy as np

from crypto.matrix_utils import (
    text_to_numbers,
    numbers_to_text,
    pad_text,
    create_blocks
)

MOD = 26


def encrypt(plaintext, key_matrix):

    steps = []

    block_size = len(key_matrix)

    plaintext = pad_text(
        plaintext,
        block_size
    )

    steps.append(
        f"Padded Plaintext: {plaintext}"
    )

    numbers = text_to_numbers(
        plaintext
    )

    steps.append(
        f"Text to Numbers: {numbers}"
    )

    blocks = create_blocks(
        numbers,
        block_size
    )

    ciphertext_numbers = []

    for block in blocks:

        vector = np.array(block).reshape(
            block_size,
            1
        )

        multiplied = np.dot(
            key_matrix,
            vector
        )

        encrypted = multiplied % MOD

        steps.append(
            f"""
Block: {block}

Vector:
{vector}

K × P:
{multiplied}

(K × P) mod 26:
{encrypted}
"""
        )

        ciphertext_numbers.extend(
            encrypted.flatten().tolist()
        )

    ciphertext = numbers_to_text(
        ciphertext_numbers
    )

    steps.append(
        f"Ciphertext: {ciphertext}"
    )

    return ciphertext, steps