import copy

n = 10
a = [1, 3, 5, 7, 4, 2, 8, 4, 9, 9]
b = [1.5, 2, 6, 8, 2, 1, 3, 8, 11, 4]

def gettime(arr):
    return sum([x[1] for x in arr])

# 计算每个零件在两台机器上的处理时间差，并排序
parts = sorted([(a[i] - b[i], i) for i in range(n)])

# 分配零件
order_a = []
order_b = []
for diff, i in parts:
    if diff > 0:
        order_b.append((i+1, a[i]))
    else:
        order_a.append((i+1, b[i]))
# 逆序 order_a
order_a.reverse()

time_a = gettime(order_a)
time_b = gettime(order_b)
# 计算结果
res = max(time_a, time_b)
print("非优化情况下最短完成时间：", res)
print("非优化情况下机器A处理的零件顺序：", [x[0] for x in order_a])
print("非优化情况下机器B处理的零件顺序：", [x[0] for x in order_b])
# 初始化一个新的 order_a 和 order_b
new_order_a = []
new_order_b = []


for i in range(len(order_a)):
    # 创建 order_a 和 order_b 的深拷贝
    new_order_a = copy.deepcopy(order_a)
    new_order_b = copy.deepcopy(order_b)
    # 交换零件
    new_order_a[i], new_order_b[i] = new_order_b[i], new_order_a[i]
    # 将 new_order_a 中的元素 (i, b[i]) 替换为 (i, a[i])
    new_order_a = [(j, a[j-1]) for j, _ in new_order_a]
    # 将 new_order_b 中的元素 (i, a[i]) 替换为 (i, b[i])    
    new_order_b = [(z, b[z-1]) for z, _ in new_order_b]
    # 计算时间
    new_time_a = gettime(new_order_a)
    new_time_b = gettime(new_order_b)
    # 更新结果
    if max(new_time_a, new_time_b) < res:
        res = max(new_time_a, new_time_b)
        order_a = new_order_a
        order_b = new_order_b
time_a = gettime(order_a)
time_b = gettime(order_b)   
print("最短完成时间：", res)
print("机器A处理的零件顺序：", [x[0] for x in order_a])
print("A完成时间：", time_a)
print("机器B处理的零件顺序：", [x[0] for x in order_b])
print("B完成时间：", time_b)