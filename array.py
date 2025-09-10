from random import randint

pontuacao = 0

while (True):
    bot = randint(1, 10)
    acerto = int(input("Digite um número de 1 a 10 e veja se voce ganhou \n"))

    if (acerto == bot):
        print("Voce acertou o Número!! \n")
        pontuacao = pontuacao + 1
        
    else:
        print(f"Voce errou, estava pensando em {bot} :( \n")
    
    r = input("quer jogar novamente? \n")
    if (r == 'nao'):
        break

    print (f"voce acertou o número {pontuacao} vezes \n")
