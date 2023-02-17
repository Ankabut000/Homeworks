import colorama as c
c.init(autoreset=True)
class Moshina:
    def __init__(self,Name,Yili,Bak,Probeg=0) -> None:

        self.variable=Bak
        
        self.__name = Name
        self.__yili = Yili
        self.__probeg = Probeg
        self.__bak = Bak
        self.z = 0

    def zavat_qilish(self):
        if self.z == 0:
            self.z = 1
            print("Moshina zavat qilindi!")
        else:
            print(f"{c.Fore.GREEN}Moshina yoqiq-ku\U0001F923🤦")

    def yurish(self,n_yurish):
        if self.z == 1:
            if n_yurish <= self.__bak*4:
                self.__probeg += n_yurish
                self.__bak -= n_yurish//4
                print(f"Mashina {n_yurish} km yurdi.")
            elif self.__bak == 0:
                print("Benzin yetarli emas!")
            else:
                print(f"""
Benzin yetarli emas,
Benzin {self.__bak*4} km ga yetadi (Yuramizmi)\n[1]-> Ha [0]-> Yo'q """)
                n = int(input())
                if n==1:
                    print(f"Moshina {self.__bak*4} km yurdi")
                    self.__bak = 0
        else:
            print("Moshina hali zavat qilinmagan!")

    def info(self):
        return f"""
Name: {self.__name}
Year: {self.__yili}
Probeg: {self.__probeg}
"""
    def Benzin_quyish(self,n_quyish):
        a = self.__bak + n_quyish
        
        if self.__bak == self.variable:
            print("Bak To'la")
        elif a <= self.variable:
            self.__bak += n_quyish
            print("Benzin quyildi")
        else:
            self.__bak = self.variable
            print("Bak to'ldirildi ottiqchasi Quyilmadi!")

    def ochirish(self):
        if self.z == 1:
            self.z = 0
            print("Moshina o'chirildi!")
        else:
            print(f"{c.Fore.RED}Moshina o'chiq-ku\U0001F923🤦")
            
if __name__=="__main__":
    pass