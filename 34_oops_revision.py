class zoo:
    prime = 'Elephant'
    elegant = 'Humming Bird' 
    __killer = 'Wolf'
    def func(s,p, e, k):
        s.prime = p
        s.elegant = e
        s.__killer = k


ob = zoo()
ob2 = zoo()
ob.func('octopus', 'kankrej', 'Human')
print(ob.prime, ob.elegant, ob._zoo__killer)

ob.elegant = 'octopus'
ob2.prime = 'Kankrej'