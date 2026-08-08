class bank:
    __name= 'SEBI'
    mobile = 9837539894
    __amount = 3457
    def __init__(self, accountno, depositor_name,mobile=mobile):
        print(self.mobile)
        self.accountno = accountno
        self.depositor_name = depositor_name
        self.mobile = mobile
        

    @classmethod 
    def amount_update(cls, amount):
        print(cls)
        cls.accountno = 1
        cls.amount -= amount
        return cls.amount
    
    def ch_mobile(self,mobile_no):
        self.mobile = mobile_no


b = bank(23423546726, 'maruti bajaj', 9876586468)
# print(b.accountno)
print(b.mobile)
b.ch_mobile(12345679)
print(b.mobile)



# print(b.mobile)
# print(bank.mobile)



# current_amount = b.amount_update(23)
# print(current_amount)
