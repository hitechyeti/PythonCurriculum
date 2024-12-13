def largest_sum_subsequence(numbers,k):
    listss = []
    
    for i in range(len(numbers)-1):
        if i+k > len(numbers):
            break
        listss.append(numbers[i:i+k])
        
    sums_l = []
    for lst in listss:
        suming = 0
        for i in range(len(lst)):
            suming += lst[i]
        sums_l.append(suming)
        
    return max(sums_l)


def largest_sum_subsequence(numbers, k):
    lst = []  
    for i in range(len(numbers) - k + 1): 
        subsequence_sum = sum(numbers[i:i + k])  
        lst.append(subsequence_sum) 
    return max(lst)


def largest_sum_subsequence(numbers,k):
    L=[]
    for i in range(len(numbers)-k+1):
        L.append(numbers[i:i+k])
    a=sum(L[0])
    for i in L:
        if sum(i)>a:
            a=sum(i)
    return a
