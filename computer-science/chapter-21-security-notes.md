# 📘 Chapter 21: Security - Cambridge International AS & A Level Computer Science (9618)

## Cambridge International AS & A Level Computer Science - Part 3

> **Rule + fully solved examples.** Everything the examiner can ask from Chapter 21: the security concerns around a transmission, symmetric and asymmetric encryption, digital signatures and digital certificates, DES/AES and RSA, SSL/TLS, and quantum key distribution. Every section ends with worked examples and exam-style questions with full mark-earning solutions.

**Learning objectives (Chapter 21):**
- Show understanding of how encryption works
- Distinguish symmetric key encryption from asymmetric (public key) encryption
- Understand digital signatures, hash functions and digital certificates
- Understand the role of a Certification Authority and a Public Key Infrastructure
- Show awareness of SSL/TLS and how they protect a web session
- Show awareness of quantum cryptography and Quantum Key Distribution (QKD)

---

## 21.01 Encryption Fundamentals

**Encryption** is the process of converting readable data (plaintext) into an unreadable form (ciphertext) using an algorithm and a key. **Decryption** reverses the process.

```
Plaintext  →  encryption algorithm + key  →  Ciphertext
Ciphertext →  decryption algorithm + key  →  Plaintext
```

> **KEY TERMS**
> - **Plaintext**: data before encryption.
> - **Ciphertext**: the result of applying an encryption algorithm to data.
> - **Key**: a value used by the algorithm to control the transformation. The algorithm is public; the key must remain secret.

### 21.01.1 The five security concerns

| Concern | Meaning | Question it answers |
|---|---|---|
| **Confidentiality** | Only the intended recipient can read the data | Can anyone else understand it? |
| **Authenticity** | The receiver is certain who sent the data | Who really sent it? |
| **Integrity** | The data has not been altered in transit | Has it been changed? |
| **Non-repudiation** | Neither party can deny sending/receiving | Can the sender deny it later? |
| **Availability** | The data/service is accessible when needed | Can the receiver actually get it? |

This chapter deals mainly with **confidentiality**, **authenticity** and **integrity**. Integrity covers both deliberate tampering and accidental corruption during transmission.

### 21.01.2 Symmetric key encryption

**Definition:** one private key (the **secret key**) is shared by sender and receiver and is used for both encryption and decryption.

- **Advantages:** fast; well suited to bulk data; simple in principle.
- **Disadvantage:** the **key distribution problem** — how do sender and receiver agree on the secret key without an eavesdropper learning it?
- **Examples:** DES, Triple DES, AES.

Both parties must already share the key, or have a secure channel to exchange it. This is why real systems often use asymmetric encryption to deliver a symmetric session key.

### 21.01.3 Asymmetric (public key) encryption

**Definition:** there is a **public key** and a **private key**; one is used for encryption and the other for decryption. The public key can be given to anyone; the private key is never released.

- If the **public key encrypts**, only the matching **private key** can decrypt. This gives confidentiality: anyone can send a secret message to the key owner.
- If the **private key encrypts**, anyone with the **public key** can decrypt. This does **not** give confidentiality (anyone can decrypt), but it can prove who sent the message — the basis of a **digital signature**.
- **Advantage:** no need to deliver a secret key; the public key is safe to publish.
- **Disadvantage:** much slower than symmetric encryption, so it is not used for large files.
- **Example:** RSA.

> **Exam tip:** do not say "the public key is used for decryption" without saying *which* direction. The pairing is what earns marks: public encrypts → private decrypts (confidentiality); private encrypts → public decrypts (authentication).

### 21.01.4 Brute-force attacks and key length

A **brute-force attack** tries every possible key until the correct one is found. The number of possibilities for an `n`-bit key is `2^n`.

| Key size | Number of keys | Time at 1 attempt per second |
|---|---|---|
| 64-bit | `2^64 ≈ 1.84 × 10^19` | about `5.8 × 10^11` years |
| 128-bit | `2^128 ≈ 3.40 × 10^38` | about `1.08 × 10^31` years |

Longer keys make brute force infeasible, but they also make encryption slower. Security therefore depends on **both** the complexity of the algorithm and the length of the key.

### 21.01.5 Worked example — symmetric vs asymmetric

**Worked example 21.01 — choose the right method**

A company wants to send a 2 GB database backup to a branch office and also wants to prove to the branch that the file came from head office.

**Solution:**

