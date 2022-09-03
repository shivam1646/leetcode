class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # replace every number with 0
        if k == 0:
            return [0] * len(code)
        sum = 0
        res = []
        if k > 0:
            left = 0
            # for 0th number, get sum of next k numbers
            # Note: k < len(code) as per constraint in description
            while left < k:
                left = left + 1
                sum += code[left]
            res.append(sum)
            # for 1...n, increment left ptr
            # sum[curr] = sum[curr - 1] - code[curr] + code[left_ptr]
            for curr in range(1, len(code)):
                left = (left + 1) % len(code)
                sum -= code[curr]
                sum += code[left]
                res.append(sum)
        else:
            right = len(code)
            # for 0th number, get sum of previous k numbers
            # Note: k < -(len(code)) as per constraint in description
            while (len(code) - right) < abs(k):
                right = right - 1
                sum += code[right]
            res.append(sum)
            # for 0...n, increment right ptr
            # sum[curr + 1] = sum[curr] + code[curr] - code[right_ptr]
            for curr in range(0, len(code) - 1):
                sum += code[curr]
                sum -= code[right]
                right = (right + 1) % len(code)
                res.append(sum)
        return res
