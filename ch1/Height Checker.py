# Leetcode Excercise
# Implements ADT to check he number of times students can be rearranged for ascending heights

class Solution:
    # Creates the Objects of the Height
    def heightChecker(self, heights):
        self.heights = heights
        self.targets = list()
        self.l = 0
        self.k = 0
        for value in self.heights:
            self.targets.append(value)
        for i in range(len(self.targets)-1, 0, -1):
        # examine each item pair
            for j in range(i):
                self.l+=1
                # swap items if needed
                if self.targets[j] > min(self.targets[j+1:]):

                    temp = self.targets[j]
                    self.targets[j] = min(self.targets[j+1:])
                    idx = self.targets[j+1:].index(min(self.targets[j+1:]))
                    self.targets[self.l+idx] = temp
        
        for i in range(len(self.heights)):
            if self.heights[i] != self.targets[i]:
                self.k+=1
        return self.k


g = Solution().heightChecker([1,1,7,8,1,3])
print(g)
