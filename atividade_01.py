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