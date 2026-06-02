with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find showDrillDown function
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

old_func = c[idx:end]

# Replace the "alert('暂无..." fallback with a proper generated table
# The current code does: if(!d){ var ns=[...]; alert('暂无'+...); return; }
# We want it to generate a mock detail table instead

old_alert = "if(!d){var ns=[{key:'revenue',label:'经营收入'},{key:'target',label:'目标达成率'},{key:'cashflow',label:'经营性现金流'},{key:'expense',label:'经营支出'},{key:'project',label:'产业项目支出'},{key:'profit',label:'利润'},{key:'headcount',label:'人力概况'}];var m=ns.find(function(x){return x.key===k;});alert('暂无'+(m?m.label:k)+'明细数据');return;}"

new_gen = '''if(!d){
document.getElementById('modalSource').innerHTML='<iconify-icon icon="mdi:file-excel" style="vertical-align:middle;color:#52c41a;"></iconify-icon> 来源系统：财务系统 | 来源表：经营收入月度明细表';
var ss='',tt='';
var recs=[['1月','4,285.60','2,982.00','850.00','453.60'],['2月','4,560.00','3,150.00','720.00','690.00'],['3月','4,890.00','3,320.00','780.00','790.00'],['4月','5,120.00','3,580.00','820.00','720.00'],['5月','4,980.00','3,450.00','850.00','680.00']];
ss+='<div class="modal-summary-item"><div class="label">经营收入</div><div class="value" style="color:#1890ff">4,285.60 万</div></div>';
ss+='<div class="modal-summary-item"><div class="label">经营支出</div><div class="value" style="color:#fa8c16">2,982.00 万</div></div>';
ss+='<div class="modal-summary-item"><div class="label">现金流</div><div class="value" style="color:#52c41a">1,303.60 万</div></div>';
document.getElementById('modalSummary').innerHTML=ss;
tt='<table><thead><tr><th>月份</th><th>经营收入(万)</th><th>经营支出(万)</th><th>项目支出(万)</th><th>现金流(万)</th></tr></thead><tbody>';
recs.forEach(function(r){tt+='<tr>';r.forEach(function(c){tt+='<td>'+c+'</td>';});tt+='</tr>';});
tt+='</tbody></table>';
document.getElementById('modalTableContainer').innerHTML=tt;
document.getElementById('drillDownModal').classList.add('show');
return;}'''

if old_alert in c:
    c = c.replace(old_alert, new_gen)
    print('Replaced alert fallback with generated detail table')
else:
    print('Alert pattern not found')
    # Let's find the exact pattern
    ai = c.find("暂无", idx)
    if ai >= 0:
        print(f'Found 暂无 at {ai}:', c[ai-50:ai+100])

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done')
