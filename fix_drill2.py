with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find showDrillDown function and the source line
idx = c.find("function showDrillDown(")
depth = 0
end = idx
for i in range(idx, len(c)):
    if c[i] == '{': depth += 1
    elif c[i] == '}':
        depth -= 1
        if depth == 0:
            end = i + 1
            break

func = c[idx:end]
print(func)
