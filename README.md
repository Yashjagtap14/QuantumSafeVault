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


**Menu Options**

1️⃣ Encrypt a file with password  
2️⃣ Decrypt a file with password  
3️⃣ Generate Kyber keys 🔑  
4️⃣ Decrypt file with Kyber (extract embedded key) 📄  
0️⃣ Exit  

**🖼️ Example Output / Screenshots**

**Step 1: Generate Kyber Keys**  
<img width="856" height="266" alt="pro1" src="https://github.com/user-attachments/assets/633b7066-b5ee-4a87-9db8-97421608270e" />


**Step 2: Encrypt/Decrypt a file**  
<img width="1370" height="113" alt="pro 2" src="https://github.com/user-attachments/assets/b92df843-5af6-45de-b076-feebb25a4b85" />
 

**📚 Detailed Notes**

- AES encryption with password is fully functional.  
- Kyber512 post-quantum encryption is included for demonstration purposes.  
- Encrypted files can contain embedded Kyber public keys to verify post-quantum workflow.  
- Replace `<your-repo-url>` with your GitHub repo URL.  
- Replace screenshot placeholders with actual images.  

**⚙️ Requirements**

- Python 3.10+  
- Linux / Windows / macOS  
- Virtual environment recommended  

**💡 License**

MIT License


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

