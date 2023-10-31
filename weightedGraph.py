import sys

class ShortestPathFinder:
    def __init__(self, district_names, adjacency_matrix, start_vertex):
        # Initialize the class with district names, adjacency matrix, and start vertex, We will be starting from Mchinji
        self.district_names = district_names
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex

        # when a vertex is not connected to any other vertex in the graph, there's no parent
        self.NO_PARENT = -1

    # Use dijkstra's a;gorithm to find the shortest path for the weighted graph
    def dijkstra(self):
        number_of_vertices = len(self.adjacency_matrix[0])

        # Initialize distance and added arrays
        shortest_distances = [sys.maxsize] * number_of_vertices
        added = [False] * number_of_vertices

        for vertex_index in range(number_of_vertices):
            shortest_distances[vertex_index] = sys.maxsize
            added[vertex_index] = False

        # Set the distance from the start vertex to itself as 0
        shortest_distances[self.start_vertex] = 0

        # Initialize parents array
        parents = [-1] * number_of_vertices
        parents[self.start_vertex] = self.NO_PARENT

        for i in range(1, number_of_vertices):
            nearest_vertex = -1
            shortest_distance = sys.maxsize

            # Find the nearest vertex
            for vertex_index in range(number_of_vertices):
                if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                    nearest_vertex = vertex_index
                    shortest_distance = shortest_distances[vertex_index]

            added[nearest_vertex] = True

            # Update distances
            for vertex_index in range(number_of_vertices):
                edge_distance = self.adjacency_matrix[nearest_vertex][vertex_index]

                if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
                    parents[vertex_index] = nearest_vertex
                    shortest_distances[vertex_index] = shortest_distance + edge_distance

        return self._get_solution(shortest_distances, parents)

    def _get_solution(self, distances, parents):
        number_of_vertices = len(distances)
        solution = []

        for vertex_index in range(number_of_vertices):
            if vertex_index != self.start_vertex:
                path = self._get_path(vertex_index, parents)
                total_distance = distances[vertex_index]
                solution.append((self.district_names[self.start_vertex], self.district_names[vertex_index], total_distance, path))

        return solution

    def _get_path(self, current_vertex, parents):
        path = []
        self._get_recursive_path(current_vertex, parents, path)
        return path

    def _get_recursive_path(self, current_vertex, parents, path):
        if current_vertex == self.NO_PARENT:
            return
        self._get_recursive_path(parents[current_vertex], parents, path)
        path.append(self.district_names[current_vertex])

if __name__ == '__main__':
    district_names = ["Mchinji", "Lilongwe", "Kasungu", "Dedza", "Ntcheu", "Salima", "Dowa", "Ntchisi", "Nkhotakota"]

    adjacency_matrix = [
        [0, 109, 141, 0, 0, 0, 0, 0, 0],
        [109, 0, 55, 92, 0, 0, 0, 0, 0],
        [141, 55, 0, 0, 0, 0, 117, 66, 0],
        [0, 92, 0, 0, 74, 96, 0, 0, 0],
        [0, 0, 0, 74, 0, 0, 0, 0, 0],
        [0, 0, 0, 96, 0, 0, 0, 67, 112],
        [0, 0, 117, 0, 0, 0, 0, 38, 0],
        [0, 0, 66, 0, 0, 67, 38, 0, 66],
        [0, 0, 0, 0, 0, 112, 0, 66, 0]
    ]

    start_vertex = 0

    shortest_path_finder = ShortestPathFinder(district_names, adjacency_matrix, start_vertex)
    shortest_path_solution = shortest_path_finder.dijkstra()

    for start, end, distance, path in shortest_path_solution:
        print(f"{start} -> {end}\t Distance: {distance}\t Path: {' -> '.join(path)}")
