# find 연산
def find(target):
    if target == parent[target]:
        return target
 
    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]
 
# union 연산
def union(a, b):
    a = find(a)
    b = find(b)
 
    # 작은 루트 노드를 기준으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 
parent = [0, 1, 2, 3, 4, 5]

union(3, 5)
print(parent)
union(1, 5)
print(parent)
union(1, 5)
print(parent)

