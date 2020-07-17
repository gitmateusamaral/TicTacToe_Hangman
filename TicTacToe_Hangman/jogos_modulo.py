# -*- coding: utf-8 -*-
"""
Aluno: Mateus Amaral do Nascimento(181101036) 
"""
import random
import itertools

def menu():
    escolha_jogo = int(input("Deseja jogar o Jogo da velha(1), o Jogo da forca(2), procurar o resultado dos jogadores(3) ou sair(4): "))
    log_jogo1 = "log_jogo1.txt"  
    log_jogo2 = "log_jogo2.txt"
    
    if escolha_jogo == 1:
        jogo_da_velha(log_jogo1)
    elif escolha_jogo == 2:
        jogo_da_forca(log_jogo2)
    elif escolha_jogo == 3:
        procurar_jogadores(log_jogo1, log_jogo2)
    elif escolha_jogo == 4:        
        print("Programa finalizado...")
    else:
        print("Comando invalido")


def procurar_jogadores(log_jogo1, log_jogo2):
    proc_jogador = str(input("Qual jogador voce está procurando? ")).lower().strip()
    
    with open(log_jogo1) as log_jogo1_aberto:
        linhas_log_jogo1 = log_jogo1_aberto.readlines()
        
    with open(log_jogo2) as log_jogo2_aberto:
        linhas_log_jogo2 = log_jogo2_aberto.readlines()  
    
    for linha in linhas_log_jogo1 + linhas_log_jogo2:
        linha = linha.replace('\n', '')
        if ' ' in linha and linha[:linha.index(' ')] == proc_jogador:
            print(linha)


#Jogo da Velha
def jogo_da_velha(log_jogo1):
    print("Bem vindo ao jogo da velha!!!") 
     
    nome_jogador1 = str(input("Digite o nome do jogador 1:")).lower().strip()
    nome_jogador2 = str(input("Digite o nome do jogador 2:")).lower().strip()
    primeiro_jogador = random.randint(1, 2)
    lista_movimentos = ["a1","b1","c1","a2","b2","c2","a3","b3","c3"]
    posicao_grafico = [42,48,54,99,105,111,156,162,168]
    vez_x = False
    movimento_x = []
    movimento_o = []
    fim_partida = False
    jogo_grafico = """
   a     b     c  
      │     │     
1     │     │     
 _____│_____│_____
      │     │     
2     │     │     
 _____│_____│_____
      │     │     
3     │     │     
      │     │     
"""
    
    if primeiro_jogador == 1:
        print(f"{nome_jogador1} Começa")
        vez_x = True
    else:
        print(f"{nome_jogador2} Começa")
        vez_x = False
    
    while fim_partida == False:
        print(jogo_grafico)
        
        if len(lista_movimentos) <= 0:
            print(jogo_grafico)
            print("\nO jogo deu velha!!!")
            fim_partida = True
            menu()
        
        movimento = str(input("Qual posição você quer jogar? "))
        
        if vez_x == True and movimento in lista_movimentos:
            jogador = 'x'
            vez_x = False
            movimento_x.append(movimento)
            posicao_grafico, lista_movimentos, jogo_grafico = executar_movimento(posicao_grafico, lista_movimentos, movimento, jogador, jogo_grafico)
        elif vez_x == False and movimento in lista_movimentos:
            jogador = 'o'
            vez_x = True
            movimento_o.append(movimento)
            posicao_grafico, lista_movimentos, jogo_grafico = executar_movimento(posicao_grafico, lista_movimentos, movimento, jogador, jogo_grafico)
        else: 
            print("Movimento inválido")
        
        
        fim_partida = checar_vitoria(movimento_x,nome_jogador1, jogo_grafico, log_jogo1, fim_partida)
        fim_partida = checar_vitoria(movimento_o,nome_jogador2, jogo_grafico, log_jogo1, fim_partida)


def checar_vitoria(movimentos, nome_jogador, jogo_grafico, log_jogo1, fim_partida):
    for a,b,c in itertools.combinations(movimentos, 3):
        if a[0]==b[0]==c[0] or a[1]==b[1]==c[1] or (a[0]!=b[0] and a[0]!=c[0] and b[0]!=c[0] and a[1]!=b[1] and a[1]!=c[1] and b[1]!=c[1] and (a=="b2" or b=="b2" or c=="b2")):
            print(f"Jogada vencedora:" + a,b,c)
            jogador_vencedor = nome_jogador
            fim_partida = vitoria_velha(jogador_vencedor, jogo_grafico, log_jogo1, fim_partida)
    return fim_partida


