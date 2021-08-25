import tkinter
import random
master_list = open("efflist.txt", "r")
line_list = [line.rstrip('\n') for line in master_list]
zoop = []
pw_dict={}
for x in line_list:
    a = x.split("\t")
    zoop.append(a)
for i in zoop:
    pw_dict[i[0]] = i[1]
nor = int(input("How Many Words? "))
global rolls
rolls = []
def indv_die():
    x = 1
    roll = []
    while x <= 5:
        a = random.randint(1,6)
        roll.append(str(a))
        x += 1
    r = ""
    r = r.join(roll)
    return(r)


def dice_rolls(nor):
    x = 1
    while x <= nor:
        a = indv_die()
        rolls.append(a)
        x += 1
    return(rolls)


dice_rolls(nor)
pw = ""
for i in rolls:
    word = pw_dict[i]
    pw = pw+word
print(pw)


