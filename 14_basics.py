from random import random

# employee salary calculator

def emp_sal(service_days, hours_per_day = 8): # service_days 30 or 31

    per_day_cost = 100 # rupees
    hours_per_day = 8   # hours of work per day, normally
    if hours_per_day-8 > 0:
        bonus = hours_per_day-8
        bonus_cost = 200 

    monthly_sal = per_day_cost * service_days + bonus * bonus_cost
    return monthly_sal

# student grade system
def gradings(marks):  # grading marks between 0 to 100(100 is included in the range)
    if 0<= marks <= 24:
        grade = 'f'
    elif 25<= marks <= 30:
        grade = 'e'
    elif 31<= marks <= 55:
        grade = 'd'
    elif 56<= marks <= 70:
        grade = 'c'
    elif 71<= marks <= 85:
        grade = 'b'
    elif 85<= marks <= 90:
        grade = 'a'
    elif 91<= marks <=100 :
        grade = 'a+'

    else:
        grade = ''

    return grade


# electricity bill generator
def e_bill(units):
    rate= 3
    if units <100:
        rate = 3
    elif 200<= units <1000 :
        rate = 5
    print("Your bill is: ", units * rate)


# ATM simulation
def atm_sim(debit_amout): # input the amout debited
    debit_amount = 100
    account_balance = 9000
    new_bal = account_balance - debit_amount
    return new_bal

def shopping_bill(item, bill, quantity=1): # use this function multiple times, in loop to enter multiple items, and calculate price
    total_price = bill, quantity
    return total_price

# number guessing game

def guess_number(guess):
    rand= random.random()
    return guess == rand

def pass_validator(password):
    good_pass = False
    if len(password) >= 8:
        good_pass = True
    for i in range(len(password)):
        if i in "!@#$%^&*()_+}{|:\"?/.,><;'[]'}":
            good_pass = True

    return good_pass

def voting_eligibility(age):
    if age<18:
        return "Can't vote, age less than 18"
    elif age>=18:
        return "Eligible to vote"

# def voting_system(**party_votes):
#     parties = {
#         'bajra': party_votes[]
#     }


# temperature converter

# celcius to fahrenheit
def ctof(degreec):
    f = degreec*(9/5) + 32
    return f
def ftoc(degreef):
    c = (degreef - 32 ) * (5/9)
    return c

# mini calculator