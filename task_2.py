import random


class Map:
    def __init__(self, m, n, land_ratio):
        self.m = m  # number of lines
        self.n = n  # number of columns
        self.land_ratio = land_ratio
        self.grid = [[0] * n for _ in range(m)]  # initializing the grid

    def generate_map(self):
        for i in range(self.m):
            for j in range(self.n):
                if random.random() < self.land_ratio:
                    self.grid[i][j] = 1  # 1 - represents land, 0 - represents water

    def display_map(self):
        for row in self.grid:
            print(' '.join(map(str, row)))

    def is_valid_move(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y] == 0

    def shortest_path(self, start, end):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        visited = set()
        queue = [(start, 0)]

        while queue:
            (x, y), dist = queue.pop(0)
            if (x, y) == end:
                return dist
            visited.add((x, y))
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if self.is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append(((new_x, new_y), dist + 1))
        return -1

# obtaining parameters from the user
m = int(input("Введите количество строк (M): "))
n = int(input("Введите количество столбцов (N): "))
land_ratio = float(input("Введите долю суши от общей площади поля (0-1): "))

# creating the map
map_obj = Map(m, n, land_ratio)
map_obj.generate_map()
print("Сгенерированная карта:")
map_obj.display_map()

# asking for coordinates of points A and B
print(f'Границы поля от 1:1 до {m}:{n}')
start_x = (int(input("Введите координату x точки A: "))) - 1
start_y = (int(input("Введите координату y точки A: "))) - 1
end_x = (int(input("Введите координату x точки B: "))) - 1
end_y = (int(input("Введите координату y точки B: "))) - 1


# finding the shortest path and displaying the result
distance = map_obj.shortest_path((start_y, start_x), (end_y, end_x))
if distance != -1:
    print(f"Кратчайший путь из точки A в точку B: {distance} клеток.")
else:
    print("Пути из точки A в точку B не существует.")