class simpleinterest:
      a = float(input("Enter Principal"))
      b = float(input("Enter Rate"))  
      c = float(input("Enter Time"))
      p = str(a)
      t = str(c)
      r = str(b)
      mul = a * b * c
      res = str(mul)
      cal = mul/100
      fres = str(cal)
      print("Simple Interest (SI)= (PTR)/100")
      print("                 SI = ("+ p + " * "+ t + " * " + r + ") / 1000")
      print("                 SI = (" + res + ") / 100")
      print("                 SI = " + fres)
      print("Therefore, SI = "+ fres)
        
