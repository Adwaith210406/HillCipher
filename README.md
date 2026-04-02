# HillCipher

Prompts:
For hill cipher, give an algorithm with your own hashing function
Give a selection of hashing functions for me to choose from
Explain how the polynomial hash is used when encrypting and decrypting
Explain the values taken for p and m
Why not take p=29

This project implements an enhanced version of the Hill Cipher, a classical encryption technique based on linear algebra, by integrating a polynomial hash-based key generation mechanism. The primary goal is to overcome the limitation of static key usage in the traditional Hill Cipher by introducing a dynamic and reproducible key generation process.

In this system, a user-defined passphrase is first processed using a polynomial rolling hash function with carefully chosen parameters (𝑝=31, 𝑚=10**9+7). The resulting hash value is then transformed into a key matrix of size 𝑘×𝑘, where each element is reduced modulo 26 to align with the alphabetic encoding scheme (A = 0 to Z = 25). The algorithm ensures that the generated matrix is invertible under modulo 26 arithmetic, which is essential for successful decryption.

During encryption, the plaintext is converted into numerical form and divided into fixed-size blocks corresponding to the matrix dimension. Each block is encrypted through matrix multiplication with the generated key matrix, followed by modulo 26 reduction to produce the ciphertext.

For decryption, the same passphrase is used to recompute the polynomial hash and regenerate the identical key matrix. The modular inverse of this matrix is then applied to the ciphertext blocks to accurately recover the original plaintext.

This approach demonstrates how classical cryptographic methods can be enhanced using modern hashing techniques, resulting in a system that is more flexible, less predictable, and better suited for educational and project-based applications