1. Encrypt the database with a fast **symmetric** algorithm (e.g. AES) using a randomly generated session key. This handles the bulk data efficiently.
2. Encrypt the session key with the branch's **public key** and send it. Only the branch can decrypt it with its private key. This solves key distribution.
3. Create a hash/digest of the database, encrypt the digest with head office's **private key**, and send it as a **digital signature**. The branch decrypts it with head office's public key and compares digests. This proves authenticity and integrity.

**What the examiner wants:** the combination — symmetric for speed, asymmetric for key delivery, digital signature for authenticity. A single method used for everything is rarely the best answer.

---

## 21.02 Digital Signatures and Digital Certificates

### 21.02.1 Hash functions and digests

A **cryptographic hash function** takes a message of any length and produces a fixed-length value called a **digest** (or hash). Properties:

- The same message always produces the same digest.
- A tiny change to the message produces a completely different digest (the **avalanche effect**).
- It is computationally infeasible to reconstruct the message from the digest (one-way).
- It is computationally infeasible to find two different messages with the same digest (collision resistance).

A digest is **not encryption**: it cannot be decrypted. It is a fingerprint of the data.

### 21.02.2 Creating a digital signature

The sender:

1. Applies the agreed hash function to the message → **digest**.
2. Encrypts the digest with the sender's **private key** → **digital signature**.
3. Sends the message (often as plaintext) and the digital signature.

The receiver:

1. Applies the **same hash function** to the received message → digest A.
2. Decrypts the digital signature with the sender's **public key** → digest B.
3. Compares A and B.
   - If they match, the message is **authentic** (it came from the holder of the private key) and **unaltered** (integrity).
   - If they differ, either the message was changed or the signature was not made with the matching private key.

Signing the digest rather than the whole message is faster, because the digest is much smaller. The signature is different for every message because the digest depends on the message.

> **Exam tip:** the private key signs, the public key verifies. Reversing this is the single most common mistake in this topic.

### 21.02.3 Why a digital signature alone is not enough

A signature proves that the sender possess **a** private key, but not **whose** private key it is. An attacker could generate a key pair, publish the public key under someone else's name, and sign messages that appear to come from that person. This is a **man-in-the-middle / impersonation** problem.

### 21.02.4 Digital certificates and Certification Authorities

A **Certification Authority (CA)** is a trusted third party that binds a public key to a verified identity. The CA issues a **digital certificate** containing:

- the owner's identity (name, organisation, domain),
- the owner's public key,
- the certificate's validity dates,
- the CA's digital signature over the certificate,
- possibly a serial number and the algorithms used.

**How a certificate is obtained:**

1. Person A generates a public–private key pair.
2. A contacts a CA and proves their identity.
3. A gives the public key to the CA.
4. The CA creates the certificate, writing A's public key into it.
5. The CA signs the certificate with the **CA's private key**.
6. The certificate is returned to A.
7. A publishes the certificate (for example on a website).

Anyone who wants A's public key obtains the certificate and verifies the CA's signature using the **CA's public key**. Because the CA is trusted, the public key inside is trusted to belong to A.

The standards for certificates and public key infrastructure are defined by **X.509** (the name is examinable but the details are not).

> **KEY TERMS**
> - **Certification Authority (CA)**: a trusted organisation that issues and signs digital certificates.
> - **Public Key Infrastructure (PKI)**: the policies, standards, software and CAs that manage public keys and certificates.
> - **Digital certificate**: a signed document that binds a public key to an identity.

### 21.02.5 Worked example — signature and certificate together

**Worked example 21.02 — securing an email**

Alice wants to send an important contract to Bob so that Bob knows it is from her and has not been changed.

1. Alice hashes the contract → digest.
2. Alice encrypts the digest with her private key → signature.
3. Alice sends the contract, signature, and her digital certificate to Bob.
4. Bob checks the certificate's signature using the CA's public key. He now trusts that the public key in the certificate belongs to Alice.
5. Bob decrypts the signature with Alice's public key → digest B.
6. Bob hashes the received contract → digest A.
7. If A = B, the contract is authentic and unchanged. If not, Bob rejects it.

**What the examiner wants:** the order — hash, sign with private key, verify with public key, compare digests — plus the role of the certificate in proving key ownership.

---

## 21.03 Symmetric Key Encryption Methods

### 21.03.1 DES, Triple DES and AES

