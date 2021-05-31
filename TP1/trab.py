import re
import difflib

inscritos = []
inscricoes = []
dic = []

f = open("inscritos-form.json", encoding='UTF-8')

docJSON = f.read()

inscricao = re.findall(r'(".*":([^[].*))', docJSON)
#print(inscricao)

for elem in inscricao:
    queroisto = re.search(r'"((\w*|\s|\W)*)"', elem[1])
    inscritos.append(queroisto.group(1))

#print(inscritos)
for val in range(0, len(inscritos), 7):
    next_jump = val + 7
    shot_values = inscritos[val:next_jump]
    inscricoes.append(shot_values)

#print(inscricoes)
#print("\n")
#elemDicionario = ["nome", "dataNasc", "morada", "email", "prova", "escalao", "equipa"]

dados = {} #dados que contem um elemento do dicionario

for e in inscricoes:
    dados['nome'] = e[0].upper()
    dados['dataNasc'] = e[1].upper()
    dados['morada'] = e[2].upper()
    dados['email'] = e[3].upper()
    dados['prova'] = e[4].upper()
    dados['escalao'] = e[5].upper()
    dados['equipa'] = e[6].upper()
    dic.append(dados)
    dados = {}


print("Boa Noite de Estudo!!!\n\n")
print(
    "Escolha uma opcao:\n   1:Pessoas Individuais de Valongo\n   2:Paulos ou Ricardos\n   3:Equipa Turbulentos\n   4:Escaloes\n   5:Site Bonitao LEGIT!!!\n\n6:Sair do Programa\n")
opcao = input()

