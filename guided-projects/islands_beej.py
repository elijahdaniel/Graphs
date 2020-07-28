# Matrix

# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west. For example:
# (N, S, E, W)

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


'''
visited = [[F, T, F, F, F],
           [T, T, F, F, F],
           [F, F, F, F, F],
           [F, F, F, F, F],
           [F, F, F, F, F]]

island_counter(islands)  # returns 4

islands[0][1]
islands[1][1]


# 1. Describe in graph terminology
# - What are our nodes?
# - What are our connections? If NSEW

# What do we call a group of 1s/nodes? Connected components.
'''


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def island_counter(islands):
    row_count = len(islands)
    col_count = len(islands[0])

    # create a visited matrix
    visited = []

    # _ shows that it will be unused
    for _ in range(row_count):
        visited.append([False] * col_count)

    island_count = 0

    # walk through each cell of the matrix
    for row in range(row_count):
        for col in range(col_count):
            # if it's not been visited
            if not visited[row][col]:
                # if we hit a 1 on the islands
                if islands[row][col] == 1:

                    # traverse and mark each as visited
                    dft(row, col, islands, visited)

                    # increment counter
                    island_counter += 1

    return island_count


def dft(row, col, islands, visited):
    s = Stack()

    s.push((row, col))

    while s.size() > 0:
        # since it's deconstructed, using (r, c)
        r, c = s.pop()

        if not visited[r][c]:
            visited[r][c] = True

            for neighbor in get_neighbors(r, c, islands):
                s.push(neighbor)


def get_neighbors(row, col, islands):
    # return list of neighbors
    neighbors = []

    # check north
    if islands[row - 1][col] == 1:
        neighbors.append((row - 1, col))

    # check sound
    if islands[row + 1][col] == 1:
        neighbors.append((row + 1, col))

    # check west
    if islands[row][col - 1] == 1:
        neighbors.append((row, col - 1))

    # check east
    if islands[row][col + 1] == 1:
        neighbors.append((row, col + 1))


island_counter(islands)
print(island_counter(islands))
