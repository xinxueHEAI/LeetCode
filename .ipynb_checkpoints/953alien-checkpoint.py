class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_dict = {i: ind for ind, i in enumerate(order)}
        i = 0 
        while True:
            min_length = True
            min_order = -1
            add_one = False
            for w in words:
                if len(w)>i:
                    min_length = False
                    if min_order < word_dict[w[i]]:
                        min_order = word_dict[w[i]]
                    elif min_order == word_dict[w[i]]:
                        add_one = True
                    else:
                        return False
                else:
                    if not min_length:
                        return False
                    continue
            if add_one:
                i+=1
            else:
                return True
        return True