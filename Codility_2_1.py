def solution(A, K):
    # write your code in Python 3.6

    for i in range(K):
        temp = A[len(A) - 1]
        for i in range(len(A)-1):
            A[len(A) - (i+1)] = A[len(A) - (i+2)]
        A[0] = temp

    print(A)
    return A
    pass

solution([1,-2,3,4], 2)
