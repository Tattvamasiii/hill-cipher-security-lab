from flask import (
    Flask,
    render_template,
    request
)

import numpy as np

from crypto.encrypt import encrypt
from crypto.decrypt import decrypt

from crypto.matrix_utils import (
    is_invertible
)

from crypto.sensitivity import (
    key_sensitivity_analysis
)

from crypto.attack import (
    recover_key_matrix
)

from crypto.performance import (
    measure_performance
)

app = Flask(__name__)


# HOME PAGE
@app.route('/')

def home():

    return render_template(
        'index.html'
    )


# ENCRYPTION PROCESS
@app.route(
    '/process',
    methods=['POST']
)

def process():

    plaintext = request.form[
        'plaintext'
    ]

    size = int(
        request.form['size']
    )

    matrix_values = request.form[
        'matrix'
    ].split()

    matrix_values = list(
        map(int, matrix_values)
    )

    key_matrix = np.array(
        matrix_values
    ).reshape(size, size)

    if not is_invertible(
            key_matrix):

        return render_template(
            'result.html',
            error="Invalid Matrix"
        )

    ciphertext, encrypt_steps = encrypt(
        plaintext,
        key_matrix
    )

    recovered, decrypt_steps = decrypt(
        ciphertext,
        key_matrix
    )

    return render_template(
        'result.html',

        plaintext=plaintext,

        ciphertext=ciphertext,

        recovered=recovered,

        encrypt_steps=encrypt_steps,

        decrypt_steps=decrypt_steps,

        matrix=key_matrix
    )


# SENSITIVITY ANALYSIS
@app.route('/sensitivity')

def sensitivity():

    plaintext = "HELLOCRYPTO"

    key1 = np.array([
        [3, 3],
        [2, 5]
    ])

    key2 = np.array([
        [3, 4],
        [2, 5]
    ])

    result = key_sensitivity_analysis(
        plaintext,
        key1,
        key2
    )

    return render_template(
        'sensitivity.html',
        result=result
    )


# KNOWN PLAINTEXT ATTACK
@app.route(
    '/attack',
    methods=['GET', 'POST']
)

def attack():

    if request.method == 'POST':

        plaintext = request.form[
            'plaintext'
        ]

        ciphertext = request.form[
            'ciphertext'
        ]

        block_size = int(
            request.form['size']
        )

        recovered_key, steps = recover_key_matrix(
            plaintext,
            ciphertext,
            block_size
        )

        return render_template(

            'attack.html',

            plaintext=plaintext,

            ciphertext=ciphertext,

            recovered_key=recovered_key,

            steps=steps
        )

    return render_template(
        'attack.html'
    )


# PERFORMANCE ANALYSIS
@app.route(
    '/performance',
    methods=['GET', 'POST']
)

def performance():

    if request.method == 'POST':

        plaintext = request.form[
            'plaintext'
        ]

        size = int(
            request.form['size']
        )

        matrix_values = request.form[
            'matrix'
        ].split()

        matrix_values = list(
            map(int, matrix_values)
        )

        key_matrix = np.array(
            matrix_values
        ).reshape(size, size)

        result = measure_performance(
            plaintext,
            key_matrix
        )

        return render_template(
            'performance.html',
            result=result
        )

    return render_template(
        'performance.html'
    )
if __name__ == '__main__':

    app.run(debug=True)