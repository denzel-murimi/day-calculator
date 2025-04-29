#Day of the Week Calculator
class DateCalculator:
    def __init__(self, year, month, day):

        if month < 3:
            month += 12
            year -= 1
        self.year = year
        self.month = month
        self.day = day

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        y = self.year
        k = y % 100
        j = y // 100

        h = (q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7


        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]


date = DateCalculator(1983, 7, 10)
print("The day of the week was: ",date.calculate_day_of_week())

