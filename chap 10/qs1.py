class programer:
    company="MICROSOFT"
    def __init__(self,name,salary,country):
        self.name=name
        self.salary=salary
        self.country=country
maryam=programer
sana=programer
hassam=programer
maryam=programer("maryam",600000,"india")
print(maryam.name,maryam.salary,maryam.country,maryam.company)

sana=programer("sana",20000,"uk")
print(sana.name,sana.salary,sana.country,sana.company)

hassam=programer("hassam",50000,"pakistan")
print(hassam.name,hassam.salary,hassam.country,hassam.company) 