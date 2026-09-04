class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        Edge case:
        if len(hand)%groupSize != 0 then return False

        1. store all numbers and their frenquency in the dictionnary in a sorted order
        2. check the frequency of the smallest value number, check also if the numbers in range(number:number+groupSize) also have enough frequency, if not return False, else we substract the frequency we needed
        '''

        if len(hand)%groupSize != 0:
            return False

        count={}

        for num in hand:
            count[num]=count.get(num,0)+1
        
        sorted_keys=sorted(count.keys())

        for number in sorted_keys:
            required_frequency=count.get(number)
            if required_frequency==0:
                continue
            for next_number in range(number, number+groupSize):
                frequency=count.get(next_number,0)
                if required_frequency > frequency:
                    return False

                count[next_number]=frequency-required_frequency
        return True