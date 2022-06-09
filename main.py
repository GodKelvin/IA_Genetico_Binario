import math
import random

#Funcao a ser minimizada
def fitness_function(x):
    return math.cos(x) * (x + 2)

#Intervalo de X
def random_value():
    return random.uniform(-20, 20)


#Selecao por torneio
def get_best(lista, tam_lista):
    pos1, pos2 = random.randint(0, tam_lista-1), random.randint(0, tam_lista-1)
    if(lista[pos1] < lista[pos2]):
        return lista[pos1]
    return lista[pos2]


#Alterar para selecao por roleto ao inves de torneio-----------------------------------------
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

def decodificacao(bin_number, min, max, size_bin):
    convert_bin = bin_to_dec(bin_number)
    x = min + ((max - min) * (convert_bin / (2**size_bin  - 1)))

    if(x < min):
        return min
    if(x > max):
        return max
    return x

def genetico_binario(tam_populacao_inicial, n_geracoes):
    populacao_inicial = []
    for i in range(tam_populacao_inicial):
        populacao_inicial.append(random_value())

    geracao = 1
    while(geracao < n_geracoes):
        new_population = []
        for i in range(tam_populacao_inicial):
            new_population.append(get_best(populacao_inicial, tam_populacao_inicial))
        
        print(populacao_inicial)
        print(new_population)

def main():
    #Para fins de teste
    #print(dec_to_bin(2288967, 22))
    print(decodificacao('1000101110110101000111', -1, 2, 22))





main()