from PIL import Image
import pytesseract

image_path = "한글이미지.png"

pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"
text=pytesseract.image_to_string(Image.open(image_path),lang="kor+eng")

print(text)