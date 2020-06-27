# coding: utf-8

'''
author: Jet Vayne
date: 2019-11-03
'''


class Solution(object):
    # 程式主要動作控制區
    def merge_sort(self, nums: list):
        start_index = 0
        end_index = len(nums) - 1

        # 建立 sorter 來幫我從最小段的 sub-list 的大小排列， 從 index 0 到最後一個 index
        self.sorter(nums, start_index, end_index)

        return nums  # 回傳最終 sort 完的結果

    # 遞迴切分出 sub-list
    def sorter(self, array: list, start_index: int, end_index: int):
        curr_mid = (start_index + end_index) // 2  # 目前對於現在的 sub-list 的中心 index

        if start_index < end_index:  # 給定一個讓 recursive 能夠跳脫的機制，也讓之後的連續兩行遞迴可以不受第二行 sorter 呼叫的影響，輕鬆跳脫
            # 這裡使用連兩行的遞迴寫法，完美的切出相同層級的 sub-list
            self.sorter(array, start_index, curr_mid)  # 左半部 sub-list 的切分
            self.sorter(array, curr_mid + 1, end_index)  # 右半部 sub-list 的切分，這個 +1 我覺得我攝得很好，能夠完美搭配上方的 if case

            # 執行到這就開始執行該圈的 sub-list 合併動作
            self.merge(array, start_index, curr_mid, end_index)

    # 比值、合併、換值區
    def merge(self, array: list, start: int, mid: int, end: int):
        result = []  # 最後 merge 完應該長成如何的指標，我用一個 list 存起來
        target_len = end - start + 1  # 該次要表定要 merge 的 element 數量
        left_list = []  # 左半部 sub-list 元素暫存區
        right_list = []  # 右半部 sub-list 元素暫存區

        # 裝填左半部 sub-list 元素
        for i in range(start, mid + 1):
            left_list.append(array[i])

        # 裝填右半部 sub-list 元素
        for i in range(mid + 1, end + 1):
            right_list.append(array[i])

        while len(result) != target_len:  # 確實讓 result 的長度達標，才停止
            # 若 right_list 元素丟完， 直接丟 left_list 元素
            if len(right_list) == 0 and len(left_list) != 0:
                result.append(left_list.pop(0))
                continue
            # 若 left_list 元素丟完， 直接丟 right_list 元素
            if len(left_list) == 0 and len(right_list) != 0:
                result.append(right_list.pop(0))
                continue

            # left_list 和 right_list 都還有元素的情況下，要做比值的動作
            if len(left_list) != 0 and len(right_list) != 0:
                # 由於從最小單位的 sub-list 開始 merge，所以各個 sub-list 都會是 sorted，直接做比值丟值即可達成 sort
                if left_list[0] <= right_list[0]:  # 若 left_list[0] <= right_list[0]，將 left_list[0] 丟入 result
                    result.append(left_list.pop(0))

                # 若 right_list[0] < left_list[0]，將 right_list[0] 丟入 result
                else:
                    result.append(right_list.pop(0))

        # 此時 result 是我們想要的元素分布狀態了，找到這次的 merge 任務對於原本的 array 來說是哪個 index 開始，哪個 index 結束
        for i in range(start, end + 1):
            array[i] = result.pop(0)  # 將 array 對應的 index 換成 result 的值
