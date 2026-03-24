"""class student:
    #name="yash"
    def __init__(self,name):
        self.name=name

s1=student("YASH SINHA")
print(s1.name)"""

class account:
    def __init__(self,bal,accno):
        self.bal=bal
        self.accno=accno
    
    def debit(self,amount):
        self.bal-=amount
        print(self.bal)
    
    def credit(self,amount):
        self.bal+=amount
        print(self.bal)

    def get_balance(self):
        return self.bal
        
    

acc=account(1000,1234)
acc.debit(200)
acc.credit(2000)

print(acc.get_balance())
        
        