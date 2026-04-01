class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots=sorted(zip(positions,healths,directions,range(len(positions))))
        stack=[]
        alive=[True]*len(positions)
        health=healths[:]
        for pos,h,d,i in robots:
            if d=='R':
                stack.append(i)
            else:
                while stack:
                    j=stack[-1]
                    if not alive[j]:
                        stack.pop()
                        continue
                    if health[j]<health[i]:
                        alive[j]=False
                        stack.pop()
                        health[i]-=1
                    elif health[j]>health[i]:
                        alive[i]=False
                        health[j]-=1
                        break
                    else:
                        alive[i]=False
                        alive[j]=False
                        stack.pop()
                        break
        result=[]
        for i in range(len(positions)):
            if alive[i]:
                result.append(health[i])
        return result
        