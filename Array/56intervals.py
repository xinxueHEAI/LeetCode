class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        return_list = []
        intervals.sort(key = lambda x: x[0])
        last_i = intervals[0]
        while i < len(intervals):
            this_i = intervals[i]
            if last_i[0] != this_i[0] and last_i[1] != this_i[1]:
                if last_i[1]<this_i[0]:
                    return_list.append(last_i)
                    last_i = this_i
                else:
                    last_i = [last_i[0], max(last_i[1],this_i[1])]
            else:
                last_i = [last_i[0], max(last_i[1],this_i[1])]
            i+=1
        return_list.append(last_i)
        return return_list
