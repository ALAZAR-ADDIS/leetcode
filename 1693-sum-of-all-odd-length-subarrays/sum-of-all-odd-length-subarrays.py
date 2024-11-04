class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0

        for num in arr:
            total += num

        i = 0
        j = 1

        while i < j < len(arr):
            if (j - i + 1) % 2 != 0:
                total += sum(arr[i: j + 1])
                j += 1
            else:
                j += 1

            if j == len(arr):
                i += 1
                j = i + 1

        return total

        