class Solution:
    def interpret(self, c: str) -> str:
        i = 0
        r = []

        while i < len(c):
            if c[i] == 'G':
                r.append('G')
                i += 1
            elif c[i:i+2] == '()':
                r.append('o')
                i += 2
            else:
                r.append('al')
                i += 4

        return ''.join(r)
