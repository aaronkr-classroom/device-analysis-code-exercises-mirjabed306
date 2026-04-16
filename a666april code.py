#SayDays.py

class SayDays:
    def _init_(self, year: int, month: int, day: int):
        
        thi.year = ywar
        this.month = month
        this.day = day
        
    def is_leap(self):
        y = self.year
        #leap year? February = 29 : not = 28
        #leap year? Year = 366: not 265
        #using in 2 place -> let's return bool
        return (
            (y % 4 == 0 and y % 100 != 0) or
            (y % 400 == o)
        )
    def days(self) -> int:
        #from January 1, how amny days untill now?
        days_in_month = [
            31, 29 if self.is_leap() else 28, 31, 30,
            31, 30, 31, 31,
            31, 30, 31, 31
            ]
        
        total = 0
        m = 0
        
        #xcalcilate all days in all previous months
        wlile m < self.month: # 0<4
            total += days_in_month[m]
            m += 1
            
            #Add the days of the month untill today (givcen date)
            total += self.day # ppproperty not function return
            return total
        
    def days_left(self) ->int:
        #untill Dec31, how many days left?
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days() # not 16th, but 116
    
    def weekday(self) ->int:
        #use Zeller's formulla to find the numeric day of the week
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3: #january? February?
            m += 12
            y -= 1
        
        K = y % 100 # last two disit of the year (2026 % 100 = 26)
        J = y // 100 # First two disit od=f the year (1926 // 100 = 19)
        
        h = (d = (13 * (m+1)) //
             5 + k + k // 4 + 5  * J) % 7
        
        return h #5 = Thursday
    
    def weekday_name(self) -> str:
        #print the english name of the numeric day if the week
        names = ["Saturday", "Sunday", "Monday", "Tuesday",
                 "Wednesday", "Thursday", "Friday"
                 ]
        return name[self.weekdays()] # 5 -> "Thursday"
            
        
# run it!!
while True:
    year = int(input("what year is it? "))
    month = int(input("what month is it? "))
    day = int(input("what day is it? "))
    
    date = SayDays(year, month, day)
    
    print("Days after Jan 1: ", date.days())
    print("Days untill Dec 31: ",date.days_left())
    print("Numeric day of the week: ", date.weekdays())
    print("English day of the week: ", date.weekday_name())