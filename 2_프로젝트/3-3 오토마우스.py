import pyautogui
import time
import pyperclip

날씨=["서울 날씨","울산 날씨","제주도 날씨","평택 날씨"]

addr_x=1119
addr_y=64

start_x=996
start_y=216

end_x=1518
end_y=728

for 지역날씨 in 날씨 :
    pyautogui.moveTo(addr_x, addr_y, 1)
    time.sleep(0.2)
    
    pyautogui.click()
    time.sleep(0.2)
    
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)
    
    pyperclip.copy(지역날씨)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    저장경로 = "날씨\지역날씨" + 지역날씨 + ".png"
    pyautogui.screenshot(저장경로, region=(start_x, start_y, end_x-start_x, end_y-start_y))