while opcao != '6':
    if opcao == '1':
        for i in dic:
            if re.search(r'(?i)valongo', i['morada']) and re.search(r'(?i)individual', i['equipa']):
                nome = i['nome']
                print("Nome: " + nome.upper() + "\n\n")

    if opcao == '2':
        for i in dic:
            if (re.match(r'(?i)ricardo', i['nome']) or re.match(r'(?i)paulo', i['nome'])) and re.search(r'(?i)gmail', i['email']):
                nome = i['nome']
                prova = i['prova']
                print("Nome: " + nome.upper() + "\n" + "Prova :" + prova.upper() + "\n\n")

    if opcao == '3':
        for i in dic:
            if re.search(r'(?i)turbulentos', i['equipa']):
                nome = i['nome']
                data = i['dataNasc']
                morada = i['morada']
                email = i['email']
                prova = i['prova']
                escalao = i['escalao']
                equipa = i['equipa']
                print("Nome: " + nome.upper() + "\nData: " + data.upper() + "\nMorada: " + morada.upper() + "\nEmail: " + email.upper() + "\nProva: " + prova.upper()
                      + "\nEscalao: " + escalao.upper() + "\nEquipa: " + equipa.upper() + "\n\n")

    if opcao == '4':
        escaloes = []
        escalaoAtletas = []

        for i in dic:
            escalao = i['escalao']
            escalaoAtletas.append(escalao)

        escaloes = escalaoAtletas.copy()  # Copia Lista para se operar sem perder info
        escaloes.sort()  # Ordena Lista
        escaloes = list(dict.fromkeys(escaloes))  # Remove Duplicados

        for k in escaloes:
            if k == "":
                print("\nSem Escalao: " + str(escalaoAtletas.count(k)))  # Conta Atletas Sem Escalao
            else:
                print("\n" + k + ": " + str(escalaoAtletas.count(k)))  # Conta Atletas por cada Escalao

    if opcao == '5':
        original = []
        dup = []

        for i in dic:
            equipa = i['equipa']
            original.append(equipa.upper()) #contém 281 equipas

        dup = list(dict.fromkeys(original))  # Remove Duplicados -> ficam 76 equipas


        for index, k in enumerate(original):
            for j in dup:
                string1 = k
                string2 = j
                matches = difflib.SequenceMatcher(
                    None, string1, string2).ratio()

                if(matches >= 0.7):
                    original[index] = j


        equipasOficias = original.copy() #cópia da lista original já com os nomes corretos
        equipasOficias = list(dict.fromkeys(equipasOficias))  # Remove Duplicados


        #atualiza o dicionário com os nomes iguais
        for d in dic:
            for e in equipasOficias:
                string1 = d['equipa']
                string2 = e.upper() #transforma em maiúscula para comparar com as equipas do dic que estão em maiúsculas
                matches = difflib.SequenceMatcher(
                    None, string1, string2).ratio()
                if (matches >= 0.7):
                    d['equipa'] = e

        # troca os | e / por espaços nas equipas para ser mais fácil criar o respetivo ficheiro html
        for d in dic:
            if (re.search(r'\|', d['equipa'])):
                d['equipa'] = re.sub(r'\|', ' ', d['equipa'])
            elif (re.search(r'\/', d['equipa'])):
                d['equipa'] = re.sub(r'\/', ' ', d['equipa'])


        equipasOficiasAtual2 = [] #coném as equipas sem | e /
        for d in dic:
            equipasOficiasAtual2.append(d['equipa'])

        equipasOficiasAtual = list(dict.fromkeys(equipasOficiasAtual2))



        #-------------------------------------------HTML---------------------------------------------


        dicEquipas = {} #vai conter o nome das equipas e o numero de atletas de cada equipa

        for ele in equipasOficiasAtual:
            somatorio = 0
            somatorio = somatorio + equipasOficiasAtual2.count(ele) #soma o numeroa de elementos de equipas com o nome parecido
            dicEquipas[ele] = somatorio #coloca o numeroa de elementos na equipa com nome na posicao 0 de ele
        equipasOrdenadas = sorted(dicEquipas.items(), key=lambda x: x[1], reverse=True) #cria tuplos com os elementos do dicEquipas ordenados de forma decrescente pelo numero de atletas


        f = open("equipas.html", "w")

        f.write('''<!DOCTYPE html>
        <html>
            <head meta charset="UTF-8">
                <title>Equipas</title>
            </head>
            <body>
                <h1>Equipas</h1>
                <ul>
                    ''')

        #adiciona as equipas no ficheiro principal
        for i in equipasOrdenadas: #tuplo
            if (re.search(r'\s', i[0])):  # cria os nomes dos ficheiros em html com _ em vez de espaço
                nomeEquipa2 = re.sub(r'\s',
                                     r'_',
                                     i[0])
                f.write("<li><a href=\"" + str(nomeEquipa2) + ".html\">" + str(i[0]) + "</a>: " + str(i[1]) + "</li><br>")
            else:
                f.write("<li><a href=\"" + str(i[0]) + ".html\">" + str(i[0]) + "</a>: " + str(i[1]) + "</li><br>")
        f.write('''</ul>
             </body>
        </html>''')

        f.close()

        # cria os ficheiros das equipas e adiciona os inscritos de cada equipa
        for i in equipasOficiasAtual:
            if (re.search(r'\s', i)):
                nomeEquipa = re.sub(r'\s',
                                     r'_',
                                     i)
                newfile = open(str(nomeEquipa) + ".html", "w")
            else:
                newfile = open(str(i) + ".html", "w")
            newfile.write('''<!DOCTYPE html>
                <html>
                    <head meta charset="UTF-8">
                        <title>''' + str(i) + ''''</title>
                    </head>
                    <body>
                    <h1>''' + str(i) + '''</h1><br>
                    <ul>
                    ''')
            for d in dic:
                if i == d['equipa']:
                    newfile.write("<li>" + d['nome'] + "</li>")
            newfile.write('''</ul>
                    </body>
                    </html>''')
            newfile.close()

    print(
        "\n\nEscolha uma opcao:\n   1:Pessoas Individuais de Valongo\n   2:Paulos ou Ricardos\n   3:Equipa Turbulentos\n   4:Escaloes\n   5:Site Bonitao LEGIT!!!\n\n6:Sair do Programa\n")
    opcao = input()

print("Ate uma proxima")
