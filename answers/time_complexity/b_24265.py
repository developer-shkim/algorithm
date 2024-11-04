import sys

num = int(sys.stdin.readline().strip())

print(sum([i for i in range(1, num)]), 2, sep='\n')

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''
