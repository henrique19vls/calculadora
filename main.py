def add(x,y):
  return x + y 

def sub(x,y):
  return x - y

def mult(x,y):
  return x * y
  
def div(x,y):
  return x / y

print("Selecione uma operaçao")
print("1.Adiçao")
print("2.Subtraçao")
print("3.Multiplicaçao")
print("4.Divisao")

escolha = input("Escolha uma operaçao (1,2,3,4)")

if escolha in ('1','2','3','4'):
  n1 = float(input("Digite um numero"))
  n2 = float(input("Digite outro numero"))

  if escolha == '1':
    print(add(n1,n2))

  if escolha == '2':
    print(sub(n1,n2))
    
  if escolha == '3':
    print(mult(n1,n2))
    
  if escolha == '4':
    if n2 != 0:
      print (div(n1,n2))
    else:
      print("Erro: divisao por 0")
else:
  print("Escolha invalida. por favor, escolha uma operaçao entre 1,2,3,4")
  
  
