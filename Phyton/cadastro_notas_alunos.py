"""ALGORITMO PARA CADASTRAR ALUNOS E NOTAS
PASSO 1: USUÁRIO INFORMA NOME DO ALUNO
PASSO 2: USUÁRIO INFORMA AS NOTAS DOS ALUNOS
PASSO 3: PROGRAMA DEVOLVE, NOME, NOTAS, MÉDIA E SITUAÇÃO



"""



import time

def aluno_notas():
    t0 = time.time()
    alunos = []
    medias =[]
    notas = 0
    contador = 0
    while True:
        notas = 0
        contador = 0
        nome = input("Digite o nome do aluno ou 0 pra sair: ")
        if nome == '0':
            print("Cadastro finalizado!")
            break
        else:
            alunos.append(nome)        
            while True:
                nota = float(input("Digite as notas do aluno ou -1 para cadastrar o próximo aluno: "))
                if nota == int(-1):
                    print("Aluno finalizado!")
                    break
                else:
                    notas = notas + nota
                    contador = contador + 1
        media = notas/contador
        medias.append(media)
        print(f'Nome: {nome} Média: {media}')
    t1 = time.time()
    print(f'Total de {len(alunos)} alunos e total de {t1-t0:.2f} segundos')
