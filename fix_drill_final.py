with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update source display format in showDrillDown (the matched data branch)
# Current: '... 数据来源：'+d.source
# Target: '... 来源系统：'+d.source
old_line = "document.getElementById('modalSource').innerHTML='<iconify-icon icon=\"mdi:file-excel\" style=\"vertical-align:middle;color:#52c41a;\"></iconify-icon> 数据来源：'+d.source;"
new_line = "document.getElementById('modalSource').innerHTML='<iconify-icon icon=\"mdi:file-excel\" style=\"vertical-align:middle;color:#52c41a;\"></iconify-icon> '+d.source;"
if old_line in c:
    c = c.replace(old_line, new_line)
    print('Updated source format in showDrillDown')

# Update all drillData source values to "系统 | 表" format
c = c.replace(
    "source:'财务系统 · 经营收入明细表'",
    "source:'来源：财务系统 | 经营收入明细表'"
)

# Fix hotel drill source
c = c.replace(
    "source:'酒店PMS系统'",
    "source:'来源：酒店PMS系统 | 酒店经营日报'"
)

# Fix property drill source if exists
c = c.replace(
    "source:'物业管理系统'",
    "source:'来源：物业管理系统 | 物业费明细表'"
)

# Fix any remaining source patterns
c = c.replace(
    "source:'经营看板_指标维度汇总.xlsx'",
    "source:'来源：财务系统 | 指标维度汇总表'"
)

c = c.replace(
    "source:'人力统计.xlsx'",
    "source:'来源：人力资源系统 | 在职人员表'"
)

# Fix the fallback source
c = c.replace(
    "来源系统：财务系统 | 来源表：经营收入月度明细表",
    "来源：财务系统 | 经营收入月度明细表"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done')
