class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        n=len(encodedText)
        cols=n//rows
        result=[]
        for start_col in range(cols):
            i,j=0,start_col
            while i<rows and j<cols:
                result.append(encodedText[i*cols+j])
                i+=1
                j+=1
        return "".join(result).rstrip()    