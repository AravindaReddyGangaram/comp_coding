class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1]*len(rains)
        d = {}
        def check(d : dict, cnt: int , c : int): #c-- position, cnt -- lake 
            try:
                for i in d[0]:
                    if i > d[cnt][0]:
                        if  i > c:
                            return (False,0)
                        d[cnt].pop(0)
                        d[0].remove(i) # removing that location from the dict .
                        return (True,i)
                return (False,0)
            except:
                return (False,0)
        for i in range(len(rains)): # [1,0,0,0,3,1] # i -- position in the array
            if rains[i] in d.keys(): # checking whether the lake already is full
                if rains[i] > 0: # ignoring zero...
                    tup = check(d, rains[i] , i) # check if we can dry a lake or not
                    try:
                        if tup[0] :
                            d[rains[i]].append(i) #adding a new element to the dict
                            ans[tup[1]] = rains[i] # replacing the values with the dried out lake number
                        else : 
                            return [] #flooded state...
                    except:
                        return []
                else:
                    d[rains[i]].append(i)
            else:
                d[rains[i]] = [i]
        if 0 in d.keys() :
            if len(d[0]) > 0:
                for i in d[0]: 
                    ans[i] = 1
        return ans
