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

def crossover(pai, filho):
    

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
        input()


def main():
    genetico_binario(10, 10)



main()