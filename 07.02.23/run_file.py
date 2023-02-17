import ttt as t

n = input("Time: ")

lst = []
for i in n.split(":"): lst.append(i)

# a,b,c = int(lst[0]),int(lst[1]),int(lst[2])

variable = t.Hour(int(lst[0]),int(lst[1]),int(lst[2]))

