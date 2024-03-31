def selection_sort(nums):
    for index in range(len(nums)):
        smallest_index = index
        for i in range(smallest_index + 1, len(nums)):
            if nums[i] < nums[smallest_index]:
                smallest_index = i
        nums[index], nums[smallest_index] = nums[smallest_index], nums[index]
    return nums
