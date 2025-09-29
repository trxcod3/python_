num1 = float(input("Digite o primeiro numero:\n"))
num2 = float(input("Digite o segundo numero:\n"))
operation = float(input("Digite a operação a ser realizada (+ - * /): \n"))

if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2

elif operation == "*":
  result =  num1 * num2

elif operation == "/":
  if num2 != 0:
    result = num1 / num2
  else: 
    print("Erro na divisao por zero")
    result = 0

else:
  print("Operação inválida")
  result = 0

  print(f"REsultado da operação é: {result:.2f}")