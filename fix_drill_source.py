with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update drill data source labels
c = c.replace(
    "source:'财务系统'",
    "source:'财务系统 · 经营收入明细表'"
)

# Update the showDrillDown modal source display to include system name
# Find the source display line in showDrillDown
old_src = "document.getElementById('modalSource').innerHTML='来源：'+(sourceMap[key]||'系统明细表');"
new_src = "var sm=sourceMap[key]||'系统明细表';document.getElementById('modalSource').innerHTML='<iconify-icon icon=\"mdi:file-excel\" style=\"vertical-align:middle;color:#52c41a;\"></iconify-icon> 来源系统：'+sm+' | 来源表：'+sm;"
if old_src in c:
    c = c.replace(old_src, new_src)
    print('Updated modal source display')
else:
    # Try to find the source line
    idx = c.find("modalSource")
    if idx >= 0:
        print('Found modalSource at', idx)
        print(c[idx:idx+200])

# Also fix the fallback source I added earlier
c = c.replace(
    "来源系统：财务系统 | 来源表：经营收入月度明细表",
    "来源系统：财务系统 | 来源表：经营收入月度明细表"  # already correct
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done')
