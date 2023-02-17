# class Weapon:
#     def __init__(self, nomi, type):
#         self.nomi = nomi
#         self.type = type
#         if self.type == "avtomat":
#             self.__soni = 30
#             self.damage = 15
#         elif self.type == "pistik":
#             self.__soni = 7
#             self.damage = 10
    
#     def otish(self):
#         self.__soni-=1
#         if self.__soni == 0:
#             self.oqlash()

#     def oqlash(self):
#         if self.type == 'avtomat':
#             self.__soni = 30
#         elif self.type == 'pistik':
#             self.__soni = 7

# class Player:
#     def __init__(self, nick, weapon: Weapon) -> None:
#         self.__health = 100
#         self.wp = weapon
#         self.nick = nick
    
#     def oqlash_weaponni(self):
#         self.wp.oqlash()
    
#     def get_health(self):
#         return f"{self.nick} -> {self.__health}"

#     def set_jon(self, obj):
#         obj.__health -= self.wp.damage
#         if obj.__health<=0:
#             print(f"{obj.nick} is DEAD by {self.nick}")
#             exit()
    
#     def otish_weaponni(self, obj):
#         self.wp.otish()
#         self.set_jon(obj)


# if __name__ == "__main__":
#     w1 = Weapon("deagle", 'pistik')
#     w2 = Weapon("AK-47", 'avtomat')

#     p1 = Player("Isco", w1)
#     p2 = Player("Jaxa", w2)

#     while True:
#         p1.otish_weaponni(p2)
#         print(p2.get_health())
#         p2.otish_weaponni(p1)
#         print(p1.get_health())

###########################################################################



# class Card:
#     def __init__(self, nomi, srok,pin):
#         self.__balans = 0
#         self.__pin = pin
#         self.nomi = nomi
#         self.srok = srok

#     def get_balans(self):
#         return f"Balans: {self.__balans} ming so'm"

#     def pin(self,pin):
#         return 1 if self.__pin == pin else 0
    
#     def set_pin(self, old_pin):
#         if old_pin == self.__pin:
#             self.__pin = int(input("Enter new pin: "))

#     def set_minus_balans(self, yechish):
#         if yechish > self.__balans:
#             return f"Pul yechish uchun kartada mablag' yetarli emas."
#         else:
#             self.__balans -= yechish
#             return f"Muvaffaqiyatli yechildi!"

#     def set_plus_balans(self, new_summa):
#         self.__balans += new_summa
    
#     def info(self):
#         return f"""Karta malumotlari:
# Nomi: {self.nomi}
# Muddati: {self.srok}
# Balans: {self.__balans}
# Pinkod: {self.__pin}.
# """

# if __name__ == "__main__":

#     # Enter your own
#     kard = Card("Humo","03/24",1111)

#     pinkod = int(input("Pin kodni kiriting: "))
#     if kard.pin(pinkod):
#         while True:
#             print("""
# [1] -> Balansni ko'rish
# [2] -> Balansga pul qo'shish
# [3] -> Balansdan pul yechish
# [4] -> Pin almashtirish
# [5] -> Info
# [0] -> EXIT
#     """)
#             n = int(input())
#             if n == 1:
#                 print(kard.get_balans())
#             elif n==2:
#                 kard.set_plus_balans(int(input("Necha pul qo'shmoqchisiz: ")))
#                 print(kard.get_balans() + ' ' + 'qo\'shildi')
#             elif n==3:
#                 print(kard.set_minus_balans(int(input("Necha pul yechmoqchisiz: "))))
#             elif n==4:
#                 kard.set_pin(pinkod)
#                 print("Pinkod muvaffaqiyatli almashtirildi!")
#             elif n==5:
#                 print(kard.info())
#             elif n==0:
#                 exit()
#     else: print("Pin kod xato kiritildi!")
