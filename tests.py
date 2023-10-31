# import sys

# NO_PARENT = -1

# def dijkstra(adjacency_matrix, start_vertex, district_names):
#     n_vertices = len(adjacency_matrix[0])

#     shortest_distances = [sys.maxsize] * n_vertices
#     added = [False] * n_vertices
#     for vertex_index in range(n_vertices):
#         shortest_distances[vertex_index] = sys.maxsize
#         added[vertex_index] = False

#     shortest_distances[start_vertex] = 0
#     parents = [-1] * n_vertices
#     parents[start_vertex] = NO_PARENT

#     for i in range(1, n_vertices):
#         nearest_vertex = -1
#         shortest_distance = sys.maxsize
#         for vertex_index in range(n_vertices):
#             if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
#                 nearest_vertex = vertex_index
#                 shortest_distance = shortest_distances[vertex_index]

#         added[nearest_vertex] = True

#         for vertex_index in range(n_vertices):
#             edge_distance = adjacency_matrix[nearest_vertex][vertex_index]

#             if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
#                 parents[vertex_index] = nearest_vertex
#                 shortest_distances[vertex_index] = shortest_distance + edge_distance

#     print_solution(start_vertex, shortest_distances, parents, district_names)


# def print_solution(start_vertex, distances, parents, district_names):
#     n_vertices = len(distances)
#     print("Vertex\t Distance\tPath")

#     for vertex_index in range(n_vertices):
#         if vertex_index != start_vertex:
#             print("\n", district_names[start_vertex], "->", district_names[vertex_index], "\t\t", distances[vertex_index], "\t\t", end="")
#             print_path(vertex_index, parents, district_names)


# def print_path(current_vertex, parents, district_names):
#     if current_vertex == NO_PARENT:
#         return
#     print_path(parents[current_vertex], parents, district_names)
#     print(district_names[current_vertex], end=" ")


# if __name__ == '__main__':
#     district_names = ["Mchinji", "Lilongwe", "Kasungu", "Dedza", "Ntcheu", "Salima", "Dowa", "Ntchisi", "Nkhotakota"]

#     adjacency_matrix = [
#         [0, 109, 141, 0, 0, 0, 0, 0, 0],
#         [109, 0, 55, 92, 0, 0, 0, 0, 0],
#         [141, 55, 0, 0, 0, 0, 117, 66, 0],
#         [0, 92, 0, 0, 74, 96, 0, 0, 0],
#         [0, 0, 0, 74, 0, 0, 0, 0, 0],
#         [0, 0, 0, 96, 0, 0, 0, 67, 112],
#         [0, 0, 117, 0, 0, 0, 0, 38, 0],
#         [0, 0, 66, 0, 0, 67, 38, 0, 66],
#         [0, 0, 0, 0, 0, 112, 0, 66, 0]
#     ]
#     start_vertex = 0

#     dijkstra(adjacency_matrix, start_vertex, district_names)


# import sys

# class ShortestPathFinder:
#     def __init__(self, district_names, adjacency_matrix, start_vertex):
#         self.district_names = district_names
#         self.adjacency_matrix = adjacency_matrix
#         self.start_vertex = start_vertex
#         self.NO_PARENT = -1

#     def dijkstra(self):
#         n_vertices = len(self.adjacency_matrix[0])

#         shortest_distances = [sys.maxsize] * n_vertices
#         added = [False] * n_vertices

#         for vertex_index in range(n_vertices):
#             shortest_distances[vertex_index] = sys.maxsize
#             added[vertex_index] = False

#         shortest_distances[self.start_vertex] = 0
#         parents = [-1] * n_vertices
#         parents[self.start_vertex] = self.NO_PARENT

#         for i in range(1, n_vertices):
#             nearest_vertex = -1
#             shortest_distance = sys.maxsize

#             for vertex_index in range(n_vertices):
#                 if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
#                     nearest_vertex = vertex_index
#                     shortest_distance = shortest_distances[vertex_index]

#             added[nearest_vertex] = True

#             for vertex_index in range(n_vertices):
#                 edge_distance = self.adjacency_matrix[nearest_vertex][vertex_index]

#                 if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
#                     parents[vertex_index] = nearest_vertex
#                     shortest_distances[vertex_index] = shortest_distance + edge_distance

#         return self._get_solution(shortest_distances, parents)

#     def _get_solution(self, distances, parents):
#         n_vertices = len(distances)
#         solution = []

#         for vertex_index in range(n_vertices):
#             if vertex_index != self.start_vertex:
#                 path = self._get_path(vertex_index, parents)
#                 total_distance = distances[vertex_index]
#                 solution.append((self.district_names[self.start_vertex], self.district_names[vertex_index], total_distance, path))

#         return solution

#     def _get_path(self, current_vertex, parents):
#         path = []
#         self._get_recursive_path(current_vertex, parents, path)
#         return path

#     def _get_recursive_path(self, current_vertex, parents, path):
#         if current_vertex == self.NO_PARENT:
#             return
#         self._get_recursive_path(parents[current_vertex], parents, path)
#         path.append(self.district_names[current_vertex])

# if __name__ == '__main__':
#     district_names = ["Mchinji", "Lilongwe", "Kasungu", "Dedza", "Ntcheu", "Salima", "Dowa", "Ntchisi", "Nkhotakota"]

#     adjacency_matrix = [
#         [0, 109, 141, 0, 0, 0, 0, 0, 0],
#         [109, 0, 55, 92, 0, 0, 0, 0, 0],
#         [141, 55, 0, 0, 0, 0, 117, 66, 0],
#         [0, 92, 0, 0, 74, 96, 0, 0, 0],
#         [0, 0, 0, 74, 0, 0, 0, 0, 0],
#         [0, 0, 0, 96, 0, 0, 0, 67, 112],
#         [0, 0, 117, 0, 0, 0, 0, 38, 0],
#         [0, 0, 66, 0, 0, 67, 38, 0, 66],
#         [0, 0, 0, 0, 0, 112, 0, 66, 0]
#     ]

#     start_vertex = 0

#     shortest_path_finder = ShortestPathFinder(district_names, adjacency_matrix, start_vertex)
#     shortest_path_solution = shortest_path_finder.dijkstra()

#     for start, end, distance, path in shortest_path_solution:
#         print(f"{start} -> {end}\t Distance: {distance}\t Path: {' -> '.join(path)}")
