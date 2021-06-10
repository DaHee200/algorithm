#-------------------add--------------------
def add(param1, param2):
    
    return param1 + param2

#------------centuryFromYear------------------

def centuryFromYear(year):
    if year % 100 == 0:
        return year / 100
    else :
        return (year// 100)+1
    #----------------------checkPalindrome----------------
    def checkPalindrome(inputString):
    if inputString == "".join(reversed(inputString)):
        return True
    else : 
        return False