import numpy as np

from crypto.matrix_utils import (
    text_to_numbers,
    create_blocks,
    matrix_mod_inverse,
    is_invertible
)

MOD = 26


def recover_key_matrix(
        plaintext,
        ciphertext,
        block_size):

    steps = []

    plain_nums = text_to_numbers(
        plaintext
    )

    cipher_nums = text_to_numbers(
        ciphertext
    )

    plain_blocks = create_blocks(
        plain_nums,
        block_size
    )

    cipher_blocks = create_blocks(
        cipher_nums,
        block_size
    )

    P = np.array(
        plain_blocks[:block_size]
    ).T

    C = np.array(
        cipher_blocks[:block_size]
    ).T

    steps.append(
        f"Plaintext Matrix P:\n{P}"
    )

    steps.append(
        f"Ciphertext Matrix C:\n{C}"
    )

    # CHECK INVERTIBILITY
    if not is_invertible(P):

        steps.append(
            "ERROR: Plaintext matrix "
            "is not invertible mod 26."
        )

        return None, steps

    P_inv = matrix_mod_inverse(P)

    steps.append(
        f"P Inverse:\n{P_inv}"
    )

    recovered_key = (
        np.dot(C, P_inv)
        % MOD
    )

    steps.append(
        f"K = C × P⁻¹ mod 26"
    )

    steps.append(
        f"Recovered Key:\n{recovered_key}"
    )

    return recovered_key, steps