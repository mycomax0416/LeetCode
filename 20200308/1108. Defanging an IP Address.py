class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = list(address)
        for idx in range(len(arr)):
            if arr[idx] == '.':
                arr[idx] = '[.]'
        return ''.join(arr)