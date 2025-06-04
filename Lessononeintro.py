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

    def agecheck(self,a):
        if a !=self.age:
            print ("The age listed has been changed. Happy birthday!")
            self.age=a
        else:
            print("Not your birthday yet")



s1= students("Kuriyan","13","54321")
s2= students("Quinn","12","12345")





p=input("Enter password : ")
s1.login(p)
s2.login(p)
a=input("Enter age : ")
s1.agecheck(a)
s2.agecheck(a)



    
    

