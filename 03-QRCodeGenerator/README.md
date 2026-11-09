# 📱 Project 03: QR Code Generator

A simple Python-based QR Code Generator that converts URLs into downloadable PNG QR code images using the `qrcode` library.

## ✨ Features

- Convert URLs into QR codes.
- Generate QR code images in PNG format.
- Custom filename support.
- Automatic `.png` extension handling.
- Empty input validation.
- File-saving error handling.

## 🛠️ Technologies Used

- Python 3
- qrcode
- Pillow (PIL)

## 📚 Concepts Practiced

- Importing external Python libraries
- User Input (`input()`)
- String Methods (`strip()`, `endswith()`, `lower()`)
- Conditional Statements (`if-else`)
- Exception Handling (`try-except`)
- File Handling and Image Saving
- Working with Third-Party Packages

## 📁 Project Structure

```text
03-qr-code-generator/
│
├── qr_generator.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/hands-on-python-projects.git
```

**2. Navigate to the project directory**

```bash
cd hands-on-python-projects/03-qr-code-generator
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

```bash
python qr_generator.py
```

## 💻 Sample Output

```text
===== QR CODE GENERATOR =====

Enter your URL: https://github.com
Enter filename: github

QR Code generated successfully!

Saved as: github.png
```

The generated QR code image will be saved in the current working directory.

## 📦 Dependencies

The project uses the following external library:

- `qrcode[pil]`: Generates QR codes and saves them as image files.

Install using:

```bash
pip install "qrcode[pil]"
```

## 🎓 What I Learned

Through this project, I learned how to install and use third-party Python libraries, accept user input, manipulate strings, generate QR code images, and save files programmatically.

This project introduced me to using external packages to build practical applications with Python.

## 🚀 Future Improvements

- Add custom QR code colors.
- Allow users to customize QR code size and border.
- Support batch QR code generation.
- Add URL format validation.
- Allow users to select an output directory.

---

**Project Status:** Completed ✅

**Version:** 1.1

**Part of:** Hands-On Python Projects 🐍