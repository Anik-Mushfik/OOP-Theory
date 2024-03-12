class DateVal:
    def __init__(self,date):
        date_info = date.split("-")
        self.date = date_info[0]
        self.month = date_info[1]
        self.year = date_info[2]
    
    def __str__(self):
        return f"Day:{self.date}; Month:{self.month}; Year:{self.year}"

    
class TimeVal:
    def __init__(self,time):
        time_info = time.split("-")
        self.hour = time_info[0]
        self.minutes = time_info[1]
        self.second = time_info[2]

    def __str__(self):
        return f"Hour:{self.hour}; Minutes:{self.minutes}; Second:{self.second}"


def main(date, time):
    d = DateVal(date)
    print(d)
    t = TimeVal(time)
    print(t)

if __name__ == "__main__":
    main("11-03-2024", "06-10-29")