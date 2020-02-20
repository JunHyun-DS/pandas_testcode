import calc_module
JH = calc_module.calc()

def normal_calc():
    num1 = 0
    num2 = 0
    operator = ''
    operator_list = ['quit', '+', '-', '*', '/', '**']
    while True:
        if operator == operator_list[0]:
            break
        try:
            num1 = int(input("첫번째 수를 입력하세요: "))
        except ValueError:
            print("--수를 잘못입력했어요--")
            break

        result = num1  # 최종결과값
        result_1 = 0  # 최종 전의 결과값 ex) (1+1)+1=3 (1+1)에 해당

        while True:

            if result == "ZeroDivisionError":
                try:
                    num1 = int(input("\n첫번째 수를 입력하세요: "))
                    result = num1
                except ValueError:
                    print("--수를 잘못입력했어요--")
                    break

            operator = input("연산자를 입력해주세요(종료시 quit를 입력해주세요): ")
            if operator not in operator_list:
                print("등록되지 않은 연산자입니다~!")
                continue
            if operator == operator_list[0]:
                break
            try:
                num2 = int(input("두번째 수를 입력하세요: "))
            except ValueError:
                print("--수를 잘못 입력했어요--")
                break
            if operator == operator_list[1]:
                result_1 = result
                result = JH.add(result, num2)

            elif operator == operator_list[2]:
                result_1 = result
                result = JH.sub(result, num2)

            elif operator == operator_list[3]:
                result_1 = result
                result = JH.mul(result, num2)

            elif operator == operator_list[4]:
                try:
                    result_1 = result
                    result = JH.div(result, num2)

                except ZeroDivisionError:
                    print("\n분모가 0이 아닌지 확인해 보세요\n")
                    result = "ZeroDivisionError"

            elif operator == operator_list[5]:
                result_1 = result
                result = JH.squared(result, num2)

            print("%d %s %d = %s" % (result_1, operator, num2, result))


## 환율
def exchange_rate_calc():
    c_money = 0  # 각 나라의 돈
    money = 0
    result = ""
    country_list = ["japan", "usa", "china"]

    while True:
        country = input("나라를 선택하세요(종료시 quit를 입력해주세요): ")  ## japan, usa만 가능

        if country == "quit":
            break

        if country in country_list:
            try:
                money = int(input("얼마 환전하실건가요? (원화) "))
            except ValueError:
                print("돈인데 제대로 입력해주세요")
                break
        if country == country_list[0]:
            result = JH.JPY(money)
        elif country == country_list[1]:
            result = JH.USD(money)
        elif country == country_list[2]:
            result = JH.CNY(money)
            print("환전은 해주지만 안가시는걸 추천합니다.")
        else:
            print("입력하신 국가는 등록되있지 않습니다.")
            continue
        print(result)


