import math


class TinyStatistician:
    def __init__(self) -> None:
        pass

    def mean(self, value):
        if not len(value):
            return None
        m = 0
        for i in value:
            m += i
        return float(m / len(value))

    def median(self, vaule):
        if not len(vaule):
            return None
        vaule.sort()
        lv = int(len(vaule) / 2)
        return float(vaule[lv])

    def quartile(self, vaule):
        if not len(vaule):
            return None
        q1 = self.median(vaule[0:int(len(vaule) / 2)])
        q2 = self.median(vaule[int(len(vaule) / 2):])
        return [q1, q2]

    def var(self, vaule):
        if not len(vaule):
            return None
        m = self.mean(vaule)
        diff = [(i - m)**2 for i in vaule]
        return float(self.mean(diff))

    def std(self, vaule):
        if not len(vaule):
            return None
        return float(math.sqrt(self.var(vaule)))
