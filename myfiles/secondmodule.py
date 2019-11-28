class Employee():
    raise_amount=1.03
    def __init__(self,eid,name,salary,lob):
        self.name=name
        self.eid=eid
        self.name=name
        self.salary=salary
        self.lob=lob

    def raisesalary(self):
        self.salary=self.salary*raiseamount
        


class Developer(Employee):
    raise_amount=1.05
    def __init__(self,eid,name,salary,lob,techstack):
        super().__init__(eid,name,salary,lob)
        self.techstack=techstack

    def raisesalary(self):
        self.salary=self.salary*self.raise_amount


devpyth=Developer(123456,'sai',50000,'wbt','pythonstack')

devpyth.raisesalary()
print(devpyth.salary)

        
        
