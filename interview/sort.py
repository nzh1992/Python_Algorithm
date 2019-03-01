"""
created by nzh
Date: 2019/2/28 12:16 AM
"""


# 排序常见算法练习

# 1.选择排序
# 思路：搜索列表找到最小项的位置，如果这个位置不是列表的第一个位置，那么就会交换这两项的位置。
# 然后回到第二个位置，重复这个过程。
# 复杂度：O(n²)
def select_sort(l):
    """
    选择排序
    :param l: list
    :return: 升序list
    """
    i = 0
    while i < len(l) - 1:
        min_index = i
        j = i + 1
        while j < len(l):
            if l[j] < l[min_index]:
                min_index = j

            j += 1

        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]

        i += 1


# 2. 冒泡排序
# 思路：依次比较相邻两项，如果右侧小于左侧则交换位置，否则不变。
# 复杂度：O(n²)
def bubble_sort(l):
    """
    冒泡排序
    :param l: list
    :return: 升序list
    """
    n = len(l)
    while n > 1:
        i = 1
        while i < n:
            if l[i] < l[i - 1]:
                l[i], l[i - 1] = l[i - 1], l[i]

            i += 1

        n -= 1


l = [5, 3, 1, 2, 4]
bubble_sort(l)
print(l)
