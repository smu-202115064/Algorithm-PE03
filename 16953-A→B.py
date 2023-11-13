A, B = map(int, input().split())

stack = [(A,1)]
answer = -1

while stack:
    node, depth = stack.pop()
    if node > B:
        continue
    if node == B:
        answer = depth
        break
    stack.append((10*node+1, depth+1))
    stack.append((2*node, depth+1))

print(answer)
