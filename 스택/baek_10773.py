n = int(input())

stack = []

for _ in range(n):
    command = int(input())
    if command != 0:
        stack.append(command)
    else:
        stack.pop()
print(sum(stack))