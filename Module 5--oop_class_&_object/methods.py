class phone:
    #attributes
    color = 'blue'
    print = 12345
    brand = 'oppo'
    features = ['camera', 'finger print', 'audio record']

    #methods
    # def call():
    #     print('hello bro how are you') # with
    def send_sms(self, phone, sms):
        text = f'sending sms to: {phone} and message: {sms}'
        return text

myPhone = phone()
res = myPhone.send_sms(415356, 'i am coming for you')
print(res)
# print(myPhone.call)