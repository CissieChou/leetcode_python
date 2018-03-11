class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0
        tank = 0
        start = 0
        for index in range(len(gas)):
            tank += gas[index] - cost[index]
            if tank < 0:
                start = index + 1
                tank = 0

            total_tank += gas[index] - cost[index]

        return start if total_tank >= 0 else -1