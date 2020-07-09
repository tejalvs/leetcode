class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        result = 0
        size = len(s)
        for i in range(size):
            if s[i] == 'L':
                counter = counter + 1
            else:
                counter = counter - 1
            if counter == 0:
                result = result + 1
        return result