def executar_movimento(posicao_grafico, lista_movimentos, movimento, jogador, jogo_grafico):
    jogo_grafico = jogo_grafico[:posicao_grafico[lista_movimentos.index(movimento)]] + jogador + jogo_grafico[posicao_grafico[lista_movimentos.index(movimento)]+1:]     
    posicao_grafico.pop(lista_movimentos.index(movimento))
    lista_movimentos.remove(movimento)
    return posicao_grafico, lista_movimentos, jogo_grafico


def vitoria_velha(jogador_vencedor, jogo_grafico,log_jogo1,fim_partida):
    print(jogo_grafico)
    print(f"\nFim de Jogo!!! \nO jogador que venceu o jogo da velha é o {jogador_vencedor}")
    with open(log_jogo1, "a") as arquivo_log1:
        arquivo_log1.write("\n" + jogador_vencedor + " venceu o jogo da velha")
    fim_partida = True
    return fim_partida


#Jogo da Forca
def jogo_da_forca(log_jogo2):
    print("Bem vindo ao jogo da forca de instrumentos musicais!!!")
    
    #Variáveis
    arquivo_dicionario = "dicionario.txt"
    nome_jogador = str(input("Digite o nome do jogador:")).lower().strip()
    tamanho_palavra = int(input("Qual o tamanho da palavra voce quer(digite o numero. ex: 6)? "))
    palavras_possiveis = []
    boneco = ['└', '┘', '_', '_', '│', 'O']
    posicao_boneco = [49,47,27,29,38,28]
    palavra_secreta = ""
    fim_de_jogo = False
    vida = 6
    forca_grafico = """
________ 
│      │ 
│        
│        
│        
│
│"""
    
    with open(arquivo_dicionario) as arquivo_dicionario_aberto:
        linhas_dicionario = arquivo_dicionario_aberto.readlines()      
    

    for linha in linhas_dicionario:
        linha = linha.replace('\n', '')
        if len(linha) == tamanho_palavra:
            palavras_possiveis.append(linha)
    
    if len(palavras_possiveis) == 0:
        print("Não existem palavras desse tamanho!!!")
        menu()
    
    posicao_palavra = random.randint(0, len(palavras_possiveis)-1)

    for letras in palavras_possiveis[posicao_palavra]:  
        palavra_secreta = palavra_secreta + '-'
  
    
    #Perguntando uma letra:
    while fim_de_jogo == False:
        print(forca_grafico)
        print(palavra_secreta)

        letra_escolhida = str(input("\nEscolha uma letra:")).lower().strip()
        
        if palavras_possiveis[posicao_palavra].find(letra_escolhida) != -1 and palavras_possiveis[posicao_palavra].find(letra_escolhida) != '' and len(letra_escolhida)<=1:
            while palavras_possiveis[posicao_palavra].find(letra_escolhida) != -1:
                palavra_secreta = palavra_secreta[:palavras_possiveis[posicao_palavra].index(letra_escolhida)] + letra_escolhida + palavra_secreta[palavras_possiveis[posicao_palavra].index(letra_escolhida)+1:]            
                palavras_possiveis[posicao_palavra] = palavras_possiveis[posicao_palavra].replace(letra_escolhida, ' ', 1)
        elif len(palavras_possiveis[posicao_palavra]) > 0 and vida > 0:
            forca_grafico = forca_grafico[:posicao_boneco[vida-1]] + boneco[vida-1] + forca_grafico[posicao_boneco[vida-1]+1:]
            print("Letra errada")
            vida -= 1
            
        if palavra_secreta.find('-') == -1:
            print(f"\nO jogador {nome_jogador} venceu!!! \nA palavra secreta era {palavra_secreta}")
            with open(log_jogo2, "a") as arquivo_log2:
                arquivo_log2.write(nome_jogador + " venceu o jogo da forca" + "\n")
            fim_de_jogo = True       
        elif vida <= 0:
            print(forca_grafico)
            print(f"\nO jogador {nome_jogador} perdeu!!!")
            fim_de_jogo = True
    else:
        print("Fim de Jogo!")
        menu()


menu()