class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op != 'C' and op != 'D' and op != '+':
                record.append(int(op))
            if op == 'C':
                record.pop()
            if op == 'D':
                scoreToDouble = record[-1]
                record.append(2*scoreToDouble)
            if op == '+':
                summand1, summand2 = record[-1], record[-2]
                record.append(summand1 + summand2)
        return sum(record)