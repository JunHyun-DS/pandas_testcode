import calc_module
import calc_start

while True:
    category = input("어떤 용도로 계산기를 이용하실건가요? \n(1.사칙연산 2.환율 3.사용하지 않는다.) ")

    ## 사칙연산
    if category == "1":
        calc_start.normal_calc()
    ## 환율
    elif category == "2":
        calc_start.exchange_rate_calc()
    ## 종료
    elif category =="3":
        break
    ## 예외처리
    else:
        print("다시 입력해주세요")
        continue