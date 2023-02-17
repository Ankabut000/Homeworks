class Employee:
    def __init__(self, name, familiya, yosh, oylik, tajriba) -> None:
        self.ism = name
        self.familiya = familiya
        self.yosh = yosh
        self.oylik = oylik
        self.tajriba = tajriba
    
    def full_name(self):
        return f"{self.ism} {self.familiya}"
    
    def __str__(self) -> str:
        return f"""
Ism_sharifi: {self.full_name()}
Yosh: {self.yosh}
Tajriba: {self.tajriba}
Maosh: {self.oylik}
"""

class Developer(Employee):
    def __init__(self, name, familiya, yosh, oylik, tajriba, prog_lang) -> None:
        super().__init__(name, familiya, yosh, oylik, tajriba)  
        self.prog_lang = prog_lang
    
    def __str__(self) -> str:
        return f"""
{super().__str__()}Dasturlash tili: {self.prog_lang}
"""

class Manager(Employee):
    def __init__(self, name, familiya, yosh, oylik, tajriba, royxat=None) -> None:
        super().__init__(name, familiya, yosh, oylik, tajriba)
        self.ishchilar_soni = 0
        if royxat == None:
            self.royxat = []
        else:
            self.royxat = royxat
    
    def add_employee(self, emp: Employee):
        if emp.full_name() not in self.royxat:
            if emp.yosh>=18:
                self.royxat.append(emp.full_name())
                self.ishchilar_soni+=1
            else:
                print(f"{emp.ism} yoshingiz to'gri kelmadi.")
    
    def all_data_emp(self):
        pass

    def delete_employee(self, emp: Employee):
        try:
            self.royxat.remove(emp.full_name())
            self.ishchilar_soni-=1
        except:
            print("Mavjud bo'lmagan inson!")
    
    def __str__(self) -> str:
        return f"""
{super().__str__()}Ishchilar soni: {self.ishchilar_soni}
"""

dev1 = Developer("Anish", "Giri", 38, 2000, 3, "flutter")
dev2 = Developer("Boxodir", "xo'ja", 19, 3500, 2, "GO")
dev3 = Developer("husan", "Musa", 25, 1000, 2, 'Go')
dev4 = Developer("Sardor", "Toshkentov", 19, 1700, 2, "GO")
dev5 = Developer("NoName", "Noname", 26, 3000, 4, "Swift")
dev6 = Developer("Kimdur", "Kimdurov", 12, 15000, 6, "C++")


manager = Manager("Toshmat", "Eshmatov", 19, 15000, 0)

print(manager)

manager.add_employee(dev4)
manager.add_employee(dev5)
manager.add_employee(dev1)
manager.add_employee(dev6)

print(manager)

manager.delete_employee(dev1)
print(manager)
