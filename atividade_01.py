import math

# questão 1
print ("Alo mundo")

# questão 2
numero = input("digite um número: ")
print(f"seu numero é {numero}")

# questão 3
primeiro_numero = float(input("digite o primeiro número: "))
segunto_numero = float(input("digite o segunto  número: "))

soma = int(primeiro_numero) + int(segunto_numero)

print(f"a soma dos número é: {soma}")

# questão 4
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunta nota: "))
nota3 = float(input("digite sua terceira nota: "))
nota4 = float(input("digite sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print (f"sua media é: {media}")

# questão 5 
metros = float(input("digite a quantidade de metros: "))

centimetros = metros * 100

print (f"quantidade de metros é {metros} convertida para centimetros é {centimetros} ")

# questão 6
raio = float(input("digite o raio do circulo: "))

area = math.pi * raio ** 2

print(f"A área do círculo com raio {raio} é {area:.2f}.")

# questão 7 
lado = float(input("digite o tamanho do quadrado: "))

area = lado * lado
area_dobro = 2* area

print (f"o dobro do quatrado é {area_dobro}")

# questão 8 
valor1 = float(input("digite o valor que vc ganha por hora: "))
valor2 = float(input("digite o valor de horas trabalhadas no mês: "))

salario = valor1 * valor2

print (f"seu salário por mês é R${salario:.2f}")

# questão 9 
gruas_f = float(input("digite a temperatura em Fahrenheit: "))

gruas_c = 5 * ((gruas_f - 32) / 9)

print (f"A temperatura em graus Celsius é {celsius:.2f}°C")

# questão 10
gruas_celsius = float(input("digite a temperatura em Celsius: "))

gruas_Fahrenheit  = 5 * ((gruas_f - 9/5) + 32)

print (f"A temperatura em graus Fahrenheit é {gruas_Fahrenheit:.2f}°C")
 