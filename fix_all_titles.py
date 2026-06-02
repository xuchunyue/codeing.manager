import os, re

pages = {
    'hr.html': '人力管理看板',
    'property.html': '物业管理看板',
    'hotel.html': '楼宇运营看板',
    'hotel-management.html': '酒店管理看板',
    'taxi.html': '出租车管理看板',
}

for filename, old_title_text in pages.items():
    if not os.path.exists(filename):
        print(f'Skip (not found): {filename}')
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old = f'<h1 class="topbar-title">{old_title_text}</h1>'
    new = f'<h1 class="topbar-title">{old_title_text}<span style="font-size:12px;color:#8c8c8c;font-weight:400;margin-left:8px;">每日更新</span></h1>'
    
    if old in content:
        content = content.replace(old, new)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filename} - {old_title_text}')
    else:
        print(f'Pattern not found in: {filename}')

print('Done')
