'''
    Autor: Júlio Campos
    Data: 22/05/19

    Algoritmo de Dijkstra
    Encontra o caminho mais curto (menor distância) entre dois nós em um grafo ponderado
'''

# grafo representado em dicionário (tabela hash)
graph = {
    's': {'a': 2, 'b': 1},
    'a': {'s': 3, 'b': 4, 'c': 8},
    'b': {'s': 4, 'a': 2, 'd': 2},
    'c': {'a': 2, 'd': 7, 't': 4},
    'd': {'b': 1, 'c': 11, 't': 5},
    't': {'c': 3, 'd': 5}
}

# obter lista de nós do grafo
nodes = list(graph.keys())

# primeiro nó do grafo
start = nodes[0]

# último nó do grafo
end = nodes[len(nodes)-1]


def dijkstra(graph: dict, start: str, end: str):

    # dicionário que armazena todos os nós visitados com suas distâncias
    visited = {}

    # dicionário que armazena todos os nós não visitados com suas distâncias
    unvisited = {}

    # dicionário que armazena os predecessores dos nós visitados
    predecessor = {}

    # lista que armazena o percurso do menor caminho entre o nó inicial e final
    path = []

    # inicializar todos os nós não visitados com distância infinita
    for node in graph:
        unvisited[node] = float('inf')

    # atribui ao nó inicial a distância 0
    unvisited[start] = 0

    # enquanto existirem nós não visitados
    while unvisited:

        # obter o nó que possui a menor distância total
        min_node = min(unvisited, key=unvisited.get)

        # visitar todos os vizinhos desse nó
        for neighbour, weight in graph[min_node].items():

           # se um vizinho não foi visitado
            if neighbour not in visited:

                # relaxamento: calcular a nova distância até o nó vizinho
                new_distance = unvisited[min_node] + graph[min_node][neighbour]

                # impressões
                print('\n- nó', min_node)
                print('     vizinho:', neighbour)
                print('     nova distância:', new_distance)
                print('     distância mínima:', weight)

                # se a distância até o vizinho for menor que a atual, atualiza os valores
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    predecessor[neighbour] = min_node

        # adicionar nó visitado no dicionário
        visited[min_node] = unvisited[min_node]

        # remover nó não visitado do dicionário
        unvisited.pop(min_node)

        # se chegou ao nó final, pára o algoritmo. Não irá calcular a distância entre o nó final e os seus vizinhos
        if min_node == end:
            break

    # criar lista com caminho mínimo
    for key, value in predecessor.items():

        # se a chave é o nó final
        if key is end:

            # adiciona o nó final a lista
            path.append(end)

            # adiciona o predecessor do nó final
            path.append(predecessor[key])

            # se o valor da chave não é o nó inicial
            if value is not start:

                # adiciona o predecessor do valor da chave na lista
                path.append(predecessor[value])

                # se o predecessor do valor da chave não é o nó inicial
                if predecessor[value] is not start:

                    # adiciona o nó inicial na lista
                    path.append(start)

    # obter lista das distâncias dos nós visitados
    list_visited = list(visited.values())

    # imprimir quantidade de nós visitados
    print(f'\nNós visitados: {len(visited)}')

    # imprimir a menor distância entre os nós inicial e final (último elemento da lista)
    print(f"A menor distância entre '{start}' e '{end}' é {list_visited[len(list_visited)-1]}")

    # imprimir caminho
    print(f'O caminho mais curto é: {list(reversed(path))}')


# executar função passando como parâmetros o grafo, o nó inicial e o nó final
dijkstra(graph, start, end)
