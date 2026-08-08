class kuchbhi:
    __var = 5
    def __init__(self, name):
        self.__name = name
        # print(self.__name)
    # private variables can be accessed only inside the class
    def get_func(self):
        print(kuchbhi.__var)
        print(self.__name)

obj = kuchbhi("shambhu")
obj.get_func()

# print(obj._kuchbhi__name)