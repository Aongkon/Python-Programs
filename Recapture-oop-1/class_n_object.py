class Phone:
    def __init__(self):
        print('i am constructor')
    def display(self):
        print('i am method')
    def __del__(self): # Destructor shob kaj ses howar por distroy hobe
        print('i am destructor')

phon = Phone()
phon.display()