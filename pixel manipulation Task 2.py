from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print(f"Image encrypted and saved as '{output_path}'")

def decrypt_image(input_path, output_path, key=None):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap red and blue channels back to original
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print(f"Image decrypted and saved as '{output_path}'")

# Image paths
input_image = r"C:\Users\Dell\OneDrive\Desktop\Prodigy\car.jpg"
encrypted_image = r"C:\Users\Dell\OneDrive\Desktop\Prodigy\encrypted_image.jpg"
decrypted_image = r"C:\Users\Dell\OneDrive\Desktop\Prodigy\decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)
