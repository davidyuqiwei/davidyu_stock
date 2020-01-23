strs = []
sql1_str = []


for i in range(1,94):
    strs.append('x'+str(i))
    sql1_str.append("avg("+"a.x"+str(i)+")"+' as '+'x'+str(i)+',')

sql1_str[-1] = sql1_str[-1].replace(',','')
t1 = 'select a.x94, \n' +''.join(sql1_str)
#print(t1)

add_str = ' from \n' +'('+'\n'
ss1 = 'select x94,'+'\n'
ss = []
for k in strs:
    ss.append('case %s when -9999 then NULL ELSE %s end as %s'%(k,k,k)+',\n')
ss[-1] = ss[-1].replace(',','')
group_str='group by a.x94;'


s1 =t1+add_str+ ss1+''.join(ss)+'from stock_dev.fin_report'+'\n'+') a'+'\n'+group_str
print(s1)