| Method | Key size | Block size | Notes |
|---|---|---|---|
| **DES** | 56 bits (often quoted as 64, including parity) | 64 bits | Obsolete; too weak for modern use |
| **Triple DES (3DES)** | 112 or 168 bits | 64 bits | Applies DES three times; deprecated but stronger than DES |
| **AES** | 128, 192 or 256 bits | 128 bits | Current standard; fast and secure |

All three are **block ciphers**: they encrypt fixed-size blocks of bits rather than one bit at a time. A **stream cipher**, by contrast, encrypts a continuous stream.

### 21.03.2 Simplified DES (S-DES) — how a block cipher works

S-DES is used only for teaching. It encrypts **8-bit blocks** with a **10-bit key**.

**Stage 1 — key generation:**

1. Apply a fixed **permutation** to the 10-bit key (reorder the bits).
2. Split the result into two 5-bit halves and apply a **circular left shift** to each.
3. Apply another permutation to produce an **8-bit key K1**.
4. Shift the halves again and permute to produce **K2**.

**Stage 2 — encryption (five steps):**

1. Initial permutation of the 8-bit plaintext block.
2. Apply a function using the first 8-bit key.
3. Swap the first and last 4-bit halves.
4. Repeat the function with the second key.
5. Final permutation (the reverse of the initial permutation).

Decryption uses the same keys in reverse order and reverses the steps. The important idea is that encryption is a sequence of reversible operations, and the key controls the permutations and substitutions.

**Worked example 21.03 — key permutation**

Key = `0101010101`, permutation `3 5 2 7 4 10 1 9 8 6`.

Read the old positions in the order given:

`pos3=0, pos5=0, pos2=1, pos7=0, pos4=1, pos10=1, pos1=0, pos9=0, pos8=1, pos6=1`

Result: `0010110011`.

Then split: `00101` and `10011`. Circular left shift each by one: `01010` and `00111`, giving `0101000111`. Applying permutation `6 3 7 4 8 5 10 9` gives:

`pos6=0, pos3=0, pos7=0, pos4=1, pos8=1, pos5=0, pos10=1, pos9=1` → `00011011` = **K1**.

> **Exam tip:** bit positions are numbered from the left starting at 1. A permutation lists the old positions in the order they are copied into the new value.

### 21.03.3 Why symmetric encryption is still used

Symmetric algorithms are much faster than asymmetric ones. A typical secure system uses:

- **asymmetric encryption** to exchange a session key or sign a digest,
- **symmetric encryption** to protect the actual data stream.

This hybrid approach gives both security and acceptable performance.

---

## 21.04 Public Key Encryption Methods

### 21.04.1 RSA key generation

RSA (Rivest–Shamir–Adleman) is the standard public key method.

1. Choose two large prime numbers `p` and `q`.
2. Compute `n = p × q` (the modulus).
3. Compute `φ = (p − 1)(q − 1)`.
4. Choose `e` such that `1 < e < φ` and `e` is coprime with `φ` (65537 is common).
5. Find `d` such that `(d × e) mod φ = 1`. `d` is the modular inverse of `e`.
6. **Public key** = `(n, e)`.
7. **Private key** = `(n, d)`.

**Encryption** of a numeric message `x`: `y = x^e mod n`.
**Decryption** of `y`: `x = y^d mod n`.

Text must first be converted to numbers using an agreed coding scheme (e.g. ASCII/Unicode values).

Security relies on the difficulty of **factoring** a very large `n` back into `p` and `q`. Multiplying `p × q` is easy; factoring `n` is infeasible for sufficiently large primes.

### 21.04.2 Worked example — toy RSA

**Worked example 21.04 — encrypt and decrypt a single number**

Choose `p = 3`, `q = 11`.

- `n = 33`
- `φ = (3−1)(11−1) = 2 × 10 = 20`
- Choose `e = 3` (coprime with 20).
- Find `d`: `3d ≡ 1 (mod 20)`. `d = 7` because `3 × 7 = 21 ≡ 1`.
- Public key: `(33, 3)`; private key: `(33, 7)`.

Encrypt `x = 4`:

`y = 4^3 mod 33 = 64 mod 33 = 31`

Decrypt `31`:

`31^7 mod 33 = 4`

So the message is recovered. Real RSA uses primes with hundreds of digits; this example is only for understanding the arithmetic.

### 21.04.3 Symmetric vs asymmetric — comparison

