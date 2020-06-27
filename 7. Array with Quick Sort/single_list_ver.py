class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        self.quick_sort(nums)

    #   ���������O���^β index ����, ��ֻ input ���ϣ��A�O����^��β
    def quick_sort(self, sequence: list, start_index=None, end_index=None):
        # default
        if start_index is None and end_index is None:
            start_index = 0
            end_index = len(sequence) - 1
        # ֻ�O���^
        elif start_index and end_index is None:
            end_index = len(sequence) - 1
        # ֻ�O��β
        elif end_index and start_index is None:
            start_index = 0

        self.sorter(sequence, start_index, end_index)

    def sorter(self, sequence, left_index, right_index):
        if left_index >= right_index:
            return

        # �S�Cȡ pivot
        median_index = (left_index + right_index) // 2  # // �ɘ�ȥС��
        pivot = sequence[median_index]

        # �ҵ��ؔ��c��֮��Ҫ�����Ҷ�
        partition = self.get_partition(sequence, left_index, right_index, pivot)
        # print(partition, sequence[partition], pivot)

        # ���
        self.sorter(sequence, left_index, partition - 1)

        # �Ҷ�
        self.sorter(sequence, partition, right_index)

    def get_partition(self, sequence, left_index, right_index, pivot):
        while left_index <= right_index:
            '''
            ��߅��Փ��Ҫ�� pivot С�� ���� while �O array[left] < pivot
            ��������߅���� index �� pivot �����^
            '''
            while sequence[left_index] < pivot:
                left_index += 1

            '''
            ��߅��Փ��Ҫ�� pivot �� ���� while �O array[right] > pivot
            ��������߅�f�p index �� pivot �����^
            '''
            while sequence[right_index] > pivot:
                right_index -= 1

            # ���Qλ����
            if left_index <= right_index:
                temp = sequence[left_index]
                sequence[left_index] = sequence[right_index]
                sequence[right_index] = temp
                left_index += 1
                right_index -= 1

        return left_index
