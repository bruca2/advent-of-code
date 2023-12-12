m = {}
def dfs(spr, nums):
    if not spr:
        return 1 if not nums else 0
    if not nums:
        return 0 if "#" in spr else 1
    result = 0

    key = (spr,nums)
    if  key in m:
        return m[key]

    #assume spring is good, so count it and continue to next spring
    if spr[0] in ".?":
        result += dfs(spr[1:], nums)
        
    #assume spring is bad, so check if the damaged block is valid
    #if it's valid, count it and go to next spring (after the block) and next block 
    if spr[0] in "#?":
        if nums[0] <= len(spr) and "." not in spr[:nums[0]] and (nums[0] == len(spr) or spr[nums[0]] != "#"):
            result += dfs(spr[nums[0]+1:], nums[1:])

    m[key] = result
    return result

def run():
    total1 = total2 = 0
    lines = open('input12.txt', 'r').read().splitlines()   
    for line in lines:
        spr,nums = line.split()
        nums = tuple(int(n) for n in nums.split(','))
        total1 += dfs(spr, nums)        
        nums *= 5
        spr = '?'.join([spr]*5)        
        total2 += dfs(spr, nums)   
    print(total1)
    print(total2)




