def canCompleteCircuit( gas: list[int], cost: list[int]) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index
    
if __name__ == '__main__':
    gas = [1,2,3,4,5] 
    cost = [3,4,5,1,2]
    print(canCompleteCircuit(gas,cost))