import numpy as np

from crypto.matrix_utils import (
    text_to_numbers,
    numbers_to_text,
    create_blocks,
    matrix_mod_inverse
)

MOD = 26


def decrypt(ciphertext, key_matrix):

    steps = []

    block_size = len(key_matrix)

    inverse_matrix = matrix_mod_inverse(
        key_matrix
    )

    steps.append(
        f"Inverse Matrix:\n{inverse_matrix}"
    )

    numbers = text_to_numbers(
        ciphertext
    )

    blocks = create_blocks(
        numbers,
        block_size
    )

    plaintext_numbers = []

    for block in blocks:

        vector = np.array(block).reshape(
            block_size,
            1
        )

        multiplied = np.dot(
            inverse_matrix,
            vector
        )

        decrypted = multiplied % MOD

        steps.append(
            f"""
Cipher Block: {block}

K⁻¹ × C:
{multiplied}

(K⁻¹ × C) mod 26:
{decrypted}
"""
        )

        plaintext_numbers.extend(
            decrypted.flatten().tolist()
        )

    plaintext = numbers_to_text(
        plaintext_numbers
    )

    steps.append(
        f"Recovered Plaintext: {plaintext}"
    )

    return plaintext, steps