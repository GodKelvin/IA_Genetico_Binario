import math
import random

from scipy import rand

#Funcao a ser minimizada
def fitness_function(x):
    return math.cos(x) * x + 2

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


#Cria uma populacao dado o tamanho e a quantidade de bits a ser representada
def populacao_inicial(tam_pop, tam_bit):
    populacao = []
    for _ in range(tam_pop):
        new_cromossomo = []
        for _ in range(tam_bit):
            new_cromossomo.append(random.randint(0,1))
        populacao.append(new_cromossomo)
    
    return populacao

#def genetico_binario(tam_populacao_inicial, n_geracoes):


#Apenas para fins de debugger
def show_value(lista):
    for value in lista:
        x = decodificacao(value, -20, 20, 16)
        y = fitness_function(x)
        print("%.5f \t\t %.3f" %(x, y))

def main():
    #Para fins de teste
    #print(dec_to_bin(2288967, 22))
    #teste = [1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1]    
    #print(decodificacao(teste, -1, 2, 22))
    
    lista = populacao_inicial(10, 16)
    show_value(lista)
    #print(fitness_function(-16))







main()