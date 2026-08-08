# Revision of OOPS

# class zoo:
#     prime = 'Elephant'
#     elegant = 'Humming Bird' 
#     __killer = 'Wolf'
#     def __init__(self, prime, elegant, killer):
#         self.prime = prime
#         self.elegant = elegant
#         self.__killer = killer

#     @staticmethod
#     def newbie():
#         return "m hu don"
#     #def func(s,p, e, k):
#         # s.prime = p
#         # s.elegant = e
#         # s.__killer = k


# ob = zoo('octopus', 'kankrej', 'Human')
# # ob2 = zoo()
# # ob.func('octopus', 'kankrej', 'Human')
# print(ob.prime, ob.elegant, ob._zoo__killer)
# ob._zoo__killer = "ravan"
# print(ob.prime, ob.elegant, ob._zoo__killer)
# # ob.elegant = 'octopus'
# # ob2.prime = 'Kankrej'

class bank:
    bname = 'dhandha bank'
    bloc = 'khatra'
    bifsc = 'dhnd0001234233'
    def __init__(self, name, bal, accno):
        self.name = name
        self.bal = bal
        self.accno = accno
    def deposit(self, amt):
        self.bal = self.add(self.bal, amt)

    def withdrawl(self, amt):
        if self.bal<amt:
            return "Insufficient Balance"
        self.bal = self.add(self.bal, amt)

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

    