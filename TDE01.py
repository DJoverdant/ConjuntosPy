# André Esteves Arantes

def lists_function(mode):  #Escolha de arquivo

    if mode == 1: #List_1
        content = open("List_1.txt", "r").readlines()

    if mode == 2: #List_2
        content = open("List_2.txt", "r").readlines()

    if mode == 3: #List_3
        content = open("List_3.txt", "r").readlines()

    if mode == 4: #txt do usuario, exemplo: C:\Users\andre\Desktop\python\lista34.txt
        content = open(input("Digite o caminho do arquivo: "), "r").readlines()

    return content


def main(mode, list, list2):  #função principal(operações, primeira lista, segunda lista)

    list_1 = set(list)  #list = [] --> list = {}
    list_2 = set(list2) 

    if mode == "U":
        print(f'\nUnião: {list_1|list_2}')

    elif mode == "I":
        print(f'\nInterseção: {list_1&list_2}')

    elif mode == "D": 
        print(f'\nDiferença: {list_1-list_2}')

    elif mode == "C":
        result = [] 
        for x in range(len(list)):  #[0,0][0,1][0,2]...[2,0][2,1].....
            for y in range(len(list2)):
                result.append([list[x], list2[y]]) #vai adicionando os valores à lista result
        print(f'\nProduto Cartesiano: {result}')

    else:
        print('\nArquivo com formatação incorreta.')

    print('=' * 100)

# Chama a função de escolha de arquivo
file = lists_function(int(input("Escolha entre as opções:\n[1]List_1\n[2]List_2\n[3]List_3\n[4]Escolha um arquivo próprio\n")))
lista = [] #lista utilizada abaixo para formatação
ops = [] #lista dos operadores 

for line in file:
    lista.append(line.strip())  #remove espaços em branco

for x in range(len(lista)):
    lista[x] = lista[x].split(",")  #separa usando a vírgula como parâmetro

    if (x - 1) % 3 == 0:
        ops.append(lista[x][0]) #adiciona e formata os valores da lista sem os '[]' à ops, ou seja, ao inves de ops = [['I'],['U']], temos ops = ['I','U']

for value in range(len(ops)):
    main(ops[value], lista[3 * value + 2], lista[3 * value + 3])  # ops[0] = I, ops[1] = C...
