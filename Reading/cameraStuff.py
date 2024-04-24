from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

def flatten(items, seqtypes=(list, tuple)):
    for i, x in enumerate(items):
        while i < len(items) and isinstance(items[i], seqtypes):
            items[i:i+1] = items[i]
    return items

def getName(result):
    names = []
    for item in result:
        if(isinstance(item, str)):
            names.append(item)
    return names

def rotate(fileName, degree):
    originalImg = Image.open(fileName)
    rotatedImg = originalImg.rotate(degree)
    rotatedImg.save("Rotated.jpg")

ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)
result = ocr.ocr("derrick.jpg")
rotate("derrick.jpg", 90)
result = flatten(result)
print(result)
print(getName(result))