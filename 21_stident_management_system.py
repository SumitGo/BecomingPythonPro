# wap to create a class m1(python class) with minimum three static members with  objects, 5 object members, and access method and any other 2 methods(for changing some attributes).
# sms = student management system 

class sms:
    class_name = 'm1-python'
    class_mentor = 'Deepak sir'
    class_timing = '8am'

    def __init__(self, stud_name, roomno, attendance, fees, n_mocks):
        self.stud_name = stud_name
        self.roomno = roomno
        self.attendance = attendance
        self.fees = fees
        self.n_mocks = n_mocks

    # getter methods
    def get_details(self):
        return dict(name = self.stud_name,
                    roomno = self.roomno, 
                    Attendace = self.attendance,
                    Fees_paid = self.fees,
                    Mocks_taken = self.n_mocks,
                    rating = self.get_stud_rating())


    @staticmethod   
    def get_stud_rating():
        return 1
    def ajuBajuPrint(func, self, name):
        print('ye h: ', func)

        # print(*params)
        print('wow')
        func(self, name)
        print("hm bhi hu:", func)


    #setter methods
    @ajuBajuPrint(self, name)
    def ch_name(self, name):
        self.stud_name = name
        return self.stud_name
    
    def update_fees(self, fees):
        self.fees +=fees
        return self.fees
    
    def update_mocks(self):
        self.n_mocks+=1
        return self.n_mocks
    


chandu = sms('chandu', 'g4', 20, 45000, 12)
print(chandu.get_details())
print(chandu.get_stud_rating())
chandu.ch_name("Prabhu Deva")
print(chandu.get_details())
print(chandu.update_fees(25000))
print(chandu.get_details())
print(chandu.update_mocks())
print(chandu.get_details())








