from Card import Card
from Person import Odam
class ATM:
    # Enter your own 
    def __init__(self,Nomi,Limit = 5_000_000) -> None:
        self.nomi = Nomi
        self.limit = Limit

    def naxt_pul_qoshish(self,karta:Odam,summa_miqdori):
        if  self.limit > summa_miqdori:
                karta.balans += summa_miqdori
                karta.karmon -= summa_miqdori
                print( f"Muvaffaqiyatli qo'shildi!")
                print(f"Balans: {karta.balans}")

        else:print(f"Limit: {self.limit}\nLimitdan oshiq pul qo'shib bo'lmaydi.")

    def card_info(self,karta:Odam):
        print(karta.card_info())

    def set_pin(self,karta:Odam,old_pin,new_pin):
        if old_pin == karta.card.pin:
            karta.card.pin = new_pin
            print("Parol muvaffaqiyatli yangilandi!")

    def sms_habarnoma(self,karta:Odam,number):
        karta.card.sms(number)

    def balans_tekshir(self,karta:Odam):
        print(f"Balans: {karta.balans} ming so'm")

    def naxt_pul_yechish(self,karta:Odam,summa_miqdori:int):
        if  self.limit > summa_miqdori:
            if karta.balans < summa_miqdori:
                print( f"Pul yechish uchun, kartada mablag' yetarli emas.")
                print(karta.balans)
            else:
                karta.balans -= summa_miqdori
                karta.karmon += summa_miqdori
                print( f"Muvaffaqiyatli yechildi!")
                print(karta.balans)
        else:print(f"Limit: {self.limit}\nLimitdan oshiq pul yechib bo'lmaydi.")