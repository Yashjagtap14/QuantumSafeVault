# 🔐 QuantumSafeVault

A Python-based file encryption tool with support for **password-based encryption** and **post-quantum Kyber512 encryption**.  
Designed to demonstrate modern cryptography techniques including **AES file encryption, password protection, and post-quantum key generation**.

---

## 🧩 Project Overview

This tool enables:

- Encrypting and decrypting files using passwords  
- Generating Kyber512 post-quantum key pairs  
- Encrypting and decrypting files using Kyber keys  
- Viewing Kyber keys embedded in files for demo purposes  

### Post-Quantum Cryptography (PQC)

Post-quantum cryptography ensures that encrypted data remains secure **even against quantum computers**.  
**Kyber** is a Key Encapsulation Mechanism (KEM) selected in the **NIST PQC standardization process**.

---

## 🚀 Features

- 🔒 File encryption/decryption using passwords  
- 🛡️ Post-quantum Kyber encryption (educational simulation)  
- 📂 Supports files like PDFs, text, images, Excel  
- 📝 Display Kyber public keys embedded in encrypted files  

---

## 📦 Required Libraries and Running the Tool

### Required Python Libraries

- Python 3.10+  
- `cryptography`  
- `kyber-py` (for Kyber post-quantum features)  

### Installation and Running

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd QuantumSafeVault

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
.\venv\Scripts\Activate.ps1     # Windows PowerShell

# 3. Install dependencies
python -m pip install --upgrade pip
python -m pip install cryptography kyber-py

# 4. Run the tool
python secure_vault.py



