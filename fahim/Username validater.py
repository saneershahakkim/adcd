#Python Project
#Project = username validator
#By: Mohammed Fahim EP

class Authentication(object):
    def __init__(self, username = ''):
        self.username = username

    def __lower(self):
        lower = any(c.islower() for c in self.username)
        return lower
    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        return upper
    def __digit(self):
        digit = any(c.isdigit() for c in self.username)
        return digit
    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)

        report = lower and upper and digit and length >=6   #Components required in Username

        if report:
            print("This is a valide Username")
            return True

        elif not lower:
            print("You didnt use  Lowercase charecter in Username")#Project = username validator
            return False

        elif not upper:
            print("You didnt use  Uppercase charecter in username")
            return False

        elif not length>=6:
            print("Username should have atleast 6 charecters")
            return False

        elif not digit:
            print("You didnt use Digits in Username")
            return False

C = Authentication("Fahim123")  #type your Username here
print(C.validate())