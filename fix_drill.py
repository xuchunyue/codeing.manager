with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the showDrillDown function
idx = c.find('function showDrillDown(')
# Find the "暂无" alert section
alert_idx = c.find("alert('暂无", idx)
if alert_idx >= 0 and alert_idx < idx + 500:
    # Find the alert block
    start = c.rfind('else{', 0, alert_idx + 500)
    if start > 0:
        start = c.rfind('{', 0, alert_idx + 200) + 1
        # Find matching }
        depth = 1
        end = start
        for i in range(start, len(c)):
            if c[i] == '{': depth += 1
            elif c[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i
                    break
        print(f'Alert block at {start} to {end}')
        print(c[start:end])

# Find drillData definition
idx2 = c.find('const drillData={')
if idx2 >= 0:
    # Find the end of drillData
    depth = 0
    end2 = idx2
    for i in range(idx2, len(c)):
        if c[i] == '{': depth += 1
        elif c[i] == '}':
            depth -= 1
            if depth == 0:
                end2 = i + 1
                break
    print(f'\ndrillData at {idx2} to {end2}, length={end2-idx2}')
    # Print first 500 chars
    print(c[idx2:idx2+500])
