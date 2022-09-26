class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # 1. all lowercase letters that are directly or indirectly equal(connected) to each other
        # will be put in the same group using union-find algorithm
        # 2. then if we find any equation that says 2 lowercase letters in same group are not equal, we return False
        # 3. else if no such equation is found, return True

        def find(n):
            g = group[n]
            while g != group[g]:
                g = group[g]
            return g
        
        # initially all lowecase letters will belong to seperate groups
        group = [i for i in range(26)]

        # merge lowercase letters that are equal in one group
        for eq in equations:
            if eq[1] == '=':
                 group[find(ord(eq[0]) - ord('a'))] = find(ord(eq[3]) - ord('a'))

        # if 2 letters are not equal then
        # they should belong to seperate groups in order to satisfy all equations
        for eq in equations:
            if eq[1] == '!' and find(ord(eq[0]) - ord('a')) == find(ord(eq[3]) - ord('a')):
                return False
        return True
