# 定义一个函数来打印数独的当前状态
def print_sudoku(sudoku):
    for row in sudoku:  # 遍历数独的每一行
        print(" ".join(str(num) for num in row))  # 将每一行的数字转为字符串并用空格连接，然后打印
    exit(0)  # 打印完数独后结束程序

# 定义一个函数来记录数独中某个位置的数字
def record(x, y, rows, cols, boxes, sudoku):
    num = sudoku[x][y]  # 获取数独中位置 (x, y) 的数字
    # 在行、列和宫的记录数组中标记该数字
    rows[x][num] = cols[y][num] = boxes[(x//3)*3 + y//3][num] = 1

# 定义一个函数来取消记录数独中某个位置的数字
def derecord(x, y, rows, cols, boxes, sudoku):
    num = sudoku[x][y]  # 获取数独中位置 (x, y) 的数字
    # 在行、列和宫的记录数组中取消标记该数字
    rows[x][num] = cols[y][num] = boxes[(x//3)*3 + y//3][num] = 0
    sudoku[x][y] = 0  # 将数独中位置 (x, y) 的数字清零

# 定义一个函数来使用深度优先搜索解决数独
def dfs(x=0, y=0, rows=None, cols=None, boxes=None, sudoku=None):
    if sudoku[x][y] != 0:  # 如果数独中位置 (x, y) 的数字已经确定
        if x == 8 and y == 8:  # 如果已经到达数独的最后一个位置
            print_sudoku(sudoku)  # 打印数独
        elif y == 8:  # 如果已经到达当前行的最后一个位置
            dfs(x+1, 0, rows, cols, boxes, sudoku)  # 移动到下一行的第一个位置
        else:  # 如果还没有到达当前行的最后一个位置
            dfs(x, y+1, rows, cols, boxes, sudoku)  # 移动到当前行的下一个位置
    else:  # 如果数独中位置 (x, y) 的数字还没有确定
        for num in range(1, 10):  # 遍历所有可能的数字
            # 如果该数字在当前位置的行、列和宫中都没有出现过
            if not rows[x][num] and not cols[y][num] and not boxes[(x//3)*3 + y//3][num]:
                sudoku[x][y] = num  # 将该数字填入数独中的当前位置
                record(x, y, rows, cols, boxes, sudoku)  # 记录该数字
                if x == 8 and y == 8:  # 如果已经到达数独的最后一个位置
                    print_sudoku(sudoku)  # 打印数独
                elif y == 8:  # 如果已经到达当前行的最后一个位置
                    dfs(x+1, 0, rows, cols, boxes, sudoku)  # 移动到下一行的第一个位置
                else:  # 如果还没有到达当前行的最后一个位置
                    dfs(x, y+1, rows, cols, boxes, sudoku)  # 移动到当前行的下一个位置
                derecord(x, y, rows, cols, boxes, sudoku)  # 取消记录该数字
        return  # 如果所有的数字都试过了，返回上一层

# 初始化数独、行、列和宫的记录数组
sudoku = [[0] * 9 for _ in range(9)]  # 创建一个 9x9 的二维数组来存储数独的状态，初始状态为全 0
rows = [[0] * 10 for _ in range(10)]  # 创建一个 10x10 的二维数组来记录每一行的数字，初始状态为全 0
cols = [[0] * 10 for _ in range(10)]  # 创建一个 10x10 的二维数组来记录每一列的数字，初始状态为全 0
boxes = [[0] * 10 for _ in range(10)]  # 创建一个 10x10 的二维数组来记录每一宫的数字，初始状态为全 0

# 从 txt 文件中读取数独初始状态，并记录已有数字
with open('sudoku.txt', 'r') as f:
    for i, line in enumerate(f):  # 遍历文件的每一行
        row = list(map(int, line.split()))  # 将每一行的数字分割并转换为整数
        for j, num in enumerate(row):  # 遍历每一行的每一个数字
            sudoku[i][j] = num  # 设置当前位置的数字
            if num != 0:  # 如果当前位置的数字不为 0
                record(i, j, rows, cols, boxes, sudoku)  # 记录当前位置的数字

# 调用深度优先搜索解决数独
dfs(rows=rows, cols=cols, boxes=boxes, sudoku=sudoku)  # 使用深度优先搜索算法解决数独
print("该数独无解")  # 如果数独无解，打印提示信息

