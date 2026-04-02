class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        front, end, sec = 0, len(nums) - 1, 0 
        sortedNum = sorted(nums)
        ans = []
        #print(sortedNum)
        #print([sortedNum[front], sortedNum[sec], sortedNum[end]])
        
        #sum = sortedNum[front] + sortedNum[sec] + sortedNum[end]
        #print(sum)
        
        for i in range(len(sortedNum)):
            #print(f"front is {sortedNum[i]}")
            sec = i + 1
            end = len(nums) - 1

            while sec < end:
                #print(f"front is {sortedNum[i]}")
                
                ind1 = sortedNum[i]
                ind2 = sortedNum[sec]
                ind3 = sortedNum[end]

                #print(f"sec is {ind2}")
                #print(f"end is {ind3}")
                
            
                sum = ind2 + ind3
                #print(f"sum is {sum}")
                if sum == -ind1:
                    if [ind1, ind2, ind3] in ans:
                        sec += 1
                    else:
                        ans.append([ind1, ind2, ind3])
                        #print(f"sum of 0 found - adding to the answer list: {[ind1, ind2, ind3]}")
                    end -= 1
                elif sum < -ind1:
                    #print(f"sum is less than target: {-ind1} so second pointer moves towards the end")
                    sec += 1
                else:
                    #print(f"sum is greater than target: {-ind1} so end pointer moves towards the front")
                    end -= 1
            #print("answer list current looks like: ")
            #print(ans)
            #end = len(sortedNum) - 1
        #print()
        #print("final answer list: ") 
        #print(ans)
        return ans
        