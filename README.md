# Remote Print Service

### Lightweight Browser-to-Printer API

## 📚 Table of Contents
1. [Overview](#-1-overview--introduction)
2. [Example Usage](#-2-example-usage)
3. [Contact](#-3-contact)

## 🧠 1. Overview / Introduction

Remote Print Service is a lightweight web-based API designed for fast and seamless printing directly from a browser. Built using Python and Flask, it enables users to send print jobs to a connected printer through a simple, intuitive web interface. 

This project provides a minimal yet efficient backend solution for handling document uploads and print commands remotely - ideal for local networks, internal tools, or quick print automation setups.

## 📬 2. Example Usage

**Start the Server**
```bash
python3 app.py
```

**Access the Web Interface**
```sql
http://localhost:5000/
```

**Set up the Default Printer across HPLIP**
*The model works well with HP Printers*
```bash
lpadmin -d <printer name>
```

**Upload and Print a File**
1. Open the web interface.
2. Choose the file you want to print.
3. Press on **Upload** button
4. Review print information and press again **Print**


## 📫 3. Contact
Name: Lucian-Florin Cusmir