# oops coding 

# class zoo():
#     _a='tiger'
#     b='cheetah'
#     c= 'hathi'
#     @staticmethod
#     def __hide():
#         print("hell")

# koi = zoo()
# jadu = zoo()
# zoo.c = 'anaconda'
# print(koi._a, koi.b)
# print(koi.c)
# print(jadu.c)

# koi._zoo__hide()


# WAP TOO CREATE A CLASS HOSPITAL WITH FOIR STATIC MEMBERS, TWO OBJECT WITH MINIMUM 7 OBJECT MEMBERS
class hospital:
    name= 'MuktiAspatal'
    slogan = 'chinta se mukti'
    features = 'advances robotics surgery'
    multispeciality = True

    def details(obj, name, loc, special, slogan, bima, refer, multispeciality):
        obj.name = name
        obj.loc = loc
        obj.special = special
        obj.slogan= slogan
        obj.bima = bima
        obj.refer = refer
        obj.multispeciality = multispeciality


nagari = hospital()
puri = hospital()


# nagari.details('chikitsalaya', 'Swarg nagari', 'LASIK', 'netra ki shuddhi', ['hdfc', 'icici'], 'vaikunth Aspatal', False)

# puri.details('nirogi kendra', 'mayandari', 'Nano Biotics', 'adhunik taknik k sath', ['hdfc', 'icici', 'yamSuraksha'], 'akshar Aspatal', True)




# nagari.name= nagari.name + 'chikitsalaya'
# nagari.loc = 'Swarg nagari'
# nagari.special = 'lasik'
# nagari.slogan = nagari.slogan + 'netra ki shuddhi'
# nagari.bima = ['hdfc', 'icici']
# nagari.refer= 'vaikunth Aspatal'
# nagari.multispeciality = False


# puri.name = puri.name + 'nirogi kendra'
# puri.loc = 'mayandari'
# puri.special = 'nano biotics'
# puri.slogan = puri.slogan + 'adhunik taknik k sath'
# puri.bima = ['hdfc', 'icici', 'yamSuraksha']
# puri.refer= 'akshar Aspatal'
# puri.multispeciality = True

# print(nagari, puri)


class bank:
    def __init__(self, name, accountno, phno, email, addr):
        self.name = name
        self.accounto