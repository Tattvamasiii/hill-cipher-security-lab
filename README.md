# Hill Cipher Security Lab

An interactive web application built with Flask that demonstrates the **Hill Cipher** — a classical polygraphic substitution cipher based on linear algebra and modular arithmetic. The lab covers encryption, decryption, cryptanalysis, key sensitivity, and performance benchmarking.

## Features

- **Encryption Simulator** — Encrypt and decrypt custom plaintext using a user-defined key matrix (2×2 or 3×3), with step-by-step breakdown of the process.
- **Known Plaintext Attack** — Simulates cryptanalysis by recovering the key matrix from a known plaintext-ciphertext pair using `K = C × P⁻¹ mod 26`.
- **Key Sensitivity Analysis** — Demonstrates the avalanche effect by comparing ciphertexts produced from two closely related keys.
- **Performance Analysis** — Measures and reports encryption/decryption execution time for a given input.

## Tech Stack

- **Backend:** Python, Flask
- **Math/Crypto:** NumPy, SymPy
- **Frontend:** HTML, CSS, JavaScript (Jinja2 templating)

## Project Structure

```
.
├── app.py                     # Flask application and routes
├── requirements.txt           # Python dependencies
├── crypto/
│   ├── encrypt.py             # Encryption logic
│   ├── decrypt.py             # Decryption logic
│   ├── matrix_utils.py        # Matrix invertibility & helper functions
│   ├── sensitivity.py         # Key sensitivity / avalanche effect analysis
│   ├── attack.py              # Known plaintext attack (key recovery)
│   └── performance.py         # Performance benchmarking
├── templates/
│   ├── index.html             # Home page
│   ├── result.html            # Encryption/decryption results
│   ├── attack.html            # Known plaintext attack page
│   ├── sensitivity.html       # Sensitivity analysis page
│   └── performance.html       # Performance analysis page
└── static/
    ├── style.css
    └── script.js
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Tattvamasiii/hill-cipher-security-lab.git
   cd hill-cipher-security-lab
   ```

2. (Recommended) Create and activate a virtual environment
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

- **Home (`/`)** — Enter plaintext and a key matrix to encrypt and decrypt a message.
- **Sensitivity (`/sensitivity`)** — View how a small change in the key drastically changes the ciphertext.
- **Attack (`/attack`)** — Provide a known plaintext-ciphertext pair to attempt key recovery.
- **Performance (`/performance`)** — Benchmark encryption/decryption speed for given input.

## How the Hill Cipher Works

- **Encryption:** `C = K × P mod 26`
- **Decryption:** `P = K⁻¹ × C mod 26`

Where `K` is the key matrix, `P` is the plaintext vector, and `C` is the ciphertext vector. For decryption to work, the key matrix must be invertible modulo 26 (i.e., `gcd(det(K), 26) = 1`).

## License

This project is open source and available for educational use.
