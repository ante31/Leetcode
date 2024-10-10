class Solution(object):
    def intToRoman(self, num):
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        romanNum = ""
        length = len(str(num))

        #radi se o 1000
        if length == 4:
            decimal = num // 1000
            for i in range(decimal):
                romanNum += "M"
            length-=1

        #radi se o 100
        if length == 3:
            decimal = (num // 100)%10
            if decimal <= 3:
                for i in range(decimal):
                    romanNum += "C"
            elif decimal == 4:
                romanNum += "CD"
            elif decimal == 5:
                romanNum += "D"
            elif 6 <= decimal and decimal <= 8:
                romanNum += "D"
                for i in range (decimal%5):
                    romanNum += "C"
            elif decimal == 9:
                romanNum += "CM"
            length-=1

        #radi se o 10
        if length == 2:
            decimal = (num // 10)%10
            if decimal <= 3:
                for i in range(decimal):
                    romanNum += "X"
            elif decimal == 4:
                romanNum += "XL"
            elif decimal == 5:
                romanNum += "L"
            elif 6 <= decimal and decimal <= 8:
                romanNum += "L"
                for i in range (decimal%5):
                    romanNum += "X"
            elif decimal == 9:
                romanNum += "XC"
            length-=1

        #radi se o <=9
        if length == 1:
            decimal = num % 10
            if decimal <= 3:
                for i in range(decimal):
                    romanNum += "I"
            elif decimal == 4:
                romanNum += "IV"
            elif decimal == 5:
                romanNum += "V"
            elif 6 <= decimal and decimal <= 8:
                romanNum += "V"
                for i in range (decimal%5):
                    romanNum += "I"
            elif decimal == 9:
                romanNum += "IX"
            length-=1
        
        return romanNum
        
num = 3749
solution = Solution()
print(solution.intToRoman(num))

#https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150