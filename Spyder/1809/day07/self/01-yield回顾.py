

def f1():
    print("启动生成器")
    for n in range(3):
        yield n
    print('生成器结束')


g1 = f1()

while True:
    try:
        print(next(g1))
    except Exception as e:
        print('循环结束', e)
        break

for i in g1:
    print(i)
