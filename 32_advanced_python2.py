import csv, json, pickle

# a = open('file.json', "w")
# data = '{"key":{"value":[1,2,3]},"1":"habibi"}'
# # a.write(data)
# a.writelines((data, data + '{"don": "m hu kon"}'))
# a.close()


# a = open("new_file.txt", "w")
# data = "heyy, how are you"
# data2 = "well done "
# data3 = "kuch bhi"

# a.writelines([data,data2,data3]) # writelines can take multiple arguments in form of an iterable like a list or a tuple
# a.close()

# a = open("file.txt","r")
# data = a.read() # reads full file characters
# d2 = a.read(10) # reads first 10 characters from the file, and moves the curson pointer to 10 characters ahead
# print(d2)
# print(data)

# data = a.readline() # read a line untile a newline character is hit
# d2 = a.readline(5) # we can also metion size inside this method and it will return that many characters from the current curson position
# print(data,d2)
# print(d2)

# readline method reads one line at a time, so we need readlines to read multiple lines at a time 

# a = open('file.txt', 'r')
# # d1 = a.readlines() # returns all the lines of the file in a list 
# # print(d1)
# d2 = a.readlines(19) # 19 is the number of characters that is read, if number exceeds the characters of a line, then this method returns the next line as well
# print(d2)
# a.close()
# a = open('file.txt', 'a')
# a.write("mishri wali mithai")


# a = open("data.csv",'w')
# var = csv.writer(a)
# var.writerow(['hell', True, 1])
# var.writerows([['narak', 'sahi', 2], ['Swarg', 'nahi', 3], ['kuch bhi', 'only data', 4], ['linux', 'no bi tools', 5]])
# a.close()


# var = open("data.csv",'r')
# var2 = csv.reader(var)
# v = csv.reader(var, dialect='excel')
# # print(var2)
# print(list(var2))

# encryption
# data = [ 10, 20, 30, 40]
# data = {
#     "key":{"halloween":True}
# }
# print(type(data))
# enc_data = json.dumps(data)
# # enc_data = str(data)
# a = open('file.txt', 'w')
# a.write(enc_data)
# a.close()

# a = open('file.txt', 'r')
# enc_data = a.read()
# org_data = json.loads(enc_data)
# print(org_data)
# print(type(org_data))
# print(type(enc_data))
# a.close()

# data = [10, 20, " hello"]
# encap_data = pickle.dumps(data)
# with open('pick_file','wb') as f:
#     l = f.write(encap_data)
#     print(l)


# with open('pick_file', 'rb') as f:
#     out = f.read()
#     org_data = pickle.loads(out)
#     print(org_data)


# TRY AND EXCEPT BLOCK-- EXCEPTION HANDLING

def div():
    try:
        a = int(input("Enter first number"))
        b = int(input("Second number: "))
        c = a/b
        print(c)

    # SPECIFIC EXCEPTION
    # except ZeroDivisionError:
    #     print('Common dude, no 0 in denominator!!!')
    # except TypeError:
    #     print("no bro, you are making typeError")
    # except SyntaxError:
    #     print("Bhai thik se likh")
    # except ValueError:
    #     print("bhaiya thik thik value doooo.")
    # GENERIC EXCEPTION
    # except Exception as e:
    #     print("Le bhai tera error",e)

    # DEFAULT EXCEPTION
    except:
        print("Agya error")
# div()

#RAISING CUSTOM EXCEPTIOIN 
# name = 3
# if name == 3:
#     print("Maya")
# else:
#     raise NameError('AE paglu, kya likh rhe ho, jra dekh ke')

# CREATING CUSTOM ERROR
class NotAvailableError(Exception):
    pass

name = 10
if name >=2000:
    print('hi hello')

else:
    raise NotAvailableError("kya bhai kya kr rha h, error aya h")