# 백준 4195 친구 네트워크 - Find_Union 문제

import sys

def find(target):
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    a = find(a)
    b = find(b)

    # 이미 union을 한번 진행한 경우 다시 union을 진행할 경우 예시 (A <- B <- C => A -> B <- C) 
    if a == b:
        return
    else:
        parent[b] = a
        visited[a] += visited[b]

t = int(sys.stdin.readline())
for _ in range(t):
    parent = dict()
    visited = dict()

    t = int(sys.stdin.readline())
    for i in range(t):
        a,b = map(str, sys.stdin.readline().split())

        if a not in parent:
            parent[a] = a
            visited[a] = 1
        
        if b not in parent:
            parent[b] = b
            visited[b] = 1

        union(a,b)

        print(visited[find(a)])
