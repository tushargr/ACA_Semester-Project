dict = {}
dict [1]=' '
dict [2]=' '
dict [3]=' '
dict [4]=' '
dict [5]=' '
dict [6]=' '
dict [7]=' '
dict [8]=' '
dict [9]=' '

def printgame():
    print(dict[1]+" | "+dict[2]+" | "+dict[3]+'\n')
    print(dict[4] + " | " + dict[5] + " | " + dict[6] + '\n')
    print(dict[7] + " | " + dict[8] + " | " + dict[9])

def step1():
    if dict[1]=='o' and dict[2]=='o' and dict[3]==' ':
        dict[3]='o'
        return 1
    elif dict[1]=='o' and dict[3]=='o' and dict[2]==' ':
        dict[2]='o'
        return 1
    elif dict[2]=='o' and dict[3]=='o' and dict[1]==' ':
        dict[1]='o'
        return 1
    elif dict[4]=='o' and dict[5]=='o' and dict[6]==' ':
        dict[6]='o'
        return 1
    elif dict[4]=='o' and dict[6]=='o' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='o' and dict[6]=='o' and dict[4]==' ':
        dict[4]='o'
        return 1
    elif dict[7]=='o' and dict[8]=='o' and dict[9]==' ':
        dict[9]='o'
        return 1
    elif dict[7]=='o' and dict[9]=='o' and dict[8]==' ':
        dict[8]='o'
        return 1
    elif dict[8]=='o' and dict[9]=='o' and dict[7]==' ':
        dict[7]='o'
        return 1
    elif dict[3]=='o' and dict[5]=='o' and dict[7]==' ':
        dict[7]='o'
        return 1
    elif dict[3]=='o' and dict[7]=='o' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='o' and dict[7]=='o' and dict[3]==' ':
        dict[3]='o'
        return 1
    elif dict[1]=='o' and dict[5]=='o' and dict[9]==' ':
        dict[9]='o'
        return 1
    elif dict[1]=='o' and dict[9]=='o' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='o' and dict[9]=='o' and dict[1]==' ':
        dict[1]='o'
        return 1
    elif dict[1]=='o' and dict[4]=='o' and dict[7]==' ':
        dict[7]='o'
        return 1
    elif dict[1]=='o' and dict[7]=='o' and dict[4]==' ':
        dict[4]='o'
        return 1
    elif dict[4]=='o' and dict[7]=='o' and dict[1]==' ':
        dict[1]='o'
        return 1
    elif dict[2]=='o' and dict[5]=='o' and dict[8]==' ':
        dict[8]='o'
        return 1
    elif dict[2]=='o' and dict[8]=='o' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='o' and dict[8]=='o' and dict[2]==' ':
        dict[2]='o'
        return 1
    elif dict[3]=='o' and dict[6]=='o' and dict[9]==' ':
        dict[9]='o'
        return 1
    elif dict[3]=='o' and dict[9]=='o' and dict[6]==' ':
        dict[6]='o'
        return 1
    elif dict[6]=='o' and dict[9]=='o' and dict[3]==' ':
        dict[3]='o'
        return 1
    else:
        return 0

