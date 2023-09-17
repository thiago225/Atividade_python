import math

def questao1():
    print("questão 1 - Faça um Programa que mostre a mensagem 'Alo mundo' na tela: \n")
    print("Alo mundo")

def questao2():
    numero = input("Digite um número: ")
    print(f"Seu número é {numero}")

def questao3():
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    soma = int(primeiro_numero) + int(segundo_numero)
    print(f"A soma dos números é: {soma}")

def questao4():
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    nota4 = float(input("Digite sua quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Sua média é: {media}")

def questao5():
    metros = float(input("Digite a quantidade de metros: "))
    centimetros = metros * 100
    print(f"A quantidade de metros é {metros} convertida para centímetros é {centimetros}")

def questao6():
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * raio ** 2
    print(f"A área do círculo com raio {raio} é {area:.2f}.")

def questao7():
    lado = float(input("Digite o tamanho do quadrado: "))
    area = lado * lado
    area_dobro = 2 * area
    print(f"O dobro do quadrado é {area_dobro}")

def questao8():
    valor1 = float(input("Digite o valor que você ganha por hora: "))
    valor2 = float(input("Digite o valor de horas trabalhadas no mês: "))
    salario = valor1 * valor2
    print(f"Seu salário por mês é R${salario:.2f}")

def questao9():
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = 5 * ((fahrenheit - 32) / 9)
    print(f"A temperatura em graus Celsius é {celsius:.2f}°C")

def questao10():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = 5 * ((celsius * 9/5) + 32)
    print(f"A temperatura em graus Fahrenheit é {fahrenheit:.2f}°F")

def questao11():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite o segundo número: '))
    num_real = float(input('Digite um número real: '))
    resultado1 = (3 * num1) * (num2 / 2)
    resultado2 = (3 * num1) + num_real
    resultado3 = num_real ** 3
    print(f"Produto do dobro do primeiro com metade do segundo: {resultado1}")
    print(f"Soma do triplo do primeiro com o terceiro: {resultado2}")
    print(f"Terceiro elevado ao cubo: {resultado3}")

def questao12():
    altura = float(input("Digite a altura da pessoa (em metros): "))
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para uma pessoa com {altura} metros de altura é {peso_ideal:.2f} kg.")

def questao13():
    altura = float(input("Digite a altura da pessoa (em metros): "))
    sexo = input("Digite o sexo da pessoa (M para homem, F para mulher): ")
    if sexo == "M" or sexo == "m":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "F" or sexo == "f":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido. Use 'M' para homem ou 'F' para mulher.")
        return
    print(f"O peso ideal para uma pessoa com {altura} metros de altura e sexo {sexo.upper()} é {peso_ideal:.2f} kg.")

def questao14():
    peso_peixes = float(input("Digite o peso de peixes (em quilos): "))
    limite_peso = 50.0
    if peso_peixes > limite_peso:
        excesso = peso_peixes - limite_peso
        multa = excesso * 4.0
        print(f"Peso excedente: {excesso:.2f} kg")
        print(f"Valor da multa a ser pago: R${multa:.2f}")
    else:
        print("O peso de peixes está dentro do limite permitido. Não há multa a ser paga.")

def questao15():
    valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    salario_bruto = valor_por_hora * horas_trabalhadas
    imposto_renda = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - imposto_renda - inss - sindicato
    print(f"+ Salário Bruto: R${salario_bruto:.2f}")
    print(f"- IR (11%): R${imposto_renda:.2f}")
    print(f"- INSS (8%): R${inss:.2f}")
    print(f"- Sindicato (5%): R${sindicato:.2f}")
    print(f"= Salário Líquido: R${salario_liquido:.2f}")

def questao16():
    area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))
    litros_de_tinta = area_a_ser_pintada / 3
    latas_de_tinta = litros_de_tinta / 18
    latas_de_tinta = math.ceil(latas_de_tinta)
    preco_por_lata = 80.00
    preco_total = latas_de_tinta * preco_por_lata
    print(f"Você precisará de {latas_de_tinta} latas de tinta.")
    print(f"O preço total será de R${preco_total:.2f}")

def questao17():
    area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))
    cobertura_por_litro = 6
    litros_de_tinta = area_a_ser_pintada / cobertura_por_litro
    litros_de_tinta_com_folga = litros_de_tinta * 1.10
    litros_por_lata = 18
    latas_de_tinta = int(litros_de_tinta_com_folga / litros_por_lata)
    litros_por_galao = 3.6
    galoes_de_tinta = int(litros_de_tinta_com_folga / litros_por_galao)
    preco_por_lata = 80.00
    preco_total_latas = latas_de_tinta * preco_por_lata
    preco_por_galao = 25.00
    preco_total_galoes = galoes_de_tinta * preco_por_galao
    litros_restantes = litros_de_tinta_com_folga - (galoes_de_tinta * litros_por_galao)
    latas_adicionais = math.ceil(litros_restantes / litros_por_lata)
    preco_total_mistura = (latas_de_tinta + latas_adicionais) * preco_por_lata
    print(f"Quantidade de tinta a ser comprada:")
    print(f"Comprar apenas latas de 18 litros: {latas_de_tinta} latas")
    print(f"Comprar apenas galões de 3,6 litros: {galoes_de_tinta} galões")
    print(f"Misturar latas e galões: {latas_de_tinta + latas_adicionais} latas e {galoes_de_tinta} galões")
    print(f"Preço total:")
    print(f"Comprar apenas latas de 18 litros: R${preco_total_latas:.2f}")
    print(f"Comprar apenas galões de 3,6 litros: R${preco_total_galoes:.2f}")
    print(f"Misturar latas e galões: R${preco_total_mistura:.2f}")

def questao18():
    tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
    velocidade_internet_mbps = float(input("Digite a velocidade da sua conexão de Internet (em Mbps): "))
    tempo_download_minutos = (tamanho_arquivo_mb / velocidade_internet_mbps) / 60
    print(f"O tempo aproximado de download do arquivo será de {tempo_download_minutos:.2f} minutos.")