import numpy as np

from crypto.encrypt import encrypt


def compare_texts(text1, text2):

    differences = 0

    for a, b in zip(text1, text2):

        if a != b:
            differences += 1

    percentage = (
        differences / len(text1)
    ) * 100

    return differences, percentage


def key_sensitivity_analysis(
        plaintext,
        key1,
        key2):

    cipher1, steps1 = encrypt(
        plaintext,
        key1
    )

    cipher2, steps2 = encrypt(
        plaintext,
        key2
    )

    diff, percentage = compare_texts(
        cipher1,
        cipher2
    )

    result = {

        "plaintext": plaintext,

        "key1": key1,

        "key2": key2,

        "cipher1": cipher1,

        "cipher2": cipher2,

        "differences": diff,

        "percentage": percentage,

        "steps1": steps1,

        "steps2": steps2
    }

    return result


def plaintext_sensitivity_analysis(
        plaintext1,
        plaintext2,
        key):

    cipher1, _ = encrypt(
        plaintext1,
        key
    )

    cipher2, _ = encrypt(
        plaintext2,
        key
    )

    diff, percentage = compare_texts(
        cipher1,
        cipher2
    )

    result = {

        "plaintext1": plaintext1,

        "plaintext2": plaintext2,

        "cipher1": cipher1,

        "cipher2": cipher2,

        "differences": diff,

        "percentage": percentage
    }

    return result