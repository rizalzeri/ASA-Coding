#Rizal Zeri Subakti
#24060120130062
#ASA B

constanta1 = 0
constanta2 = 1
n = int(input())
A = list(map(int, input().split()))[:n]
k = int(input())

array = [[constanta1 for i in range(constanta2 + n)]for j in range(constanta2 + k)]
for i in range(constanta2, constanta2 + k):
   for j in range(constanta2, constanta2 + n):
      array[i][j] = array[i][j - constanta2]
      if A[j - constanta2] <= i and A[j - constanta2] > constanta1:
         array[i][j] = array[i][j] +  array[i // A[j - constanta2]][j - constanta2] + constanta2
result = 0
result = result + array[k][n]
print(result)

