# # 1 Problem

# class Kitob:
#     def __init__(self,nomi:str,muallifi:str,narxi:int,nashriyoti:str):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.narx = narxi
#         self.nashr = nashriyoti

#     def check(self):
#         a = list("ABCDEFGHabcdefgh")
#         if self.nashr[0] in a:
#             self.info()

#     def info(self):
#         print(f"""
# Kitob nomi: {self.nomi}
# Kitob Muallifi: {self.muallifi}
# Kitob narxi: {self.narx}
# Kitob nashriyoti: {self.nashr}
#         """)
# lst = []
# for i in  range(int(input(">>> "))):
#     nom = input("Kitob nomini kiriting: ")
#     muall = input("Kitob muallifini kiriting: ")
#     narxii = int(input("Kitob narxini kiriting: "))
#     nashriyott = input("Kitob nashriyotini kiriting: ")
#     obj = Kitob(nom,muall,narxii,nashriyott)
#     lst.append(obj)
#     print()

# for i in range(len(lst)):
#     lst[i].check()

###########################################

# # 2 Problem

# class Kompyuter:
#     def __init__(self,NOM,RAM,NARX,PROSS) -> None:
#         self.nomi = NOM
#         self.rami = RAM
#         self.narxi = NARX
#         self.pros = PROSS

#     def check(self):
#         if self.rami>=4 and 16>=self.rami:
#             self.info()
        
#     def info(self):
#         print(f"""
# Nomi: {self.nomi}
# RAM: {self.rami}
# Narxi: {self.narxi}
# Protsessori: {self.pros}
# """)
# lst = []
# for i in  range(int(input(">>> "))):
#     nom = input("Kompyuter nomini kiriting: ")
#     ram = int(input("Kompyuter ramini kiriting: "))
#     narxii = int(input("Kompyuter narxini kiriting: "))
#     protsessor = input("Kompyuter protsessorni kiriting: ")
#     obb = Kompyuter(nom,ram,narxii,protsessor)
#     lst.append(obb)
#     print()
# for i in range(len(lst)):
#     lst[i].check()

###########################################

# # 3 Problem

# class User:
#     def __init__(self,name,surname,email,phone_number,age):
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.phone_number = phone_number
#         self.age = age

#     def get_info(self):
#         print(f"""Foydalanuvchi
# Name: {self.name}
# Surname: {self.surname}
# Email: {self.email}
# Phone number: +{self.phone_number}
# Age: {self.age}
# """)

# lst = []
# for i in  range(int(input(">>> "))):
#     name = input("Ism kiriting: ")
#     surname = input("Familiya kiriting: ")
#     email = input("Email kiriting: ")
#     phone_number = int(input("Telfon raqam: +"))
#     age = int(input("Yosh kiriting: "))
#     obb = User(name,surname,email,phone_number,age)
#     lst.append(obb)
#     print()
# for i in range(len(lst)):
#     lst[i].get_info()

# print("\nAbout myself👇\n")
# selfinfo = User("Salohiddin","Sunnatov","ankabut571@gmail.com",94_044_50_02,19)
# selfinfo.get_info()

