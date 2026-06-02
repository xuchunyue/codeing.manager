import os

fixes = {
    'hr.html': ('<h1 class="topbar-title">人力运营看板</h1>', '<h1 class="topbar-title">人力运营看板<span style="font-size:12px;color:#8c8c8c;font-weight:400;margin-left:8px;">每日更新</span></h1>'),
    'taxi.html': ('<h1 class="topbar-title">出租车看板</h1>', '<h1 class="topbar-title">出租车看板<span style="font-size:12px;color:#8c8c8c;font-weight:400;margin-left:8px;">每日更新</span></h1>'),
}

for f, (old, new) in fixes.items():
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if old in c:
        c = c.replace(old, new)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f'Updated: {f}')
    else:
        print(f'Not found: {f}')
print('Done')
