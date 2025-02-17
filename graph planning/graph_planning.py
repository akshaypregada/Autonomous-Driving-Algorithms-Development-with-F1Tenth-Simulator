
import networkx as nx

def shortest_path(graph, start, goal):
    """
    Compute the shortest path using Dijkstra's algorithm.
    """
    return nx.dijkstra_path(graph, start, goal)

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(1, 2, {'weight': 1}), (2, 3, {'weight': 2}), (3, 4, {'weight': 1}), (1, 4, {'weight': 4})])
    
    start_node = 1
    goal_node = 4
    path = shortest_path(G, start_node, goal_node)
    
    print("Shortest Path:", path)
