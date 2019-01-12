class simple_interest:
	def sol():
		p = int(input("Enter Principal"))
		r = int(input("Enter Rate"))
        t = int(input("Enter Time"))
        print("Simple Interest (SI) = (PTR) / 100")
        print("                  SI  = ("+ p + " * " + t + " * " + r + ") / 100")
        print("                  SI  = (" + P*t*r + ") / 100")
        print("                  SI  = (" + ((p*t*r)/100))
        res = ((p*t*r)/100)
        print("Therefore, Simple Interest (SI) = " + res)