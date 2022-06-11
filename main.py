import math
import random


#Apenas para fins de debugger
def show_value(lista):
    for value in lista:
        x = decodificacao(value, -20, 20, 16)
        y = fitness_function(x)
        print("%f \t\t %f" %(x, y))

def show_populacao(populacao):
    for value in populacao:
        print(value)

#Funcao a ser minimizada
def fitness_function(x):
    return math.cos(x) * x + 2

def mutacao(cromossomo, taxa_mutacao):
    muta = random.uniform(0, 1)
    if(muta >= taxa_mutacao):
        change_bit = random.randint(0, len(cromossomo)-1)
        if(cromossomo[change_bit]):
            cromossomo[change_bit] = 0
        else:
            cromossomo[change_bit] = 1
    return cromossomo


def crossover(pai1, pai2, taxa_crossover):
    filho1 = 0
    filho2 = 0
    cross = random.uniform(0, taxa_crossover)
    if(cross >= taxa_crossover):
        half_cromossomo = len(pai1) / 2
        filho1 = (pai1[:half_cromossomo] + pai2[half_cromossomo:])
        filho2= (pai1[half_cromossomo:] + pai2[:half_cromossomo])
    else:
        filho1 = pai1
        filho2 = pai2

    return filho1, filho2
#Criacao de novos filhos aplicando crossover e mutacao
def gera_filhos(pais, taxa_crossover, taxa_mutacao, best_cromossomo):
    filhos = []
    filhos.append(best_cromossomo)
    #Cria uma quantidade de filhos igual a de pais
    while(len(filhos) < len(pais)):
        pos_pai1, pos_pai2 = random.randint(0, len(pais)-1), random.randint(0, len(pais)-1)
        pai1 = pais[pos_pai1]
        pai2 = pais[pos_pai2]

        #Aplica crossover
        filho1, filho2 = crossover(pai1, pai2, taxa_crossover)

        #Aplicar taxa de mutacao
        filho1 = mutacao(filho1, taxa_mutacao)
        filho2 = mutacao(filho2, taxa_mutacao)

        filhos.append(filho1)
        if(len(filhos) < len(pais)):
            filhos.append(filho2)

        #show_populacao(filhos)
        #print(best_cromossomo)
        #print("-----")
    return filhos

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
        x = decodificacao(value, min, max, size_bin)
        value_x = fitness_function(x)
        if(value_x < value_elite):
            cromossomo = value
            value_elite = value_x
    return cromossomo

#Selecao por torneio
#Retorna uma lista com uma nova geracao
def best_values(lista, min, max, qtd_bits):
    nova_geracao = []
    tam_geracao = len(lista)
    #-1 porque ja foi aplicado o elitismo
    for _ in range(tam_geracao):
        pos1, pos2 = random.randint(0, tam_geracao-1), random.randint(0, tam_geracao-1)
        #Verifico qual melhor resultado com base no sorteio
        x1 = decodificacao(lista[pos1], min, max, qtd_bits)
        x2 = decodificacao(lista[pos2], min, max, qtd_bits)
        if(fitness_function(x1) < fitness_function(x2)):
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




#Tamanho da populacao / Numero de geracoes / Quantidade de bits p/ cromossomo / valores min e max
#retorna: #[0] = cromossomo, [1] = valor de x, [2] = valor de y
def genetico_binario(tam_populacao_inicial, n_geracoes, qtd_bits, min, max):
    populacao = populacao_inicial(tam_populacao_inicial, qtd_bits)
    geracao = 0
    best_cromossomo = [0]
    while(geracao < n_geracoes):
        #Salva o melhor valor da populacao
        best_cromossomo = elitismo(populacao.copy(), min, max, qtd_bits)

        #Captura os pais via torneio
        pais = best_values(populacao.copy(), min, max, qtd_bits)
        #Gera uma nova populacao
        populacao = gera_filhos(pais.copy(), 0.6, 0.01, best_cromossomo.copy())
        #best_cromossomo = elitismo(populacao.copy(), min, max, qtd_bits)
        geracao += 1
    best_cromossomo = elitismo(populacao.copy(), min, max, qtd_bits)
    return [best_cromossomo, decodificacao(best_cromossomo, min, max, qtd_bits), fitness_function(decodificacao(best_cromossomo, min, max, qtd_bits))]

def run_genetico_binario():
    result_10 = []
    result_20 = []

    result_100 = []
    for _ in range(10):
        res_10 = genetico_binario(10, 10, 16, -20, 20)
        res_20 = genetico_binario(10, 20, 16, -20, 20)
        res_100 = genetico_binario(10, 100, 16, -20, 20)

        #[0] = cromossomo, [1] = valor de x, [2] = valor de y
        result_10.append(res_10[2])
        result_20.append(res_20[2])
        result_100.append(res_100[2])
    
    #Tirando a media dos menores valores encontrados
    media_10 = 0
    media_20 = 0
    media_100 = 0
    for i in range(10):
        media_10 += result_10[i]
        media_20 += result_20[i]
        media_100 += result_100[i]
    
    media_10 = media_10 / 10
    media_20 = media_20 / 10
    media_100 = media_100 / 10
    
    print(media_10)
    print(media_20)
    print(media_100)
        

def main():
    #Para fins de teste
    #print(dec_to_bin(2288967, 22))
    #teste = [1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1]  
    #teste = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]  
    #print(decodificacao(teste, -1, 2, 22))
    
    #Populacao / num de geracoes / tamanho do cromossomo, valor min e valor max
    #print(genetico_binario(10, 10, 16, -20, 20))
    run_genetico_binario()
main()