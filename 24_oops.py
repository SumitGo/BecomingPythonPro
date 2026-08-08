# wap to find the sum of two numbers using object method and class method and static method


class s:
    a = 1
    b = 2
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obj_add(self):
        return self.a + self.b
    
    @classmethod
    def class_add(cls):
        return cls.a + cls.b
    
    @staticmethod
    def static_add(a,b):
        return a+b 

num = s(5,4)
print(num.obj_add())
s.a = 4
s.b = 12
print(num.class_add())

print(num.static_add(6,5))
