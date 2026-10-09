class calculator:
    #attributes here
    # ---------
    
    # methods here
    def calculate(self, num1,num2, symbol):
        ans = 0
        if symbol == '+':
            ans = num1 + num2
        elif symbol == '*':
            ans = num1 * num2
        elif symbol == '-':
            ans = num1 - num2
        elif symbol == '%':
            ans = num1 % num2
        else:
            ans = num1 // num2
        return ans

num1 = int(input())
symbol = input()
num2 = int(input())

calcu = calculator()
result = calcu.calculate(num1, num2, symbol)

print('>>>>')
print(f'this is the answer: {result}')


