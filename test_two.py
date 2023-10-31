import sys

NO_PARENT = -1

def dijkstra(adjacency_matrix, start_vertex, district_names):
    n_vertices = len(adjacency_matrix[0])

    shortest_distances = [sys.maxsize] * n_vertices
    added = [False] * n_vertices
    for vertex_index in range(n_vertices):
        shortest_distances[vertex_index] = sys.maxsize
        added[vertex_index] = False

    shortest_distances[start_vertex] = 0
    parents = [-1] * n_vertices
    parents[start_vertex] = NO_PARENT

    for i in range(1, n_vertices):
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        added[nearest_vertex] = True

        for vertex_index in range(n_vertices):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]

            if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance

    print_solution(start_vertex, shortest_distances, parents, district_names)


def print_solution(start_vertex, distances, parents, district_names):
    n_vertices = len(distances)
    print("Vertex\t Distance\tPath")

    for vertex_index in range(n_vertices):
        if vertex_index != start_vertex:
            print("\n", district_names[start_vertex], "->", district_names[vertex_index], "\t\t", distances[vertex_index], "\t\t", end="")
            print_path(vertex_index, parents, district_names)


def print_path(current_vertex, parents, district_names):
    if current_vertex == NO_PARENT:
        return
    print_path(parents[current_vertex], parents, district_names)
    print(district_names[current_vertex], end=" ")


if __name__ == '__main__':
    edge_weights = {
        ("Mchinji", "Kasungu"): 141,
        ("Mchinji", "Lilongwe"): 109,
        ("Lilongwe", "Dedza"): 92,
        ("Lilongwe", "Dowa"): 55,
        ("Kasungu", "Dowa"): 117,
        ("Kasungu", "Ntchisi"): 66,
        ("Dowa", "Ntchisi"): 38,
        ("Dowa", "Salima"): 67,
        ("Dedza", "Ntcheu"): 74,
        ("Dedza", "Salima"): 96,
        ("Nkhotakota", "Ntchisi"): 66,
        ("Nkhotakota", "Salima"): 112
    }
    
    district_names = ["Mchinji", "Lilongwe", "Kasungu", "Dedza", "Ntcheu", "Salima", "Dowa", "Ntchisi", "Nkhotakota"]
    
    start_vertex = 0
    
    adjacency_matrix = [[0] * len(district_names) for _ in range(len(district_names))]
    
    for i in range(len(district_names)):
        for j in range(i + 1, len(district_names)):
            edge = (district_names[i], district_names[j])
            if edge in edge_weights:
                weight = edge_weights[edge]
                adjacency_matrix[i][j] = weight
                adjacency_matrix[j][i] = weight
    
    dijkstra(adjacency_matrix, start_vertex, district_names)
