def binarysearch( arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        left = binarysearch(arr, 0, mid, target)
        return left
    else:
        right = binarysearch(arr, mid, high, target)
        return right
    return -1


def search( nums, target):
    element = binarysearch(nums, 0, len(nums) - 1, target)
    return element

print(search([-1,0,3,5,9,12],9))