# Intuition
# For each number except '0' we have 2 ways to decode - either use it or concat with the next number(if current number is '1' or '2').

# Approach
# Go through all the numbers in the string recursively using DFS.
# If current number is '1', we have 2 recursive paths - (curr + 1) and (curr + 2).
# If current number is '2' and next number is b/w '0' and '6', we again have 2 recursive paths - (curr + 1) and (curr + 2).
# If the current number is '0', we can't go ahead with that path.
# Finally, we can store the number of ways to decode starting at a given index and use the stored value directly when we come across the same subproblem.
# For eg:- "11106". We find dp[2] = 1 while recursively doing index + 1. Now for index = 0 and path -> index + 2, we end up calling our DFS function with index 2. Lucky for us we already computed number of ways to decode for index 2 and stored it in dp[2], so we can use the stored result.

#   Complexity
# Time complexity:
# O(N)

# Space complexity:
# O(N)

class Solution:
    def numDecodings(self, s: str) -> int:
      N = len(s)
      dp = [0] * (N + 1)
      # no of ways to decode for length 1 = 1
      dp[N] = 1
      def ways(i):
        if dp[i]: return dp[i]
        # no ways
        if s[i] == '0': return 0
        # current number is a single number
        ans = ways(i + 1)
        if i + 1 < N and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
          # current number is concatenated with next number
          ans += ways(i + 2)
        # store no of ways to decode at index i
        dp[i] = ans
        return ans
      return ways(0)
