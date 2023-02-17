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