| Feature | Symmetric | Asymmetric |
|---|---|---|
| Keys | One shared secret key | Public + private pair |
| Speed | Fast | Slow |
| Key distribution | Difficult — must share secretly | Easy — public key can be published |
| Main use | Bulk data encryption | Key exchange, digital signatures, certificates |
| Examples | DES, 3DES, AES | RSA |
| Confidentiality | Yes, if key stays secret | Yes, when public key encrypts |
| Authentication | Limited (both share the key) | Yes, when private key signs |

---

## 21.05 SSL and TLS

**SSL (Secure Sockets Layer)** and its successor **TLS (Transport Layer Security)** protect data sent between a client (usually a browser) and a server.

### 21.05.1 Where SSL/TLS sits

A **socket** is the combination of an IP address and a port number. TCP uses the port number to deliver data to the correct application. SSL/TLS sits **between TCP (transport layer) and the application layer**, adding security without changing the application itself.

When HTTP is protected by SSL/TLS it becomes **HTTPS**. The user does not need to take any action; the browser and server negotiate security automatically.

SSL is not a single protocol but a **protocol suite**, containing (among others):

- a **Record Protocol** — defines the format for transmitted data, including encryption and integrity protection;
- a **Handshake Protocol** — establishes the secure connection and agrees the keys.

### 21.05.2 The SSL/TLS handshake

1. TCP connection is established between client and server.
2. The client sends a request to start a secure session, listing supported algorithms.
3. The server responds with its **SSL/TLS certificate**, containing its public key, signed by a CA.
4. The client verifies the certificate using the CA's public key (and checks the domain name and validity dates).
5. The client generates a **one-off session key**, encrypts it with the server's public key, and sends it.
6. The server decrypts the session key with its private key.
7. Both sides now use the **symmetric session key** for fast encryption of the actual data.
8. Message authentication codes (or AEAD) protect integrity during the session.

The asymmetric phase is used only to authenticate the server and deliver the session key; the bulk data uses symmetric encryption.

### 21.05.3 SSL vs TLS

- SSL was originally proprietary; it was standardised by the **IETF** and reached version 3.0.
- **TLS** is the improved, standardised successor. It fixes security weaknesses in SSL.
- TLS 1.2 and 1.3 are the versions in current use. SSL is deprecated, although the name "SSL" is still used loosely.

> **Exam tip:** if asked "why is TLS preferred to SSL?", answer with security improvements and standardisation — not "it is newer" alone.

### 21.05.4 Worked example — what an attacker sees

**Worked example 21.05 — café Wi-Fi**

A user logs into a bank over HTTPS on public Wi-Fi. An attacker captures the packets.

- The attacker can see the server's IP address, the port, and the fact that TLS is used.
- The attacker **cannot** read the password or account details, because they are encrypted with the session key.
- The attacker **cannot** silently alter the data, because integrity checking would fail.
- If the attacker presents a fake certificate, the browser warns the user unless the attacker can forge a CA signature (infeasible) or the user ignores the warning.

**What the examiner wants:** confidentiality and integrity provided by encryption/MACs, authentication provided by the certificate, and the limit that metadata (IP, timing, volume) may still be visible.

---

## 21.06 Quantum Cryptography

### 21.06.1 Polarised photons

Quantum cryptography uses the quantum properties of **photons** (particles of light). A photon vibrates in a particular plane; this is its **polarisation**, drawn as a double-ended arrow.

Four polarisation states can encode bits using two **bases**:

- **Rectilinear basis (`+`)**: vertical `↕` = 1, horizontal `↔` = 0.
- **Diagonal basis (`×`)**: one diagonal = 1, the other = 0.

A sender can therefore encode a 1 or a 0 in either basis. The receiver must choose a basis to measure each photon. If the receiver chooses the **same basis** as the sender, the bit is read correctly. If the receiver chooses the **wrong basis**, the measurement is random and cannot be trusted.

### 21.06.2 Creating a shared secret (Quantum Key Distribution)

1. The sender chooses a random bit string and a random basis for each bit.
2. The receiver independently chooses a random basis for each photon.
3. The sender publicly announces the **basis** used for each bit (not the bit values).
4. The receiver replies with which bases matched.
5. Only the matching positions are kept; their bit values form the **shared secret key**.

**Worked example 21.06 — basis matching**

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bit sent | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| Sender basis | + | × | × | + | + | × | × | + | × | + |
| Receiver basis | × | + | + | + | × | × | + | × | × | + |
| Match? | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ |
| Shared bit | — | — | — | 1 | — | 0 | — | — | 0 | 1 |

Shared secret = `1001` (positions 4, 6, 9, 10).

### 21.06.3 Why QKD is secure

