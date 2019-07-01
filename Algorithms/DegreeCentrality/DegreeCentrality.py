def degree_centrality(adj_mat, index):
    count = 0
    for p in range(number_nodes):
        if adj_mat[index][p] == 1:
            count = count + 1
    return count


def print_centrality(adj_mat):
    for n in range(number_nodes):
        print(str(degree_centrality(adj_mat, n)) + "\n")
    return None


first_line = input()
first_line = first_line.split()
number_nodes = int(first_line[0])
number_edges = int(first_line[1])
adj_matrix = [[0 for x in range(number_nodes)] for y in range(number_nodes)]

for i in range(number_edges):
    my_line = input()
    my_line = my_line.split()
    my_line = [int(i) for i in (my_line)]
    adj_matrix[my_line[0]][my_line[1]] = 1
    adj_matrix[my_line[1]][my_line[0]]= 1
    i = i + 1

print_centrality(adj_matrix)
