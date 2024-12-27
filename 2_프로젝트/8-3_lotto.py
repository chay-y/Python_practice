import tkinter
import tkinter.font
import random

lotto_num = range(1, 46)

def buttonClick():
    print(random.sample(lotto_num,6))

window=tkinter.Tk()                     # 메인 창을 생성
window.title("lotto")                   # 제목표시줄에 표시
window.geometry("400x200+800+300")      # 400X200사이즈의 창을 설정하고, X축을800, Y축을300좌표에 창을 출력
window.resizable(False, False)          # 창의 크기를 변경할 수 없도록 설정
 
# window : 부모창, overrelief="solid" : 외곽선 표시
# text : 버튼의 글자, width : 가로 크기
# command : 버튼을 클릭할 때 실행할 함수 지정
# repeatdelay, repeatinterval : 반복입력이 1초 후에 시작되고, 0.1초 간격으로 반복되도록 설정
button = tkinter.Button(window, overrelief="solid", text="번호확인",width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)

# 창을 화면에 배치
button.pack()

# 창이 닫힐때까지 반복해서 실행
window.mainloop()