An eavesdropper cannot copy an unknown quantum state (the **no-cloning theorem**). Any attempt to intercept and measure a photon disturbs its polarisation. When the sender and receiver compare a sample of their shared bits, errors reveal the eavesdropper, and the key is discarded.

**Advantages:**

- Eavesdropping is detectable, not merely difficult.
- Security rests on physical laws, not on computational difficulty.

**Disadvantages:**

- Requires a dedicated **quantum channel** (e.g. fibre or free-space optical link), not ordinary network media.
- Very high cost and limited range.
- Needs authenticated classical communication to compare bases.
- Photon loss and detector noise limit practical distance.

> **Exam tip:** distinguish **QKD** (a method of distributing a key) from **quantum computing** (a different field). QKD does not encrypt the message itself; the resulting key is used in conventional symmetric encryption.

---

## 📝 Exam-style Questions with Full Solutions

### Question 1 — Security concerns and key methods (15 marks)

(a) Explain confidentiality, authenticity and integrity. [4]
(b) Explain how keys are used in symmetric and asymmetric encryption. Include reference to a public key, a private key and a secret key. [6]
(c) Explain the use of digital signatures and digital certificates. [5]

**Solution:**

(a) **Confidentiality:** only the intended recipient can decrypt and read the data; an interceptor cannot understand it. **Authenticity:** the receiver can be certain who sent the data. **Integrity:** the receiver can detect whether the data was altered or corrupted in transit.

(b) **Symmetric:** a single secret key is shared by sender and receiver; the same key encrypts and decrypts. **Asymmetric:** the sender uses the receiver's **public key** to encrypt; only the receiver's matching **private key** can decrypt. For authentication the sender can encrypt/sign with their **private key**, and anyone with the **public key** can verify. The public key may be published; the private key is never shared.

(c) A **digital signature** is a digest of the message encrypted with the sender's private key. The receiver hashes the message and decrypts the signature with the sender's public key; matching digests prove authenticity and integrity. A **digital certificate** is issued by a trusted **CA** and binds the sender's public key to their verified identity; it is signed with the CA's private key and verified with the CA's public key. This prevents someone from publishing a fake public key in another person's name.

**What the examiner wants:** precise "which key does what", plus the hash-and-compare mechanism. Vague statements like "keys keep it safe" earn nothing.

### Question 2 — SSL/TLS (15 marks)

(a) Explain the meaning of "protocol suite". [3]
(b) Describe a type of activity where SSL/TLS would be used. [4]
(c) Explain how digital certificates are used in the suite. [3]
(d) Explain how encryption keys are used in the suite. [5]

**Solution:**

(a) A protocol suite is a set of related protocols that work together at different stages of a communication, each handling a specific task. In SSL/TLS, the Handshake Protocol establishes security while the Record Protocol formats and protects the data.

(b) Any client–server activity where sensitive data crosses an untrusted network: online banking, e-commerce checkout with card details, logging into a webmail account, or submitting personal data on a form. The browser and server use HTTPS.

(c) The server presents its digital certificate, containing its public key and signed by a CA. The client verifies the CA's signature with the CA's public key and checks the identity, so it can trust that the public key belongs to the genuine server.

(d) The client generates a one-off symmetric **session key**, encrypts it with the server's **public key**, and sends it. The server decrypts it with its **private key**. Both then use the session key for fast symmetric encryption of the data. Asymmetric encryption is used only for key exchange/authentication; symmetric encryption protects the bulk data.

**What the examiner wants:** "suite = several protocols", "certificate proves server identity", and the hybrid key exchange. The phrase "session key" is usually an exact mark.

### Question 3 — Digital certificates (7 marks)

(a) Name three data items present in a digital certificate. [3]
(b) Explain why a certificate must be signed by a Certification Authority. [3]
(c) State one reason a certificate may be rejected by a browser. [1]

**Solution:**

(a) Owner's name/domain; owner's public key; validity dates; CA's digital signature; serial number. (Any three.)

(b) The CA is a trusted third party. Its signature proves that it has verified the owner's identity and that the public key genuinely belongs to that owner. Without it, an attacker could publish a public key under a false identity.

(c) The certificate has expired; the domain name does not match; the CA is not trusted; the signature is invalid.

### Question 4 — Symmetric vs asymmetric (6 marks)

A 1 GB file must be sent securely. Explain why a hybrid approach is used rather than encrypting the whole file with RSA.

**Solution:**

