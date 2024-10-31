import math

def func4(a,b,l,n):
    return a+l+2*(n-1)*(b+a)

def chocoeasy(n,m,k):
    for xc in range(1,n):
        if k==xc*m: return True
    for yc in range(1,m):
        if k==n*yc: return True
    return False

def pairscount(l4iw):
    cntr=[]
    for i1 in range(0,len(l4iw)):
        pnc=-1
        for i2 in range(0,len(l4iw)):
            if l4iw[i1]==l4iw[i2]:
                pnc=pnc+1
        cntr.append(pnc)
    return cntr

print("Please note that this program is for internal use only\nI'm beliving that anyone who will use this program sane enough to not put latters in number fields\nThis program DOES NOT have any safeguards against stupid users\nFloat is supported by default")
afe=True
while afe:
    match input("\nSelect a program: A, B, C, D, E, F, G, H, I, laba2 or exit\nthis choice is case-sensetive\n"):
        case "A":
            print("Sum of numbers")
            print(float(input("1: "))+float(input("2: "))+float(input("3: ")))
        case "B":
            print("Right triangle calculator")
            if input("Reverse mode? [y/.*]")=="y":
                print("Unknown short side is "+str(math.sqrt((float(input("Hypotenuse length (float supported): "))**2)-(float(input("Cathetus length (float supported): "))**2))))
            else:
                print("Unknown long side is "+str(math.sqrt((float(input("Cathetus II length (float supported): "))**2)+(float(input("Cathetus I length (float supported): "))**2))))
        case "C":
            t = int(input("Time in minutes (float isn't supported): "))
            print("{hh:02d}:{mm:02d}".format(hh=t%1440//60,mm=t%1440%60))
        case "D":
            print("Shoe calculator. Float supported, except for n")
            print("Cord length: "+str(func4(float(input("a: ")),float(input("b: ")),float(input("l: ")),int(input("n: ")))))
        case "E": #H, I
            print("Default python's sort")
            listovals=[]
            print('Type any number of numbers separated via newline than type "done"')
            while True:
                recivedstr=input()
                if recivedstr=="done": break
                listovals.append(float(recivedstr))
            listovals.sort(reverse=False)
            if input("Display all numbers? [y/.*]")=="y":
                print(listovals)
            else:
                print(listovals[0])
        case "F":
            print("Chess board... program. Float isn't supported")
            print(((int(input("X1: ")))+int(input("Y1: ")))%2==(int(input("X2: "))+int(input("Y2: ")))%2)
        case "G":
            yea = int(input("Year (float isn't supported)? "))
            print(yea%400==0 or((yea%4==0)and(yea%100!=0)))
        case "H":
            print("Pairs counter")
            listovals=[]
            print('Type any number of numbers separated via newline than type "done"')
            while True:
                recivedstr=input()
                if recivedstr=="done": break
                listovals.append(float(recivedstr))
            ansff=pairscount(listovals)
            print("There's "+str(len(ansff)-ansff.count(0))+" numbers that have at least one pair")
        case "I":
            print("Choco script. Float isn't supported")
            print(chocoeasy(int(input("n: ")),int(input("m: ")),int(input("k: "))))
        case "laba2": #15
            if input("Would you like to use custom arguments? [y/.*]")=="y":
                x=float(input("x: "))
                y=float(input("y: "))
                z=float(input("z: "))
            else:
                x=2.444
                y=0.00869
                z=-130
            s=((x**(y+1)+math.exp(y-1))/(1+x*abs(y-math.tan(z))))*(1+abs(y-x))+((abs(y-x)**2)/2)-((abs(y-x)**3)/3)
            print(s)
        case "exit":
            afe=False
        case _:
            print("There's no such program. Try copying symbol associated with program from above")
