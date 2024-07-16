''' FERRAMENTA PARA VERIFICAR CARACTERES USANDO REGEX
1- USUÁRIO FORNECE CARACTERES
2- É FEITO A ANÁLISE DOS CARACTERES
3- AO FINAL É INFORMADO SE OS CARACTERES TEM O PADRÃO DE PLACA ANTIGA, PLACA MERCOSUL OU FOI UMA ENTRADA INVÁLIDA E TEMPO DE USO

CONDIÇÕES PARA TESTE SE É PLACA: OCD8547 OU OCD8F47
 1- COMEÇA COM LETRA
 2- TERMINA COM NÚMERO
 3- TEM 7 CARACTERES
 4- TEM LETRAS E NÚMEROS
 4- TEM 3 LETRAS E 4 NÚMEROS(PLACA ANTIGA)
 5- TEM 4 LETRAS E 3 NÚMEROS(MERCOSUL)

'''
import time
import re

t0 = time.time()
while True:
    placa = input('Informe a placa(sem hífen) ou 0 para finalizar:')
    if re.match(r"^[A-Za-z]{3}[0-9]{4}$", placa):
        print("Segue o padrão de placa antiga. Fazer consulta nas bases de dados para confirmar se é placa veicular")
    elif re.match(r"^[A-Za-z]{3}[0-9]{1}[A-Za-z]{1}[0-9]{2}$", placa):
            print("Segue o padrão de placa mercosul. Fazer consulta nas bases de dados para confirmar se é placa veicular")
    elif placa == '0':
        print('Consulta Finalizada')
        break
    else:
        print("A entrada não é válida!")          
t1 = time.time()
print(f'Uso finalizado em {t1-t0:.2f} segundos')