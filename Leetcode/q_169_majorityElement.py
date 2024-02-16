def majorityElement(nums) -> int:
    count = 1
    element = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == element:
            count += 1
        else:
            count -= 1
            if count == 0:
                element = nums[i]
                count = 1
    return element


'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element 
always exists in the array.
'''
