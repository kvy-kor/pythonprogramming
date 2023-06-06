number = input("정수 입력 : ")
last_character = number [-1]

last_number = last_character

if last_number in "02468":
    print("짝수입니다.")

if last_number in "13579":
    print("홀수입니다.")

