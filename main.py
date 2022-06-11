import math
import random

#Funcao a ser minimizada
def fitness_function(x):
    return math.cos(x) * x + 2

#Intervalo de X
def random_value():
    return random.uniform(-20, 20)

#Realizar crossover
def crossover(lista, tam_lista):
    pai1, pai2 = random.randint(0, tam_lista-1), random.randint(0, tam_lista-1)
    if(lista[pai1] < lista[pai2]):
        return lista[pai1]
    return lista[pai2]

#Recebe o numero em DECIMANl e a quantidade de bits a ser representada em binario
#Retorna o numero binario
def dec_to_bin(int_dec, size_bin):
    return f"{int_dec:0{size_bin}b}"

def bin_to_dec(str_bin):
    return int(str_bin, 2)


#Converte um array binario em string
def bin_to_str(array):
    bin_str = ""
    for i in range(len(array)):
        bin_str += str(array[i])
    return bin_str


#Converte um array de binario para seu valor em decimal
def array_bin_to_dec(array):
    value_bin = bin_to_str(array)
    value_dec = bin_to_dec(value_bin)
    return value_dec

#Retornar o valor de X com base na codificacao do cromossomo binario do array
def decodificacao(array_bin, min, max, size_bin):
    #Converto o array binario para inteiro
    convert_bin = array_bin_to_dec(array_bin)
    x = min + ((max - min) * (convert_bin / (2**size_bin  - 1)))
    return x


def elitismo(geracao, min, max, size_bin):
    value_elite = float('inf')
    cromossomo = []
    
    for value in geracao:
        value_cromossomo_avaliado = decodificacao(value, min, max, size_bin)
        if(value_cromossomo_avaliado < value_elite):
            cromossomo = value
            value_elite = value_cromossomo_avaliado

    #print(cromossomo)
    return cromossomo

#Selecao por torneio
#Retorna uma lista com uma nova geracao
def new_generation(lista, min, max, qtd_bits):
    nova_geracao = []
    #Salvo o melhor valor para a proxima geracao
    nova_geracao.append(elitismo(lista, min, max, qtd_bits))
    tam_geracao = len(lista)
    #-1 porque ja foi aplicado o elitismo
    for _ in range(tam_geracao-1):
        pos1, pos2 = random.randint(0, tam_geracao-1), random.randint(0, tam_geracao-1)
        #Verifico qual melhor resultado com base no sorteio
        value1 = decodificacao(lista[pos1], min, max, qtd_bits)
        value2 = decodificacao(lista[pos2], min, max, qtd_bits)
        if(value1 < value2):
            nova_geracao.append(lista[pos1])
        else:
            nova_geracao.append(lista[pos2])
    
    return nova_geracao




#Cria uma populacao dado o tamanho e a quantidade de bits a ser representada
def populacao_inicial(tam_pop, tam_bit):
    populacao = []
    for _ in range(tam_pop):
        new_cromossomo = []
        for _ in range(tam_bit):
            new_cromossomo.append(random.randint(0,1))
        populacao.append(new_cromossomo)
    
    return populacao

#Apenas para fins de debugger
def show_value(lista):
    for value in lista:
        x = decodificacao(value, -20, 20, 16)
        y = fitness_function(x)
        print("%.5f \t\t %.3f" %(x, y))

def show_populacao(populacao):
    for value in populacao:
        print(value)

#Tamanho da populacao / Numero de geracoes / Quantidade de bits p/ cromossomo
def genetico_binario(tam_populacao_inicial, n_geracoes, qtd_bits, min, max):
    populacao = populacao_inicial(tam_populacao_inicial, qtd_bits)
    #Como queremos o menor valor: colocar o elite com um valor alto
    geracao = 0
    best_cromossomo = [0]
    while(geracao < n_geracoes):
        best_cromossomo = elitismo(populacao, min, max, qtd_bits)
        # print(len(populacao))
        print(decodificacao(best_cromossomo, min, max, qtd_bits))
        print(best_cromossomo)
        # show_value(populacao)
        #show_populacao(populacao)
        print('-----------------------------------------------')
        #input()
        populacao = new_generation(populacao, min, max, qtd_bits)
        #print(populacao)
        #Aplicar crossover
        #Aplicar mutacao
        geracao += 1



def main():
    #Para fins de teste
    #print(dec_to_bin(2288967, 22))
    #teste = [1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1]    
    #print(decodificacao(teste, -1, 2, 22))
    
    #Populacao / num de geracoes / tamanho do cromossomo
    genetico_binario(10, 20, 16, -20, 20)
main()