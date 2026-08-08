
class online_bank:

    # customer_name = 'hi'
    # aadhaar_no = 123345465677
    # account_type = "fd"
    # mobile_no = 98365739374
    # email_id = "somemail@email.com"

    def __init__(self, customer_name, aadhaar_no, account_type, mobile_no, email_id):
        self.customer_name = customer_name
        self.aadhaar_no = aadhaar_no
        self.account_type= account_type
        self.mobile_no = mobile_no
        self.email_id = email_id

    def details(self):
        return self.aadhaar_no, self.account_type
    
class offline_bank(online_bank):
    bank_name = "boi"
    branch = 'saket'
    ifsc_code = 'BOI00000230478234'

    def __init__(self):
        pass

    # def __init__(self, customer_name, aadhaar_no, account_type, mobile_no, email_id):
    #     super().__init__(customer_name, aadhaar_no, account_type, mobile_no, email_id)


    def get_details(self):
        return self.customer_name
    
    def details(self):
        super().details()
        return self.ifsc_code

user = offline_bank("babuRao", 123456789089, "FD", 9876543210, "ganpatraoapte@gmail.com")
print(user.get_details())
print(user.details())