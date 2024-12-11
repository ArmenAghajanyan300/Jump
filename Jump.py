def jump_search(arr, target):

    n = len(arr)
    step = int(n ** 0.5)

    prev = 0
 
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1

 
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1 


# Example usage
array = [2, 4, 8, 12, 16, 18, 20, 24, 28, 32, 36, 40, 44]
target = int(input("Enter the number to search: "))

index = jump_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
