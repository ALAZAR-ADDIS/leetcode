class Solution:
    def convertTemperature(self, Celsius: float) -> List[float]:
        ans=[]
        Kelvin=Celsius+273.15
        Fahrenheit=Celsius * 1.80 + 32.00
        ans.append(Kelvin)
        ans.append(Fahrenheit)
        return ans