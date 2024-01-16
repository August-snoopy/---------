def main():
    n = input("输入被删减的数字n:")  # 输入n
    if n[0] == '-' or n == '0':  # 判断n是否为负数或者为0
        print("n 不是正数!")  # 输出n不是正整数
        return
    k = int(input("输入删减位数 k:"))  # 输入k
    if len(n) <= k:  # 判断n的长度是否小于等于k
        print("删的太多了!")  # 输出没有足够的数字
        return
    ans = []
    while k > 0 and len(n) > k:
        min_index = min(range(k+1), key=n.__getitem__)
        ans.append(n[min_index])
        n = n[min_index+1:]
        k -= min_index
    ans += list(n)
    ans = ''.join(ans).lstrip('0')
    print(ans)

if __name__ == "__main__":
    main()