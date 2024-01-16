# 定义一个函数用于显示比赛日程表
def display(table, n):
    print("比赛日程表：")
    for i in range(n):
        for j in range(n):
            print(table[i][j], end=" ")
            if j == 0:
                print("|", end=" ")
        print()

def table(k, d):
    # 是否是最初条件
    if k == d:
        return
    for i in range(d):
        for j in range(d):
            a[i + d][j + d] = a[i][j]
            a[i][j + d] = a[i][j] + d
            a[i + d][j] = a[i][j] + d
    table(k, d * 2)

if __name__ == "__main__":
    # 输入人数
    n = int(input("学生人数k=2^n,请输入k:"))
    k = 2 ** n
    # 初始化一个全零的二维数组
    a = [[0 for _ in range(k)] for _ in range(k)]
    # 初始化并判断是否只有一个人参赛
    if k == 1:
        a[0][0] = 0
    else:
        a[0][0] = 1
    # 递归
    table(k, 1)
    # 输出
    display(a, k)