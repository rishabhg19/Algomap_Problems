class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        canMake = True
        balloon = {'b': 1, 'a': 1,'n':1, 'l':2, 'o':2}
        freqs = Counter(text)
        impossible = False
        for letter in balloon:
            if letter not in freqs:
                impossible = True
        if impossible:
            return 0
        numLO = min(freqs['l'],freqs['o'])
        if numLO < 2:
            return 0
        numOther = min(freqs['b'], freqs['a'], freqs['n'])
        if numLO // 2 >= numOther:
            return numOther
        elif numLO // 2 < numOther:
            return numLO // 2
        else:
            return 0