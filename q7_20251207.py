def file_read(pathname):
    with open(pathname) as f:
        input_file = f.read().splitlines()
    return input_file


def find_character_index(s, ch):
    return [k for k, ltr in enumerate(s) if ltr == ch]


def insert_character(s, c, pos):
    # Insert character at specified position
    return s[:pos] + c + s[pos+1:]


def put_dash_and_count(mymap):
    start_pos = find_character_index(mymap[0], 'S')
    mymap[1] = insert_character(mymap[1], '|', start_pos[0])
    hit_count = 0
    index_range = [x for x in range(2, len(mymap)-1) if x % 2 == 0]

    for j in index_range:
        beam_index = find_character_index(mymap[j-1], '|')
        block_index = find_character_index(mymap[j], '^')
        hit_index = list(set(beam_index).intersection(set(block_index)))
        non_hit_index = list(set(beam_index).difference(set(hit_index)))
        hit_count = hit_count + len(hit_index)
        # insert beams
        for k in hit_index:
            mymap[j+1] = insert_character(mymap[j+1], '|', k - 1)
            mymap[j+1] = insert_character(mymap[j+1], '|', k + 1)

        for k in non_hit_index:
            mymap[j+1] = insert_character(mymap[j+1], '|', k)

    return hit_count


# Python Code to find count of paths between
# two vertices of a directed graph using DFS
def dfs(node, dest, graph, visited, count):

    # If destination is reached,
    # increment count
    if node == dest:
        count[0] += 1
        return

    # Mark current node as visited
    visited[node] = True

    # Explore all unvisited neighbors
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, dest, graph, visited, count)

    # Backtrack: unmark the node
    # before returning
    visited[node] = False


def countPaths(n, edgeList, source, destination):

    # Create adjacency list(1 - based indexing)
    graph = [[] for _ in range(n + 1)]
    for u, v in edgeList:
        graph[u].append(v)

    # Track visited nodes
    visited = [False] * (n + 1)
    count = [0]

    # Start DFS from source
    dfs(source, destination, graph, visited, count)

    return count[0]

def extract_path_count(edge_list, node_list):
    n = 5

    # Edge list: [u, v] represents u -> v
    edgeList = [
        [1, 2], [1, 3], [1, 5],
        [2, 5], [2, 4], [3, 5], [4, 3]
    ]

    source = 1
    destination = 5

    print(countPaths(n, edgeList, source, destination))