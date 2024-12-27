from PIL import Image
import pytesseract

image_path = r"한글이미지.png"

pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"
text=pytesseract.image_to_string(Image.open(image_path),lang="kor+eng")

print(text)

with open("한글변환.txt","w",encoding="utf8") as f:
    f.write(text)