RSA is computationally expensive and very slow for large amounts of data, so encrypting 1 GB directly would take an impractical amount of time. Instead, a fast symmetric key (e.g. AES) encrypts the file. RSA is used only to encrypt the small session key with the recipient's public key. The recipient decrypts the session key with their private key and then decrypts the file symmetrically. This gives the security of asymmetric key exchange with the speed of symmetric encryption.

**What the examiner wants:** speed/overhead of asymmetric, speed of symmetric, and the role of each in the hybrid scheme.

### Question 5 — Quantum key distribution (6 marks)

(a) Explain how polarised photons can be used to create a shared secret key. [4]
(b) Give one advantage and one disadvantage of QKD. [2]

**Solution:**

(a) The sender encodes each bit using a randomly chosen polarisation basis and records the bit and basis. The receiver independently chooses a random basis for each photon and measures it. The sender publicly announces the bases used; the receiver identifies the positions where the bases matched. The bits at those positions form the shared secret. Positions with mismatched bases are discarded because the measured values are unreliable.

(b) Advantage: any eavesdropping disturbs the photons and is detectable, so security is based on physics rather than computational difficulty. Disadvantage: it needs a dedicated quantum channel and is expensive/limited in range; it cannot use ordinary network infrastructure.

**What the examiner wants:** random bases, public comparison of bases only, discard mismatches, and the no-cloning/eavesdropper-detection idea.

### Question 6 — Digital signature process (5 marks)

Describe the steps by which a receiver can verify that a message is authentic and unaltered.

**Solution:**

1. The receiver applies the agreed hash function to the received message, producing digest A.
2. The receiver decrypts the digital signature using the sender's public key, producing digest B.
3. The receiver compares A and B.
4. If they are identical, the message is authentic (it was signed with the sender's private key) and unaltered (any change would change the digest).
5. If they differ, the message is rejected.

**What the examiner wants:** hash → decrypt signature with public key → compare. The order and the key used are the marks.

---

# 📋 Formula / Fact Sheet (Chapter 21)

**Core terms:** plaintext, ciphertext, encryption, decryption, key, digest, digital signature, digital certificate, CA, PKI, session key.

**Five security concerns:** confidentiality, authenticity, integrity, non-repudiation, availability.

**Symmetric:** one shared secret key; fast; key distribution problem; DES, 3DES, AES.

**Asymmetric:** public key + private key; slow; public encrypts → private decrypts (confidentiality); private encrypts → public decrypts (signature); RSA.

**RSA:** `n = p × q`; `φ = (p−1)(q−1)`; choose `e` coprime to `φ`; find `d` with `de ≡ 1 (mod φ)`; public `(n,e)`, private `(n,d)`; `y = x^e mod n`; `x = y^d mod n`.

**Digital signature:** hash message → digest; encrypt digest with sender's private key; receiver hashes message and decrypts signature with sender's public key; compare digests.

**Certificate contents:** owner identity, public key, validity dates, CA signature, serial number.

**SSL/TLS:** sits between TCP and application layer; HTTPS = HTTP + SSL/TLS; Handshake Protocol + Record Protocol; server certificate → client verifies → client sends session key encrypted with server's public key → symmetric session.

**QKD:** random bases; compare bases publicly; keep matches; eavesdropping disturbs photons; needs dedicated quantum channel.

**Key sizes:** DES 56-bit key/64-bit block; AES 128/192/256-bit key/128-bit block; S-DES 10-bit key/8-bit block.

# ⚡ Quick Reference Card

1. **Encryption does not hide the fact that communication happened** — it hides the content.
2. **Symmetric = one key, fast, hard to share. Asymmetric = two keys, slow, easy to publish.**
3. **Public encrypts, private decrypts** → confidentiality. **Private signs, public verifies** → authenticity.
4. **Hash is one-way** — you cannot decrypt a digest; you recompute and compare.
5. **Digital signature = encrypted digest**, not an encrypted message.
6. **Certificate = public key + identity + CA signature.** The CA is the trust anchor.
7. **SSL/TLS handshake:** certificate → verify → session key → symmetric data.
8. **HTTPS** is HTTP carried inside SSL/TLS.
9. **RSA security = factoring a large `n` is hard.**
10. **QKD detects eavesdropping** because measuring a photon changes it; it does not encrypt the message itself.
11. **Brute force:** `2^n` keys for an `n`-bit key; longer key = more security but slower.
12. **Never reuse a session key** across sessions; one-off keys limit the damage if one is compromised.
