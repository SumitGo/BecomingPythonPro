# method overriding
class cal:
    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a
    
    def __sub__(self, other):
        return self.a - self.a
    
    def __mul__(self, other):
        return self.a * other.a
    
    def __truediv__(self, other):
        return self.a/ other.a
    
    def __floordiv__(self, other):
        return self.a // other.a

# obj1 = cal(5)
# obj2 = cal(12)

# print(obj1 + obj2)
# print(obj1 - obj2)
# print(obj1 * obj2)
# print(obj1 / obj2)
# print(obj1 // obj2)
# print(isinstance(5,tuple))


class sms:
    n_students = 100
    _school_name = "Dada giri public School"
    _principal_name = "Bhanu Prata Mishra"
    def get_school


# print(sms._sms__marks)