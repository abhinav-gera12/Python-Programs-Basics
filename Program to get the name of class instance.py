#Program to get the name of class instance

class smartphone:
    def name(self,name):
        return name
    
s1 = smartphone()
print(s1.__class__.__name__)