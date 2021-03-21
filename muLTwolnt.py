def mul_num(a,b):
  mul=a*b;
  return mul;

def main():
    import sys
    print(sys.argv)
    i =(len(sys.argv)-1)
    print("le nombre d'arguments : ",i)

  if(i==2):
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    print(mul_num(x,y))
  else:
       print("erreur:veuillez inserer que deux arguments")

main()

