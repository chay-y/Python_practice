import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"c:\Program Files\Tesseract-OCR\tesseract.exe"
languages = pytesseract.get_languages(config='')
print(languages)