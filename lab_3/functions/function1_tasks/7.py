def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]== 3:
            return True
    return False

print(has_33([1,3,3]))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.