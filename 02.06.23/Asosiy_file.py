import Library_file as f
moshina = f.Moshina("KIA",2022,50)

while True:
    print(f"""
[1]-> Zavat qilish
[2]-> Yurish
[3]-> Benzin quyish
[4]-> Benzin qancha
[5]-> Info
[6]-> O'chirish
[0]-> EXIT
""")
    n = int(input())
    if n==1:
        moshina.zavat_qilish()
    elif n==2:
        moshina.yurish(int(input("Necha km yurmoqchisiz: ")))
    elif n==3:
        moshina.Benzin_quyish(int(input("Necha litr benzin quymoqchisiz: ")))
    elif n==4:
        print(f"{moshina._Moshina__bak} litr benzin bor")
    elif n==5:
        print(moshina.info())
    elif n==6:
        moshina.ochirish()
    elif n==0:
        print("Dastur Tugatildi")
        exit()