import datetime
class DayOfWeekFinder:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_day_of_week(self, day: int, month: int, year: int) -> str:
        date = datetime.date(year, month, day)
        return self.days[date.weekday()]

def main():
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    
    finder = DayOfWeekFinder()
    print(f"The day of the week is: {finder.get_day_of_week(day, month, year)}")
main()