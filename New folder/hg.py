
class Solution:
    def matSearch(self, mat, N, M, X):
    
        r = binaryrowsearc(mat, X, N)
        if r == -1:
            return 0
        bo = binarysearch(mat, r, X, M)
        if bo:
            return 1
        return 0


def binaryrowsearc(mat, X, N):
    l = 0
    h = N-1
    while l <= h:
        mid = (h-l)//2
        if mat[mid][0] <= X and mat[mid][-1] >= X:
            return mid
    
        elif mat[mid][0] < X:
            l = mid+1
        else:
            h = mid-1
    return -1


def binarysearch(mat, r, X, M):
    l = 0
    r = M-1
    while l <= r:
        mid = (r-l)//2
        if mat[r][mid] == X:
            return True

        elif mat[r][mid] < X:
            l = mid+1
        else:
            r = mid-1
    return False

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends
