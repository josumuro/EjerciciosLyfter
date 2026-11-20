class Employee:
    def __init__(self,name:str,salary:float):
        self.__name = name
        self.__salary = salary


    @property
    def name(self):
       return self.__name
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary

    def promote(self,amount:float):
        self.salary += amount


    def __str__(self):        
        return f"Employee(Name: {self.name}, Salary: {self.salary})"
# example usage
employee=Employee("Josue Ocampo", 50000)
print(employee) 
employee.promote(5000)
print(employee) 
    



