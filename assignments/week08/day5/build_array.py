def buildArray(target: list[int], n: int) -> list[str]:
        ans = []
        for i in range(1,target[-1]+1):
            if i in target:
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans

print(buildArray([1,2,3],3))