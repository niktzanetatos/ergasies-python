import random
pl1=0
pl2=0
dr=0
for n in range (0,100):
 xartia = []
 figures = ["J", "Q", "K"]
 xarti = [i for i in range(1, 11)] + figures
 color = ["H", "S", "C", "D"]
 for i in xarti:
    for j in color:
        xartia.append([i,j])
 random.shuffle(xartia)
 player1=[]
 sum1=0
 while sum1<16:
    sum1=0
    player1.append(xartia.pop())

    for card in player1:
        if card[0] in figures:
            sum1=sum1+10
        else:
            sum1=sum1+card[0]
    print(sum1)
 if sum1>21:
    print("P2 wins!")
    pl2+=1
 else:


    print("P2 joins the game")
    player2=[]
    sum2=0
    while sum2<16:
        sum2=0
        player2.append(xartia.pop())

        for card in player2:
            if card[0] in figures:
                sum2=sum2+10
            else:
                sum2=sum2+card[0]
        print(sum2)
    if sum2>21:
        sum2=0
    if sum1>sum2:
        print("P1 wins!")
        pl1+=1
    elif sum2>sum1:
        print("P2 wins!")
        pl2+=1
    else:
        print("draw!")
        dr+=1

print("Ο 1 ΚΕΡΔΙΣΕ",pl1,"ΦΟΡΕΣ")
print("Ο 2 ΚΕΡΔΙΣΕ",pl2,"ΦΟΡΕΣ")
print("ΤΟ ΠΑΙΧΝΙΔΙ ΗΡΘΕ",dr, "ΦΟΡΕΣ ΙΣΟΠΑΛΙΑ")

print("ΑΡΧΗ 2ΟΥ ΣΚΕΛΟΥΣ  ΤΗΣ ΑΣΚΗΣΗΣ")



pl1=0
pl2=0
dr=0
for n in range (0,100):
 xartia1 = []
 xartia2 = []
 xartia = []
 figures = ["J", "Q", "K"]
 xarti1 = [10] + figures
 xarti2 = [k for k in range(1,10)]
 color = ["H", "S","C", "D"]
 for i in xarti1:
    for j in color:
        xartia1.append([i,j])
 random.shuffle(xartia1)
 for k in xarti2:
     for j in color:
         xartia2.append([k,j])
 random.shuffle(xartia2)
 for i in xartia1:
     xartia.append(i)

 for j in xartia2:
     xartia.append(j)

 random.shuffle(xartia)
 print(xartia)
 print(xartia1)
 print(xartia2)
 player1=[]
 sum1=0
 check=0
 while sum1<16:
    sum1=0
    if check==1:
        y=xartia.pop()
        player1.append(y)
        if y in xartia2:
            xartia2.remove(y)
        elif y in xartia1:
            xartia1.remove(y)

    else:
        y=xartia1.pop()
        print(y)
        indexy=xartia.index(y)
        xartia.pop(indexy)

        player1.append(y)
        check=1

    for card in player1:
        if card[0] in figures:
            sum1=sum1+10
        else:
            sum1=sum1+card[0]
    print(sum1)
 if sum1>21:
    print("P2 wins!")
    pl2+=1
 else:


    print("P2 joins the game")
    player2=[]
    sum2=0
    check=0
    while sum2<16:
        sum2=0
        if check==1:
            k=xartia.pop()
            player2.append(k)
        if k in xartia1:
            xartia1.remove(k)
        elif k in xartia2:
            xartia2.remove(k)
        else:
            l=xartia2.pop()
            print(l)
            print(pl1)
            print(pl2)
            print(dr)
            player2.append(l)
            check=1



        for card in player2:
            if card[0] in figures:
                sum2=sum2+10
            else:
                sum2=sum2+card[0]
        print(sum2)
    if sum2>21:
        sum2=0
    if sum1>sum2:
        print("P1 wins!")
        pl1+=1
    elif sum2>sum1:
        print("P2 wins!")
        pl2+=1
    else:
        print("draw!")
        dr+=1

print("Ο 1 ΚΕΡΔΙΣΕ",pl1,"ΦΟΡΕΣ")
print("Ο 2 ΚΕΡΔΙΣΕ",pl2,"ΦΟΡΕΣ")
print("ΤΟ ΠΑΙΧΝΙΔΙ ΗΡΘΕ",dr, "ΦΟΡΕΣ ΙΣΟΠΑΛΙΑ")
