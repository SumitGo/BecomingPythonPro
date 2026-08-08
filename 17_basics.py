# Functional arguments

# positional arguments
# def names(*args):
#     return args
# print(names('sumit', 'mahesh', 'suresh', 'jayesh','ganesh'))
# # keyword args

# def properties(**props):
#     for key, value in props.items():
#         print(f'{key}: {value}')
    
# print(properties(
#     name='baba',
#     surname='gaga',
#     raag='malhar',
#     git='tansen sur',
# ))

# default args
# def rangoli(color=True, bullet=False, *cols):
#     # print(cols)
#     return cols

# # out=(rangoli('baigani', 'gulabi','narangi','hariya'))
# out=rangoli('baigani', 'gulabi','narangi','hariya')
# print(out)

#variale length arguments
# def resource(*items)


# calculate interest

# def cal_interest(p,rate, duration):
#     # p=100
#     # rate =1.5
#     # duration=2 #years
#     interest = p*rate*duration/100
#     return interest

# out = cal_interest(100,1.5,2)
# print(out)


# stident details function 

# def details(**kwargs):
#     return kwargs

# out=details(
#     name='pandey',
#     method='chulbule',
#     practice='lathi',
#     soil='mati',
#     kahna='bhati'
# )
# print(out)


# employee details function
# def emp_details(**kwargs):
#     for key,val in kwargs.items():
#         if key.lower()=='name':
#             return (key,val)
#     return kwargs

# out= emp_details(
#     # name='achar',
#     first_name='bhrashta',
#     milake='bhrashtachar',
#     maihu='lachar',
#     doing='vichar',
# )

# print(out)


# shopping bill calculator
def total_bill(**items):
    total_price=0
    for val in items.values():
        total_price+=val
    return val

out=total_bill(
    product='laptop',
    price= 1234
)

