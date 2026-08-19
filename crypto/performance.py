import time

from crypto.encrypt import encrypt
from crypto.decrypt import decrypt


def measure_performance(
        plaintext,
        key_matrix):

    # HIGH PRECISION TIMER
    start_encrypt = time.perf_counter()

    ciphertext, _ = encrypt(
        plaintext,
        key_matrix
    )

    end_encrypt = time.perf_counter()

    encrypt_time = (
        end_encrypt - start_encrypt
    )

    start_decrypt = time.perf_counter()

    decrypted, _ = decrypt(
        ciphertext,
        key_matrix
    )

    end_decrypt = time.perf_counter()

    decrypt_time = (
        end_decrypt - start_decrypt
    )

    return {

        "ciphertext": ciphertext,

        "decrypted": decrypted,

        "encrypt_time":
            f"{encrypt_time:.10f}",

        "decrypt_time":
            f"{decrypt_time:.10f}"
    }