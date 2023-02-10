'''

1
5
8 6 9 2 5
2
12 2 3 4
30 0

'''

class Solution:
    def maximumToys(self , NumberOfToys , costOfToys , lenNumberOfQueries , numberOfQueries):
        sorted(costOfToys)
        return costOfToys[-1]



if __name__ == "__main__":
    for _ in range(int(input())):
        NumberOfToys = int(input())
        costOfToys = [int(i) for i in input().strip().split()]
        numberOfQueries = [[] for _ in range(int(input()))]
        
        for i in range(len(numberOfQueries)):
            numberOfQueries[i].extend(int(i) for i in input().strip().split())
            
        answer = Solution().maximumToys(NumberOfToys,costOfToys,len(numberOfQueries),numberOfQueries)
        for i in answer:
            print(i , end=" ")
        print()
    
