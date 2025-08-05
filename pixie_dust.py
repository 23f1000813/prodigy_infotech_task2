from PIL import Image
import os

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure RGB mode
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Apply XOR encryption
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_path, key, output_path):
    encrypt_image(encrypted_path, key, output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage
if __name__ == "_main_":
    import argparse

    parser = argparse.ArgumentParser(description="Simple Image Encryptor/Decryptor using XOR.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to output image")
    parser.add_argument("--key", type=int, default=123, help="Encryption key (0–255)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input file not found.")
        exit()

    if args.mode == "encrypt":
        encrypt_image(args.input, args.key, args.output)
    elif args.mode == "decrypt":
        decrypt_image(args.input, args.key, args.output)