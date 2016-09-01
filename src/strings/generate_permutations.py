import pprint as pp
count = 0
# doesn't handle dupes yet
class Perm(object):

    __slot__ = ['memo', 'memo_count']

    def __init__(self):
        self.memo = {}
        self.memo_count = 0

    def permutation(self, a_string):
        if self.memo.get(a_string):
    	    self.memo_count += 1
            return self.memo[a_string]   
        if len(a_string) == 1:
            return set([a_string])
        permutations = set([])
        for index, letter in enumerate(a_string):
            results = self.permutation(a_string[:index] + a_string[index + 1:])
            for value in results:
	        value += letter
                permutations.append(value)
        self.memo[a_string] = permutations
        return permutations


if __name__=='__main__':
    perm = Perm()
    a_string = 'aa'
    values = perm.permutation(a_string)
    pp.pprint(sorted(values))
    pp.pprint('factorial count: {0}'.format(len(a_string)))
    pp.pprint(perm.memo_count)
   
