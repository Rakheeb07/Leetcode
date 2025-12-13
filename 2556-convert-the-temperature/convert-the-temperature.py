class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        w=[]
        a=celsius+273.15
        w.append(a)
        f=celsius*1.80+32.00
        w.append(f)
        return w