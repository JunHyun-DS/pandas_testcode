class calc():
    # 사칙연산
    def __init__(self):
        self.result = 0
        # self.num2 = 0
    
    def add(self, result, num2):
        self.result = result
        self.result += num2
    
        return self.result
    
    def sub(self, result, num2):
        self.result = result
        self.result = self.result - num2
    
        return self.result
    def div(self, result, num2):
        self.result = result
        self.result = self.result / num2
    
        return self.result
    
    def mul(self, result, num2):
        self.result = result
        self.result = self.result * num2
    
        return self.result
    
    def squared(self, result, num2):
        self.result = result
        self.result = self.result ** num2
    
        return self.result
    
    ## 환율
    def JPY(self, money):
        JPY = 1073.51 # 100엔
        c_money = round((money / JPY), 2) * 100
        result = str(c_money) + "엔"
        return result
    
    def USD(self, money):
        USD = 1180.80 # 1달러
        c_money = round((money / USD), 2)
        result = str(c_money) + "달러"
        return result
    def CNY(self, money):
        CNY = 169.84 # 1위안
        c_money = round((money / CNY), 2)
        result = str(c_money) + "위안"
        return result
