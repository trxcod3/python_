num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Aritiméticos

sum = num1 + num2
sub =  num1 -  num2
div =  num1 / num2
mult =  num1 *  num2
mod =  num1 % num2
exp =  num1 ** num2

print(f"Potência do número {num1} por {num2} é : {exp}")
print(f"O resto da divisao  do número {num1} por {num2} é : {mod}")

# Comparação

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os números {num1} e {num2} sao igual? {equal}")
print(f"O número {num1} é maior ou igual a {num1}? {bigger_equal}")