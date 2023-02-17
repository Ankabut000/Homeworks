from Bankomat import ATM
from Card import Card
from Person import Odam
import colorama as f

f.init(autoreset=True)

print(f"\n{f.Back.GREEN}Assalomu alaykum Bankomatga hush kelibsiz")
print(f"{f.Fore.RED}Eslatma: Sizda 3 tadan ortiq imkoniyatingiz yo'q aks holda karta bloklanadi!!!")

parol = 1111
count = 0
n = int(input("Parolni kiriting: "))
if n != parol:
    for i in range(1,3):
        print(f"{i+1} -> Imkoniyatingiz: ")
        n = int(input())
        if n == parol:
            break
        count+=1    
if count==2:
    print('Karta bloklandi')
    exit()

atm = ATM("Nimadur")
crd = Card("Humo",pin=parol)
od = Odam("Toshmat",1_000_000,crd,120_000,94_044_50_02)

while True:
    print(f"""
[1]-> Kartadan pul yechish 
[2]-> Kartaga pul qo'shish
[3]-> Parol almashtirish
[4]-> SMS habarnoma ulash
[5]-> Karta ma'lumotlari
[6]-> Balansni tekshirish
[0]-> Exit
""")

    n = int(input())
    if n==1:
        atm.naxt_pul_yechish(od,int(input("Necha pul yechmoqchisiz: ")))
    elif n==2:
        atm.naxt_pul_qoshish(od,int(input("Necha pul qo'shmoqchisiz: ")))
    elif n==3:
        atm.set_pin(od,parol,int(input("Yangi parolni kiriting: ")))
    elif n==4:
        atm.sms_habarnoma(od,int(input("Telefon raqamingizni kiriting: ")))
    elif n==5:
        atm.card_info(crd)
    elif n==6:
        atm.balans_tekshir(od)
    elif n==0:
        print("Bankomatdan foydalanganingiz uchun tashakkur!")
        exit()