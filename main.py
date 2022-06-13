import math

el = list(map(int,input().strip().split()))

if len(el)<=1 or len(el)>=3:
  print("Podaj dwie liczby")
elif len(el)==2:
  def symbol_newtona(el):
    return math.factorial(el[0])/(math.factorial(el[1])*math.factorial(el[0]-el[1]))
  if el[0]>el[1] and el[1]>0:
    print(math.ceil(symbol_newtona(el)))
  elif el[0]==el[1] or el[1]==0:
    print('1')
  else: 
    print('N (pierwsza liczba) musi być większe od k (drugiej liczby)') 