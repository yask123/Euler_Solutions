def permutations(items):
 
    # terminal
    if len(items) == 2:
        return [''.join(items), ''.join(items[::-1])]
 
    # iteration
    result = []
    for i in range(len(items)):
        p_list = permutations(items[:i] + items[i + 1:])
        for p in p_list:
            result.append(items[i] + p)
 
    return result
print (permutations([1,2,3]))    