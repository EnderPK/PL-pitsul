def fun():        
        for x in (1,0):
            k = int(input())
            if k == 0 :
                return
            if x:
                print(' *\t',k)
        fun()  
      
fun()