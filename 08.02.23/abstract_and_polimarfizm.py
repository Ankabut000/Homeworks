# 1 Problem
# class Mylist(list):
#     def remove(self, __value) -> None:
#         __count1 = self.count(__value)
#         if __value in self:
#             for i in range(__count1):
#                 super().remove(__value)
#         else:print("Bunday qiymat mavjud emas!")

# my = Mylist([1,2,3,1,2,2,21,1,2,2,3,2,1])
# my.remove(2)
# print(my)






# 2 Problem
# class Mylist(list):
#     def append(self, __object) -> None:
#             if __object not in self:
#                 super().append(__object)
#             elif __object in self:
#                 print("Element is dublicated")
# my = Mylist()
# my.append(1)
# print(my)
# my.append(2)
# print(my)
# my.append(1)






# 3 Problem
# class Asosiy:
#     Phone=[ '+998 33 651 31 24',
#             '+998 33 677 41 04',
#             '+998 33 566 62 04',
#             '+998 33 742 82 45',
#             '+998 62 299 67 26',
#             '+998 33 554 13 04',
#             '+998 55 909 84 80',
#             '+998 90 474 95 41',
#             '+998 90 061 55 33',
#             '+998 88 796 23 94',
#             '+998 33 571 33 62',
#             '+998 33 404 57 99',
#             '+998 33 301 37 38',
#             '+998 88 117 73 49',
#             '+998 33 211 04 23',
#             '+998 55 906 58 43',
#             '+998 55 909 42 11',
#             '+998 33 835 00 54',
#             '+998 62 299 75 40',
#             '+998 88 621 52 65',
#             '+998 88 895 68 28',
#             '+998 88 605 56 87',
#             '+998 71 982 19 12',
#             '+998 33 124 79 13',
#             '+998 88 636 74 68',
#             '+998 55 903 88 20',
#             '+998 33 297 52 01',
#             '+998 55 503 78 37',
#             '+998 33 230 79 78',
#             '+998 61 298 46 75',
#             '+998 98 094 42 10',
#             '+998 55 909 55 39',
#             '+998 98 572 22 97',
#             '+998 91 657 21 33',
#             '+998 33 946 08 67',
#             '+998 88 880 65 46',
#             '+998 55 503 26 39',
#             '+998 88 028 69 47',
#             '+998 33 081 08 97',
#             '+998 33 772 60 80',
#             '+998 88 694 22 74',
#             '+998 55 909 16 05',
#             '+998 55 906 26 75',
#             '+998 94 727 45 55',
#             '+998 55 503 73 82',
#             '+998 33 817 92 84',
#             '+998 74 988 20 94',
#             '+998 88 996 44 49',
#             '+998 33 943 90 87',
#             '+998 33 849 80 58']



# class Operator(Asosiy):
#     def get_info_operators(self):
#         __lst = []
#         for i in self.Phone:
#             __lst.append(i[5:7])
#         return set(__lst)
    
#     def get_info_numbers(self):
#         __obj = []
#         for i in self.Phone:
#             __obj.append(i[7:])
#             # print(i[7:])
#         return set(__obj)
# op = Operator()
# # # print(op.get_info()) Operatorlarini chiqaradi (takrorlanmagan holatda)
# for i in op.get_info_numbers():print(i) # No'mer larni chiqaradi (takrorlanmagan holatda)






# 4 Problem

# class Ism_familiya(list):
#     Names=[
#     'Vivian Kidd',
#     'Bradyn Grant',
#     'Alexis Strickland',
#     'Madeleine Dunn',
#     'Emanuel Deleon',
#     'Charlotte Moody',
#     'Ian Wells',
#     'Greyson Sellers',
#     'Abril Cordova',
#     'Julissa Wolf',
#     'Gabrielle Osborne',
#     'Brian Webster',
#     'Ethen Charles',
#     'Ashtyn Cowan',
#     'Brycen Benson',
#     'Thomas Sexton',
#     'Brynlee Park',
#     'Keaton Pena',
#     'Lily Ochoa',
#     'Jaycee Glass',
#     'Anderson Stark',
#     'Alexandria Harper',
#     'Derek Cooley',
#     'Savannah Coleman',
#     'Chase Cantu',
#     'Maverick Gonzales',
#     'Wyatt Browning',
#     'Brenden Walter',
#     'Paula Bullock',
#     'Alisha Hicks',
#     'Genevieve Petty',
#     'Reece Erickson',
#     'Brice Pope',
#     'Maverick Hammond',
#     'Giuliana Morris',
#     'Kaelyn Kelley',
#     'Paisley French',
#     'Cassius Rogers',
#     'Gloria French',
#     'Hugh Richardson',
#     'Braiden Tate',
#     'Sophia Wang',
#     'Cortez Kirby',
#     'Sebastian Wilkinson',
#     'Joanna Shannon',
#     'Miracle Barrera',
#     'Cali Kaiser',
#     'Bridget Leon',
#     'Gillian Hall',
#     'Jade King',
#     'Aydin Powell',
#     'Anthony Paul',
#     'Brittany Rios',
#     'Arely Howe',
#     'Trace Valenzuela',
#     'Aryanna Hicks',
#     'Connor Nixon',
#     'Santiago Vargas',
#     'Kirsten Monroe',
#     'Norah Schultz',
#     'Danika Hudson',
#     'Makena Escobar',
#     'Jayce Navarro',
#     'Thaddeus Strickland',
#     'Michaela Robinson',
#     'Remington Hurley',
#     'Jairo Sanders',
#     'Averie Huber',
#     'Cody Jensen',
#     'Kennedy Wall',
#     'Fiona Huynh',
#     'August Tapia',
#     'Sarah Manning',
#     'Joselyn Allison',
#     'Dayton Barnes',
#     'Santiago Glenn',
#     'Rashad Cuevas',
#     'Bernard Nicholson',
#     'Will Moyer',
#     'Aliza Frazier',
#     'Abram Burch',
#     'Lilly Klein',
#     'Carlee Montes',
#     'Madeleine Patton',
#     'Brady Osborn',
#     'Ruth Monroe',
#     'Celia Horn',
#     'Braylen Cabrera',
#     'Jennifer Tanner',
#     'Kendra Cross',
#     'Olive Sherman',
#     'Aiyana Wolfe',
#     'Charlize Cervantes',
#     'Braydon Esparza',
#     'Kash Osborne',
#     'Maximus Mathews',
#     'Kamora Richardson',
#     'Tripp Sosa',
#     'Kameron Taylor',
#     'Tyler Jackson']

