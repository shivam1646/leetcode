class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # odd length
        if len(changed) % 2 != 0:
            return []
        
        # Algo based on given hints
        # 1. sort the array
        # 2. remove the smallest num and it's double value
        # 3. repeat until array is empty

        res = []
        # sort the array
        changed.sort()
        
        freq = Counter(changed)
            
        for num in changed:
            # stop the loop if we found the original array
            if len(res) == len(changed) / 2:
                break
            double = num * 2
            if num > 0 and freq[num] and freq[double]:
                res.append(num)
                freq[num] -= 1
                freq[double] -= 1 
            elif num == 0 and freq[num] > 1:
                res.append(num)
                freq[num] -= 2
                
        return res if len(res) == len(changed) / 2 else []
        
