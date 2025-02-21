def spy_game(nums):
    for i in range(len(nums)-1):
        if nums[i:i+3] == [0, 0, 7]:
            return True
    return False

print(spy_game([1,3,0,0,7]))

#Write a function that takes in a list of integers and returns True if it contains 007 in order