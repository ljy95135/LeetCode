# write it in a more beautiful way!
# like a num_map List with (number, string)
# or for every thousand hundred ten and one position have a string map
# "" "I" "II" "III" "IV" ... "IX"


class Solution:
    def intToRoman(self, num):
        """
        assume 0<num<4000
        :type num: int
        :rtype: str
        """
        roman = ''
        while num > 0:
            if num >= 1000:
                num -= 1000
                roman += 'M'
            elif num >= 900:
                num -= 900
                roman += 'CM'
            elif num >= 500:
                num -= 500
                roman += 'D'
            elif num >= 400:
                num -= 400
                roman += 'CD'
            elif num >= 100:
                num -= 100
                roman += 'C'
            elif num >= 90:
                num -= 90
                roman += 'XC'
            elif num >= 50:
                num -= 50
                roman += 'L'
            elif num >= 40:
                num -= 40
                roman += 'XL'
            elif num >= 10:
                num -= 10
                roman += 'X'
            elif num >= 9:
                num -= 9
                roman += 'IX'
            elif num >= 5:
                num -= 5
                roman += 'V'
            elif num >= 4:
                num -= 4
                roman += 'IV'
            elif num >= 1:
                num -= 1
                roman += 'I'
        return roman
