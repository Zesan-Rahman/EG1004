import pytesseract
from PIL import Image

image_path = "Call.jpg"
image = Image.open(image_path)
text = pytesseract.image_to_string(image)
print(text)