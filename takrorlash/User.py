class User:
    def __init__(self,ID,NAME,SURNAME,SUMMA):
        self.id = ID
        self.name = NAME
        self.surname = SURNAME
        self.summa = SUMMA

    # def User_in_file(self,nimani,nimaga):
    #     if nimani not in nimaga:
    #         self.write_file(nimani)

    def __str__(self):
        return f"{self.id}\n{self.name}\n{self.surname}\n{self.summa}"
    
if __name__=='__main__':
    pass