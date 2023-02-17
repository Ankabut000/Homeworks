from User import User as User
f = open("Users_data.txt","w+")

lst = []

# for i in range(int(input(">>> "))):
print("Assalomu alaykum Malumotlaringizni kiriting:")
id = int(input("ID: "))
name = input("Name: ")
surname = input("Surname: ")
mablag = int(input("Mablag': "))
obj = User(id,name,surname,mablag)
lst.append(obj)
print(obj)
print(type(obj))

f.close()