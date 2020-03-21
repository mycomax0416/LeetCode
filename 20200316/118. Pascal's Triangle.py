class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            ans = [[1]]
            for n in range(numRows-1):
                row = [1]
                for idx in range(len(ans)-1):
                    row.append(ans[-1][idx]+ans[-1][idx+1])
                row.append(1)
                ans.append(row)
            return ans