class Phone:
    def __init__(self):
          print('i am constructor')
    def display(self):
          print('i am method')
# method bahirew lekhe jabe
def outside_fun(self):
     print('i am out side method')

Phone.outside_fun = outside_fun # eta phone object create er age phone er moddhe dhokaite hoibo
p = Phone()

# print(Phone.__dict__)
print(Phone.__dict__.keys())
