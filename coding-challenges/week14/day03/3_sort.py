def maximumUnits( boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units
                return ans
        return ans 

if __name__ == '__main__':


    boxTypes = [[1,3],[2,2],[3,1]] 
    truckSize = 4
    print(maximumUnits(boxTypes , truckSize))