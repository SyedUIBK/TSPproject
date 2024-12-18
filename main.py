import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_complete_graph(num_nodes, weight_range=(1, 100)):
  
    G = nx.complete_graph(num_nodes)
    for u, v in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)
    return G

def plot_graph_step(G, tour, current_node, pos):
 
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='red', node_size=500)
    path_edges = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='green', node_size=500)

    edge_labels = nx.get_edge_attributes(G, name='weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.pause(0.6)  # Shorter pause for smoother visualization

def calculate_tour_cost(G, tour):
    return sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

def nearest_neighbor_tsp(G, start_node=None):
    if start_node is None:
        start_node = random.choice(list(G.nodes))
    
    pos = nx.circular_layout(G)  
    plt.ion()
    plt.show()

    unvisited = set(G.nodes)
    unvisited.remove(start_node)

    tour = [start_node]
    current_node = start_node

    plot_graph_step(G, tour, current_node, pos)

    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        unvisited.remove(next_node)
        tour.append(next_node)
        current_node = next_node
        plot_graph_step(G, tour, current_node, pos)

    tour.append(start_node)  
    plot_graph_step(G, tour, current_node, pos)

    print("Tour:", tour)
    tour_cost = calculate_tour_cost(G, tour)
    print(f'Construction heuristic Tour Cost: {tour_cost}')

    plt.ioff()
    plt.show()

if __name__ == '__main__':
    G = generate_complete_graph(5)
    nearest_neighbor_tsp(G, start_node=0)
