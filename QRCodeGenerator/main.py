import qrcode

print("===== QR CODE GENERATOR =====")

url = input("Enter your URL: ").strip()

if not url:
    print("Error! URL cannot be empty.")
    exit()

filename = input("Enter filename: ").strip()

if not filename:
    filename = "qrcode"

if not filename.lower().endswith(".png"):
    filename += ".png"

try:
    img = qrcode.make(url)
    img.save(filename)

    print(f"\nQR Code generated successfully!")
    print(f"Saved as: {filename}")

except OSError as e:
    print(f"Error saving QR code: {e}")