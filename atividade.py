#Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime. As perguntas são:
 "Esteve no local do crime?"
 "Mora perto da vítima?"
 “Tinha dívidas com a vítima?"
 "Já trabalhou com a vítima?“
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como
"Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def classificar_participacao(respostas):
    # Contabiliza o número de respostas "sim"
    respostas_positivas = sum(respostas)

    # Classificação com base no número de respostas "sim"
    if respostas_positivas == 2:
        return "Suspeita"
    elif 3 <= respostas_positivas <= 4:
        return "Cúmplice"
    elif respostas_positivas == 5:
        return "Assassino"
    else:
        return "Inocente"
def main():
    # Perguntas a serem feitas
    perguntas = [
        "Telefonou para a vítima? (s/n) ",
        "Esteve no local do crime? (s/n) ",
        "Mora perto da vítima? (s/n) ",
        "Tinha dívidas com a vítima? (s/n) ",
        "Já trabalhou com a vítima? (s/n) "
    ]
    respostas = []

    # Faz as perguntas e armazena as respostas (True para 's' e False para 'n')
    for pergunta in perguntas:
        resposta = input(pergunta).strip().lower()
        if resposta == 's':
            respostas.append(True)
        elif resposta == 'n':
            respostas.append(False)
        else:
            print("Resposta inválida, por favor responda com 's' ou 'n'.")
            return  # Interrompe o programa em caso de resposta inválida

    # Classifica a pessoa com base nas respostas
    classificacao = classificar_participacao(respostas)
# Exibe o resultado
    print(f"\nClassificação: {classificacao}")

# Executa o programa
if __name__ == "__main__":
    main()

