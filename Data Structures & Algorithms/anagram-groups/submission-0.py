class Solution:

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaGroup = {}
        
        for i in strs:
            sortedI = "".join(sorted(i))
            if sortedI in anaGroup:
                anaGroup[sortedI].append(i)
            else:
                anaGroup[sortedI] = [i]
        
        return list(anaGroup.values())
                
        