# Decentralized-Verifiable-Cloud-Storage
: Cloud-based storage of continuously generated streaming data introduces significant concerns related to data integrity, authenticity, and freshness. Traditional verification mechanisms are inefficient for large-scale dynamic data streams due to high computational and storage overheads

# Decentralized Verifiable Cloud Storage for Data Streaming

## 📌 Project Overview

This project implements a decentralized commitment-based verifiable cloud storage system for real-time data streaming. It ensures secure storage, integrity verification, and replay attack protection using lightweight commitment proofs in a simulated cloud environment.

## 🎯 Objectives

* Securely store streaming data in cloud simulation
* Provide commitment-based integrity verification
* Support batch verification of multiple data blocks
* Prevent replay and stale data attacks

## 🏗 System Modules

1. Data Owner Module – Generates and uploads streaming data
2. Cloud Storage Module – Stores data and commitment metadata
3. User Verification Module – Retrieves and verifies data integrity
4. Commitment Engine – Generates decentralized commitment hashes

## 🛠 Technology Stack

* Python
* Flask Framework
* REST APIs
* JSON Storage
* VS Code

## 🔐 Key Features

* Real-time streaming data storage
* Decentralized integrity verification
* Batch query support
* Lightweight authentication metadata
* Replay attack detection

## 🚀 How It Works

1. Owner uploads streaming data with commitments
2. Cloud server stores data + proof metadata
3. User requests data block
4. System verifies integrity using commitment comparison

## 📂 Project Structure

See `/src` folder for module-wise implementation.

## 📈 Future Scope

* Integration with AWS / Azure cloud storage
* Blockchain-based decentralized auditing
* Encrypted streaming data verification
