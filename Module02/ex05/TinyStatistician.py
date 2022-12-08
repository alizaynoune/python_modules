import math

class TinyStatistician:
    def __init__(self) -> None:
        pass

    def mean(self, l):
        if not len(l):
            return None
        m = 0
        for i in l:
            m += i
        return float(m / len(l))

    def median(self, l):
        if not len(l):
            return None
        l.sort()
        ll = int(len(l) / 2)
        return float(l[ll])

    def quartile(self, l):
        if not len(l):
            return None
        q1 = self.median(l[0:int(len(l) / 2)])
        q2 = self.median(l[int(len(l) / 2):])
        return [q1, q2]

    def var(self, l):
        if not len(l):
            return None
        m = self.mean(l)
        diff = [(i - m)**2 for i in l]
        return float(self.mean(diff))

    def std(self, l):
        if not len(l):
            return None
        return float(math.sqrt(self.var(l)))


tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
# Expected result: 82.4
print(tstat.median(a))
# Expected result: 42.0
print(tstat.quartile(a))
# Expected result: [10.0, 59.0]
print(tstat.var(a))
# Expected result: 12279.439999999999
print(tstat.std(a))
# Expected result: 110.81263465868862