def step2():
    if dict[1]=='x' and dict[2]=='x' and dict[3]==' ':
        dict[3]='o'
        return 1
    elif dict[1]=='x' and dict[3]=='x' and dict[2]==' ':
        dict[2]='o'
        return 1
    elif dict[2]=='x' and dict[3]=='x' and dict[1]==' ':
        dict[1]='o'
        return 1
    elif dict[4]=='x' and dict[5]=='x' and dict[6]==' ':
        dict[6]='o'
        return 1
    elif dict[4]=='x' and dict[6]=='x' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='x' and dict[6]=='x' and dict[4]==' ':
        dict[4]='o'
        return 1
    elif dict[7]=='x' and dict[8]=='x' and dict[9]==' ':
        dict[9]='o'
        return 1
    elif dict[7]=='x' and dict[9]=='x' and dict[8]==' ':
        dict[8]='o'
        return 1
    elif dict[8]=='x' and dict[9]=='x' and dict[7]==' ':
        dict[7]='o'
        return 1
    elif dict[3]=='x' and dict[5]=='x' and dict[7]==' ':
        dict[7]='o'
        return 1
    elif dict[3]=='x' and dict[7]=='x' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='x' and dict[7]=='x' and dict[3]==' ':
        dict[3]='o'
        return 1
    elif dict[1]=='x' and dict[5]=='x' and dict[9]==' ':
        dict[9]='o'
        return 1
    elif dict[1]=='x' and dict[9]=='x' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='x' and dict[9]=='x' and dict[1]==' ':
        dict[1]='o'
        return 1
    elif dict[1]=='x' and dict[4]=='x' and dict[7]==' ':
        dict[7]='o'
        return 1
    elif dict[1]=='x' and dict[7]=='x' and dict[4]==' ':
        dict[4]='o'
        return 1
    elif dict[4]=='x' and dict[7]=='x' and dict[1]==' ':
        dict[1]='o'
        return 1
    elif dict[2]=='x' and dict[5]=='x' and dict[8]==' ':
        dict[8]='o'
        return 1
    elif dict[2]=='x' and dict[8]=='x' and dict[5]==' ':
        dict[5]='o'
        return 1
    elif dict[5]=='x' and dict[8]=='x' and dict[2]==' ':
        dict[2]='o'
        return 1
    elif dict[3]=='x' and dict[6]=='x' and dict[9]==' ':
        dict[9]='o'
        return 1
    elif dict[3]=='x' and dict[9]=='x' and dict[6]==' ':
        dict[6]='o'
        return 1
    elif dict[6]=='x' and dict[9]=='x' and dict[3]==' ':
        dict[3]='o'
        return 1
    else:
        return 0

def step3():
    if dict[1]==' ':
        dict[1]='o'
        return 1
    elif dict[3]==' ':
        dict[3]='o'
        return 1
    elif dict[7]==' ':
        dict[7]='o'
        return 1
    elif dict[9]==' ':
        dict[9]='o'
        return 1
    else:
        return 0

def step4():
    if dict[5]==' ':
        dict[5]='o'
        return 1
    else:
        return 0

def step5():
    if dict[2]==' ':
        dict[2]='o'
        return 1
    elif dict[4]==' ':
        dict[4]='o'
        return 1
    elif dict[6]==' ':
        dict[6]='o'
        return 1
    elif dict[8]==' ':
        dict[8]='o'
        return 1
    else:
        return 0

def userwin():
    if dict[1]=='x' and dict[2]=='x' and dict[3]=='x':
        return 1
    elif dict[4]=='x' and dict[5]=='x' and dict[6]=='x':
        return 1
    elif dict[7]=='x' and dict[8]=='x' and dict[9]=='x':
        return 1
    elif dict[1]=='x' and dict[4]=='x' and dict[7]=='x':
        return 1
    elif dict[2]=='x' and dict[5]=='x' and dict[8]=='x':
        return 1
    elif dict[3]=='x' and dict[6]=='x' and dict[9]=='x':
        return 1
    elif dict[1]=='x' and dict[5]=='x' and dict[9]=='x':
        return 1
    elif dict[3]=='x' and dict[5]=='x' and dict[7]=='x':
        return 1
    else:
        return 0
count = 0
while count < 9:
    x=int(input("make ur move:"))
    dict[x]='x'
    if userwin()==1:
        printgame()
        print("u win")
        break

    count += 1
    printgame()
    if step1()==1:
        printgame()
        print('\n')
        print("u lost")
        break
    elif step2()==1:
        printgame()
        count += 1
        continue
    elif step3() == 1:
        printgame()
        count += 1
        continue
    elif step4()==1:
        printgame()
        count += 1
        continue
    elif step5()==1:
        printgame()
        count += 1
        continue
if count==9:
    print("tie")
