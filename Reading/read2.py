import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('newTest.png', detail = 0)
print(result)