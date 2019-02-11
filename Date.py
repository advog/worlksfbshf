from datetime import date
from datetime import time
from datetime import datetime


def main():
    today = date.today()
    print("ayy yo it be ",today)

    print(today.day," ",today.month," ",today.year)

    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print(days[today.weekday()])

    today = datetime.now()
    print(today.time())



if __name__ == '__main__':
    main()