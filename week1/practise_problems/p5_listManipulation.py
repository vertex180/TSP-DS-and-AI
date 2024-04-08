def listManip(nums):
    #nums = []
    sum =0
    # onlyEven = [x%2 == 0 for x in nums]
    onlyEven = [x for x in nums if x%2 == 0 ]
    squared = [y*y for y in onlyEven]
    [sum := z + sum for z in squared]

    print(f'first step only even numbers: {onlyEven}')
    print(f'second step square them: {squared}')
    print(f'sum the remaining: {sum}')


sampleArray = [8,2,45,82,12]
listManip(sampleArray)
