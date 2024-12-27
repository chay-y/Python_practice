import random

random_number = random.randint(0,100)

game_count = 0

print("1~100까지 숫자를 맞추는 게임입니다.")

while True : 
    game_count +=  1

    try: 
        my_number= int(input("숫자를 입력하세요.(종료하려면 0 입력) > "))
        if (my_number==0) :
            print("게임을 종료합니다.")
            break
        elif my_number <1 or my_number>100:
            print("1부터 100사이의 숫자를 입력하세요")
            continue
    except :
        print ("잘못된 입력입니다. 다시 입력하세요")
        continue

    if my_number > random_number :
        print("다운!")
    elif my_number < random_number :
        print("업!")
    else :
        print("축하합니다.",game_count,"번만에 맞추셨습니다.")
        break