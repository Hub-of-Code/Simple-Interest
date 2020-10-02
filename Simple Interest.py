class simpleinterest:
      a = float(input("Enter Principal(P): "))             # asking for principal
      b = float(input("Enter Rate(R): "))                  # asking for rate  
      c = float(input("Enter Time(T): "))                  # asking for time
      p = str(a)
      t = str(c)
      r = str(b)
      mul = a * b * c
      res = str(mul)
      cal = mul/100
      fres = str(cal)
      print("Simple Interest (SI)= (P*T*R)/100")
      print("                 SI = ("+ p + " * "+ t + " * " + r + ") / 1000")
      print("                 SI = (" + res + ") / 100")
      print("                 SI = " + fres)
      print("Therefore, SI = "+ fres)
        
