import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 7},
    'C': {'A': 4, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 7, 'F': 3},
    'F': {'C': 5, 'E': 3}
}

start_node = 'A'
print("Shortest distances from", start_node, "using Dijkstra's Algorithm:")
print(dijkstra(graph, start_node))