#     def sort_Surname(self):
#         names.Names.sort(key=lambda x: x.split()[-1])
#         return names.Names

# names = Ism_familiya()
# print(names.sort_Surname())



# 2 Usul 
# def sortSurname(namelist):
#     lst = []

#     for i in namelist:
#         lst.append(i.split())
#     namelist = []

#     for j in sorted(lst,key=lambda x:x[-1]):
#         namelist.append(' '.join(j))

#     return namelist

# for i in sortSurname(names.Names):print(i)















class Dori(dict):
    def __init__(self,Nomi,Narxi,Muddati=20_23) -> None:
        self.nomi = Nomi
        self.narxi = Narxi
        self.muddati = Muddati

    def get_info(self):
        return f"Nomi: {self.nomi}\nNarxi: {self.narxi}\nMuddati: {self.muddati}"



class Apteka(Dori):
    def __init__(self, Nomi, Narxi,Location,Dokon_nomi,Muddati=20_23) -> None:
        super().__init__(Nomi, Narxi, Muddati)
        self.location = Location
        self.d_nomi = Dokon_nomi
        self.__kassa = 0
        self.Royxat=[
                ["Izofluran",self.muddati+5,self.narxi+20],
                ["Galotan",self.muddati+2,self.narxi*2],
                ["Sevofluran",self.muddati+4,self.narxi*4],
                ["Ketamin",self.muddati+12,self.narxi*7]]


    def get_info(self):
        return f"""{super().get_info()}\nRoyxat: {self.Royxat}"""

    def dori_sotish(self:str,soni_dorini=0):
        self.__kassa += self.Royxat[soni_dorini][2]


class Person(Apteka):
    def __init__(self,Puli:int) -> None:
        self.puli = Puli

    def sotib_olish(self):
        pass



if __name__ == "__main__":

    dori = Dori("Nimadur",1_000)
    odam = Person(200_000)
    apteka = Apteka("Nimadur",100_000,"Dorixona",'7777')
    apteka.dori_sotish(2)
    apteka.dori_qoshish("Nimadur",2000,12_000)

    # print("\nAssalomu alaykum qaysi dorini sotib olmoqchisiz ?\nRaqam tanlang.\n")
    # j=0
    # while True:
        # print(f"{j+1}-> {i}")
        # j+=1


    # n = input()

    


class Card:
    def __init__(self, nomi, srok,pin):
        self.__balans = 0
        self.__pin = pin
        self.nomi = nomi
        self.srok = srok

    def get_balans(self):
        return f"Balans: {self.__balans} ming so'm"

    def pin(self,pin):
        return 1 if self.__pin == pin else 0
    
    def set_pin(self, old_pin):
        if old_pin == self.__pin:
            self.__pin = int(input("Enter new pin: "))

    def set_minus_balans(self, yechish):
        if yechish > self.__balans:
            return f"Pul yechish uchun kartada mablag' yetarli emas."
        else:
            self.__balans -= yechish
            return f"Muvaffaqiyatli yechildi!"

    def set_plus_balans(self, new_summa):
        self.__balans += new_summa
    
    def info(self):
        return f"""Karta malumotlari:
Nomi: {self.nomi}
Muddati: {self.srok}
Balans: {self.__balans}
Pinkod: {self.__pin}.
"""



if __name__ == "__main__":

    # Enter your own
    kard = Card("Humo","03/24",1111)

    pinkod = int(input("Pin kodni kiriting: "))
    if kard.pin(pinkod):
        while True:
            print("""
[1] -> Balansni ko'rish
[2] -> Balansga pul qo'shish
[3] -> Balansdan pul yechish
[4] -> Pin almashtirish
[5] -> Info
[0] -> EXIT
    """)
            n = int(input())
            if n == 1:
                print(kard.get_balans())
            elif n==2:
                kard.set_plus_balans(int(input("Necha pul qo'shmoqchisiz: ")))
                print(kard.get_balans() + ' ' + 'qo\'shildi')
            elif n==3:
                print(kard.set_minus_balans(int(input("Necha pul yechmoqchisiz: "))))
            elif n==4:
                kard.set_pin(pinkod)
                print("Pinkod muvaffaqiyatli almashtirildi!")
            elif n==5:
                print(kard.info())
            elif n==0:
                exit()
    else: print("Pin kod xato kiritildi!")
