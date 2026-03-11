class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b=bin(n)[2:]
        flipped=""
        for bit in b:
            if bit=='0':
                flipped+='1'
            else:
                flipped+='0'
        return int(flipped,2)