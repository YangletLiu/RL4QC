import ast
# 从txt文件中读取contraction_ordering
file_path = "N53M12.txt"
# file_path = "N53M14.txt"
# file_path = "N53M16.txt"
# file_path = "N53M18.txt"
# file_path = "N53M20.txt"


with open(file_path, 'r') as file:
    content = file.read()
    contraction_ordering = ast.literal_eval(content)

count = 0

# 遍历所有可能的组合
i = 0
while i < len(contraction_ordering) - 2:
    order1 = contraction_ordering[i]
    order2 = contraction_ordering[i + 1]
    order3 = contraction_ordering[i + 2]

    a1, b1 = order1
    c1, d1 = order2
    e1, f1 = order3

    # 检查是否满足条件
    if ((a1 == e1 or b1 == e1) and (c1 == f1 or d1 == f1)):
        # 打印满足条件的组
        print(f"符合条件的组 {count + 1}:")
        print(order1)
        print(order2)
        print(order3)
        count += 1

    i += 1

print(f"共找到{count}组满足条件的收缩对。")
