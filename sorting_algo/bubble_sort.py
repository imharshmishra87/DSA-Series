def bubble_sort(nums: list) -> list:
    print(f"Original array : {nums}")

    for pass_num in range(len(nums) - 1):
        stop_point = len(nums) - 1 - pass_num
        is_swap = False
        for i in range(stop_point):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_swap = True
        if is_swap == False:
            break
        print(f"Each successfull pass aray is :{nums}")

    return nums


print(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8]))

"""Best Case o(N) , Worst Case and Average case is o(n**2)"""
