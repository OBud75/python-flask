import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        shortest_path = {}

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    shortest_path[neighbor] = current_vertex

        return distances, shortest_path

    def draw_graph(self, output_file="graph.png"):
        G = nx.DiGraph()
        for vertex in self.edges:
            for neighbor, weight in self.edges[vertex]:
                G.add_edge(vertex, neighbor, weight=weight)
        
        pos = nx.spring_layout(G)
        plt.figure()
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold', arrows=True)
        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.savefig(output_file)
        plt.close()


