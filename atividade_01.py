import funcoes_atv01

def main():
    while True:
        print("\nEscolha a questão que deseja ver:")
        print("1 - Questão 1")
        print("2 - Questão 2")
        print("3 - Questão 3")
        print("4 - Questão 4")
        print("5 - Questão 5")
        print("6 - Questão 6")
        print("7 - Questão 7")
        print("8 - Questão 8")
        print("9 - Questão 9")
        print("10 - Questão 10")
        print("11 - Questão 11")
        print("12 - Questão 12")
        print("13 - Questão 13")
        print("14 - Questão 14")
        print("15 - Questão 15")
        print("16 - Questão 16")
        print("17 - Questão 17")
        print("18 - Questão 18")
        escolha = input("Digite o número da questão que deseja ver (ou 'sair' para encerrar ó script): ")
        print("\n")

        if escolha.lower() == 'sair':
            break

        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > 18:
                print("Opção inválida. Escolha um número de 1 a 18.")
            else:
                getattr(funcoes_atv01, f"questao{escolha}")()
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 18.")

if __name__ == "__main__":
    main()
