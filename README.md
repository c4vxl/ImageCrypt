# ImageCrypt: Steganography Tool for Hiding Data in Images

ImageCrypt is a Python tool that allows you to hide files or text within images using a technique called steganography. Steganography is the practice of concealing one piece of information within another in a way that's difficult to detect.

---

## How it Works

ImageCrypt takes an input image and performs steganography to encode either bytes of data or text into the image's pixels. The encoded data is then hidden within the least significant bit of each pixel's color channel.

### Features

- **Byte Encoding:** Encode raw bytes into images.
- **Text Encoding:** Encode text messages into images.
- **File Encoding:** Encode entire files into images.

## Usage

1. Install the required Python package:
```bash
pip install Pillow
```

2. Clone the file `ImageCrypt.py` into your project.

3. Import the ImageCrypt class from the provided script:
```python
from image_crypt import ImageCrypt
```

4. Initialize an ImageCrypt instance with the path to your input image:
```python
image_crypt = ImageCrypt("input_image.png")
```

5. To encode data into the image:
```python
encoded_image = image_crypt.encodeText("Secret message to hide") # Encode a text
encoded_image = image_crypt.encodeFile("file_to_hide.txt") # Encode a file
```

6. To decode hidden data from the image:
```python
decoded_text = image_crypt.decodeText() # Decode text
decoded_file = image_crypt.decodeFile("hidden_file.txt") # Decode file
```

## Example
Check out the provided example code for a basic demonstration of how to use the ImageCrypt class. This exaple code will hide the text "test12345" in the image "example.png". After that, it will decode the text again and print it out.
```python
# Example usage
image_crypt = ImageCrypt("example.png")
encoded_image = image_crypt.encodeText("test12345")
hidden_data = image_crypt.decodeBytes()
print(hidden_data)
```

## Limitations
- Image size: The image must be large enough to accommodate the data you want to hide.
- Security: This tool provides a basic form of steganography, but it's not suitable for secure data encryption.

---

## Developer
This Project was Developed by [c4vxl](https://c4vxl.de)
