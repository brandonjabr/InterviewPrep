# For strings
def permutations_string(word):
    if len(word) == 1:
        return [word]
 
    #get all permutations of length N-1
    perms = permutations_string(word[1:])
    char = word[0]
    result = []
    
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

# For arrays
def permutations_array(nums):
    if len(nums) == 1:
        return [nums]

    x = nums[0]
    perms = permutations_array(nums[1:])
    out = []
    for perm in perms:
        for i in range(len(perm)+1):
            out.append(perm[:i] + [x] + perm[i:])
    return out

a = [1,2,3]
s = 'yew'
print permutations_array(a)
print permutations_string(s)