class students():

    def __init__(self,name,age,password):
        self.name= name
        self.age= age
        self.password=password

    def login(self,p):
        if p==self.password:
            print("login succesfull")
        else:
            print("incorrect password")


s1= students("Kuriyan",13,"54321")
s2= students("Quinn",12,"12345")

print(s1.name)
print(s2.age)

p=input("Enter password : ")
s1.login(p)
s2.login(p)

