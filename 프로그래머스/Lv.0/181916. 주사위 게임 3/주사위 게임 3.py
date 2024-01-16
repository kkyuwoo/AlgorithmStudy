def solution(a, b, c, d):
    answer = 0
    nums = [0] * 7
    nums[a] += 1
    nums[b] += 1
    nums[c] += 1
    nums[d] += 1
    if 4 in nums:
        answer = nums.index(4) * 1111
    elif 3 in nums:
        answer = (nums.index(3) * 10 + nums.index(1))**2
    elif 2 in nums:
        if nums.count(2) == 2:
            for i in range(len(nums)):
                if nums[i] == 2:
                    p = i
                    break
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == 2:
                    q = i
                    break
            answer = (p + q) * abs(p-q)
        else:
            p = nums.index(2)
            for i in range(len(nums)):
                if nums[i] == 1:
                    q = i
                    break
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == 1:
                    r = i
                    break
            answer = q * r
    if nums.count(1) == 4:
        for i in range(len(nums)):
            if nums[i] == 1:
                answer = i
                break
    return answer