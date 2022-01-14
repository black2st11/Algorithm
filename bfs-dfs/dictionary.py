import sys
from collections import defaultdict


def dfs(vertex):
    global flag
    visited[vertex] = False

    adjacent = graph[vertex]

    for node in adjacent:
        if visited[node] is False:
            flag = False

        elif visited[node] is None:
            dfs(node)
    
    sequence.append(vertex)
    visited[vertex] = True


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    
    graph = defaultdict(set)
    N = int(sys.stdin.readline().rstrip())
    words = []
    visited = {}
    for _ in range(N):
        words.append(sys.stdin.readline().rstrip())

    # make graph
    prev = ""
    for word in words:

        for i in range(min(len(prev), len(word))):
            if prev[i] != word[i]:
                graph[prev[i]].add(word[i])
                visited[prev[i]] = None
                visited[word[i]] = None
                break
        
        prev = word
    print(graph)
    # dfs all
    answer = []
    for vertex in visited.keys():
        if visited[vertex] is None:
            sequence = []
            flag = True

            dfs(vertex)

            if flag:
                answer.extend(sequence)
            else:
                break
    print(visited)
    if flag:
        alphabet = [a if a not in answer else "" for a in "abcdefghijklmnopqrstuvwxyz"]
        answer.reverse()
        answer = "".join(answer +alphabet)
        print(answer)
    else:
        print("INVALID HYPOTHESIS")