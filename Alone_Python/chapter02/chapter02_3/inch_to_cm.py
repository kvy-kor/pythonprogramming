#숫자를 입력 받습니다.
raw_input = input("inch 단위 숫자를 입력해주세요: ")

#입력 받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경
inch = int(raw_input)
cm = inch * 2.54

#출력
print(inch, "inch는 cm 단위로", cm, "cm 입니다.")