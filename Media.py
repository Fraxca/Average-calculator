#sistema simples de notas objetivo
def calcular_media_bimestral():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    media = (n1 + n2 + n3 + n4) / 4
    if media >= 5:
        print("Aprovado! Sua média é:", media)
    else:
        print("Reprovado! Sua média é:", media)
    return media

#media anual
def media_anual(m1, m2, m3, m4):
    m1 = float(input("Digite a média do primeiro bimestre: "))
    m2 = float(input("Digite a média do segundo bimestre: "))
    m3 = float(input("Digite a média do terceiro bimestre: "))
    m4 = float(input("Digite a média do quarto bimestre: "))

    media = ((m1 *1) + (m2 * 2) + (m3 * 3) + (m4 * 4)) / 10
    if media >= 5:
        print("Aprovado! Sua média anual é:", media)
    else:
        print("Reprovado! Sua média anual é:", media)
    return media

#quanto falta para passar
def quanto_falta_para_passar(media):
    if media >= 5:
        print("Parabéns! Você já passou!")
    else:
        falta = 5 - media
        print("Faltam", falta, "pontos para você passar.")

#chamada das funções
while True:
    print("Calculadora de Média Bimestral")
    print("-----------------------------")
    print("Deseja calcular a média bimestral ou anual?")
    print("1 - Média Bimestral")
    print("2 - Média Anual")
    print("3 - Quanto falta para passar?")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        calcular_media_bimestral()
    elif opcao == 2:
        media_anual(0, 0, 0, 0)
    elif opcao == 3:
        media = calcular_media_bimestral()  
        quanto_falta_para_passar(media)
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
