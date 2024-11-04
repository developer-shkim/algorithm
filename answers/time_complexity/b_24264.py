import sys

num = int(sys.stdin.readline().strip())

print(num * num, 2, sep='\n')

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

