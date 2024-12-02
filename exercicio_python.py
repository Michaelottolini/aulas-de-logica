#Calculadora
numero1 = int(input("Digite um numero para ser calculado "))
operador = input("Digite * para multiplicação, + para adição - para subtração ou / para divisão ")
numero2 = int(input("Digite o segundo numero para ser calculado "))

if operador == "*":
 print ("Resultado da multipicaçao", numero1,"*",numero2, "é =",numero1*numero2)
elif operador == "+":
  print ("Resultado da soma", numero1,"+",numero2, "é =",numero1+numero2)
elif operador == "-":
  print ("Resultado da subtração", numero1,"-",numero2,"é = ",numero1-numero2)
elif operador == "/":
  print ("Resultado da Divisão", numero1,"-",numero2,"é = ",numero1/numero2)
else :
 print ("Operador invalido")
