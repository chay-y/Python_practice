from gtts import gTTS               # 텍스트를 음성파일로 변환
from playsound import playsound     # 음성파일을 재생하는 라이브러리
import os

# 현재 실행중인 파이썬 파일의 폴더로 직접 경로를 변경
os.chdir(os.path.dirname(os.path.abspath(__file__)))


file_path ='나의텍스트.txt'
with open(file_path,'rt',encoding='UTF8')as f:
    read_file = f.read()

tts = gTTS(text=file_path, lang='ko')

tts.save("hi.mp3")

playsound("hi.mp3")