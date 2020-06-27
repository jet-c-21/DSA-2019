# coding: utf-8

'''
author : Jet Vayne
date: 2019-10-28
'''


class Solution(object):
    # 程式主要動作控制區
    def heap_sort(self, nums):
        result = []  # 最終要輸出的排過的 list
        self.heapify(nums)  # 先將輸入的 list 變成 heap 結構
        while len(nums) != 0:  # 迴圈控制丟出 root 做 sort 的動作
            result.append(nums.pop(0))  # 將剛剛丟出的 root append 到最終結果 list 裡面
            self.heapify(nums)  # 此時，少了一個 element 的 list 不見得是heap結構了，所以我們再重新將它整理成 heap 結構，並重複上述動作

        return result  # 回傳最終結果

    # 將輸入的 list 變成 heap 結構，heap型態為 min heap
    def heapify(self, array: list):
        for i in reversed(range(len(array))):  # 使用 reverse 將 index 由大到小 iter
            self.climber(i, array)  # 透過 index 往上找 parent ，並做值的比較，必要時會換值

    # 由下往上爬取數值，並比較 self(child) and parent
    def climber(self, index: int, array: list):
        pi = self.get_pix(index)  # 取得 parent index
        if pi is None:
            return

        self_val = array[index]  # 自己的值
        par_val = array[pi]  # parent 的值

        # 若 parent 的值大於 自己的值，則做 index 換值的動作
        if par_val > self_val:
            array[index] = par_val
            array[pi] = self_val

        self.climber(pi, array)  # check parent 和它的 parent 是否也符合 heap 結構，並用 recursive 去實現

    # tool-function，回傳該 index 的 parent index
    def get_pix(self, index: int):
        if index <= 0:
            return
        return int((index + 1) / 2 - 1)

