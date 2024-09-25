#init
age=21
seconds=2*3600+32*60+18
n = "3421"
x = 228
y = 1984
number = 2
#
ivan=["Ivan","Vanya","Ваня","Иван","Ванька","Ванечка","Ивася","Иваха","Ванюха","Ванюра","Ванюра","Иоанн","Ванюра", "Ванюся", "Ванюта"]

def kop():
    print("Курс Основы программирования начался")
    val2p = round(16823*12302/3092)
    h2c = input("Hash\nSum digits of "+str(val2p)+" until there's one digit left: ")
    if int(h2c)==crtHash(str(val2p)):
        print("You're right!")
    else:
        print("too bad.")
        return ""

    if age<0 or age>75:
        print("тычё")
        return ""
    else:
        name=input("Имя? ")
        for i in range(len(ivan)):
            if ivan[i]==name:
                print("Во ВГУИТ не учатся "+"ЛИЦА ВЫПОЛНЯЮЩИЕ ФУНКЦИИ ИНОСТРАННОГО АГЕНТА, И (ИЛИ) РОССИЙСКИЕ ЮРИДИЧЕСКИЕ ЛИЦА, ВЫПОЛНЯЮЩИЕ ФУНКЦИИ ИНОСТРАННОГО АГЕНТА")
                return ""
    if age>15:
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Сначала нужно окончить школу!")
        time2free = 16-age
        print("До конца отсидки: "+str(time2free)+years(time2free))
        return ""

    str2p=""
    for i in range(3,0,-1):
        str2p=str2p+":"+format((seconds%(60**i))//(60**(i-1)),"02")
    str2p=str2p[1:]
    print("second: "+str2p)
    intn = int(n)
    numb=intn
    for i in range(2,6):
        numb+=numb+intn**i
    print("number: "+str(numb))

    global x,y
    tempx = x
    x=y
    y=tempx

    if number%2==1:
        print("Да")
    elif number%2==0:
        print("Нет")
    else:
        print("тычё")

def years(t):
     match t:
          case 1:
               return " год"
          case lets if 1<lets<5:
               return " года"
          case lets if 5<=lets<=16:
               return " лет"
          case _:
               return " тычё"
          
def crtHash(valtt):
    hashval = 99999
    while (len(str(hashval))>1):
        hashval = 0
        for i in range(len(valtt)):
            hashval=hashval+int(valtt[i])
        valtt = str(hashval)
    return(hashval)

kop()