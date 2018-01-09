'''20180108@keyber
    目的:不用key code跟第三方就能视化DB
    把DB展开的工具的简易可视化工具，只用内建的sqlite3，不需要其他轮子
	DB路径可以把DB file直接拖拉到console
        DB
        |_TAble
        |_Table
            |__data
    '''
    
import sqlite3 as lite

#读取db path，顺便去掉"符号
mydb = input('''2018018@keyber\n\n#enter db full path : \n''')
if mydb[0] == '"':
    mydb = mydb[1:-1]

#把DB的table名称刷成list
conn = lite.Connection(mydb)
cur = conn.cursor()
rawlist = list(cur.execute('''SELECT name FROM sqlite_master WHERE type='table' '''))
conn.commit

#把list show出来
count = 0
print("\nDB")
for i in rawlist:
    print('|__',format(count),' = ',format(i))
    count += 1

#用数字选择table
num = input("\n\n#enter number(=0): ")
if num == "":
    num = 0
rawtable = str(rawlist[int(num)])
thetable = str(rawtable[2:-3])

#组sql码，开始从table倒资料出来，可视化 看架构不需要刷太多 20差不多
cmd = "select * from " + thetable + " LIMIT 20"
data = list(conn.execute(cmd))

#把资料show出来
count = 1
for i in data:
    print(format(count),':',format(i))
    count += 1

raw = input("\n--press enter to leave--")


