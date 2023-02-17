class Card:
    def __init__(self, nomi,pin=1111):
        self.balans = 100
        self.pin = pin
        self.nomi = nomi
        self.__variable = 0
        self.a = 0

    def sms(self,phone_nuber):
        if self.__variable == 0:
            a = phone_nuber
            self.a = phone_nuber
            self.__variable=1
            print("SMS habarnoma Muvaffaqiyatli ulandi")
            return a
        else:
            print("SMS habarnoma ulangan!")

    def card_info(self):
        return f"""Karta malumotlari:
Nomi: {self.nomi}
Balans: {self.balans}
Pinkod: {self.pin}
Phone number: {self.a}
"""