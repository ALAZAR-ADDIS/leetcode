class Solution:
    def intToRoman(self, num: int) -> str:
        num_rom = {
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"}
        ans=[]

        for pair in num_rom:
            
            while pair <= num:
                ans.append(num_rom[pair])
                num-=pair
            
        return "".join(ans)
                
            