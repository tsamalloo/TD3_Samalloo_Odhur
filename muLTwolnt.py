def mul_num(a,b):
  mul=a*b;
  return mul;

def main():
    import sys
    print(sys.argv)
    i =(len(sys.argv)-1)
    print("le nombre d'arguments : ",i)

  if(i==0):
    n1=int(input("inserez le premier argument : "))
    n2=int(input("inserez le deuxieme argument : "))
    x=int(n1)
    y=int(n2)
    print(mul_num(x,y))
  elif(i==1):
       n1=int(input("inserez le premier argument : "))
       x=int(sys.argv[1])
       y=int(n1)
       print(mul_num(x,y))
  elif(i==2):
        x=int(sys.argv[1])
        y=int(sys.arg[2])
        print(mul_num(x,y))
  else:
       print("erreur:veuillez inserer que deux arguments")

main()

