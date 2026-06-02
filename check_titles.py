import re
for f in ['hr.html','taxi.html']:
    with open(f,'r',encoding='utf-8') as fp:
        c = fp.read()
    m = re.findall(r'<h1 class="topbar-title">[^<]*</h1>', c)
    for x in m:
        print(f'{f}: {x}')
