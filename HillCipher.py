import numpy as np
from math import gcd

# ---------- Polynomial Hash ----------
def polynomial_hash(s, p=31, m=10**9 + 7):
    H, power = 0, 1
    for ch in s:
        H = (H + ord(ch) * power) % m
        power = (power * p) % m
    return H

# ---------- Generate Always Valid Key Matrix ----------
def generate_valid_key_matrix(key):
    H = polynomial_hash(key)

    while True:
        a = (H % 25) + 1
        b = ((H // 3) % 26)
        c = ((H // 5) % 26)
        d = ((H // 7) % 26)

        K = np.array([[a, b], [c, d]])

        det = (a * d - b * c) % 26

        if gcd(det, 26) == 1:
            return K, key

        H += 1

# ---------- Modular Inverse ----------
def mod_inverse(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No inverse")

# ---------- Matrix Inverse ----------
def matrix_mod_inverse(K):
    det = int(round(np.linalg.det(K))) % 26
    det_inv = mod_inverse(det, 26)

    adj = np.array([
        [K[1][1], -K[0][1]],
        [-K[1][0], K[0][0]]
    ])

    return (det_inv * adj) % 26

# ---------- Text Conversion ----------
def text_to_numbers(t):
    return [ord(c) - 65 for c in t]

def numbers_to_text(nums):
    return ''.join(chr(n + 65) for n in nums)

# ---------- Block Creation ----------
def create_blocks(nums):
    if len(nums) % 2 != 0:
        nums.append(23)
    return [nums[i:i+2] for i in range(0, len(nums), 2)]

# ---------- Encryption ----------
def encrypt(pt, key):
    pt = pt.upper().replace(" ", "")
    K, used_key = generate_valid_key_matrix(key)

    nums = text_to_numbers(pt)
    blocks = create_blocks(nums)

    res = []
    for b in blocks:
        P = np.array(b).reshape(2, 1)
        C = np.dot(K, P) % 26
        res.extend(C.flatten())

    return numbers_to_text(res), used_key

# ---------- Decryption ----------
def decrypt(ct, key):
    ct = ct.upper().replace(" ", "")
    K, used_key = generate_valid_key_matrix(key)
    K_inv = matrix_mod_inverse(K)

    nums = text_to_numbers(ct)
    blocks = create_blocks(nums)

    res = []
    for b in blocks:
        C = np.array(b).reshape(2, 1)
        P = np.dot(K_inv, C) % 26
        res.extend(P.flatten())

    return numbers_to_text(res), used_key

# ---------- User Input ----------
if __name__ == "__main__":
    choice = input("Enter E for Encryption or D for Decryption: ").strip().upper()
    text = input("Enter text: ").strip()
    key = input("Enter key: ").strip()

    try:
        if choice == 'E':
            cipher, used_key = encrypt(text, key)
            print("Cipher:", cipher)
            print("Key used:", used_key)

        elif choice == 'D':
            plain, used_key = decrypt(text, key)
            print("Plaintext:", plain)
            print("Key used:", used_key)

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)