import datetime as dt


# Implements a proleptic Gregorian calendar date as a Julian day number.
class date:
    def __init__(self, month = 0, day = 0, year = 0):
            if month == 0 or day == 0 or year == 0:
                month, day, year = dt.date.today().strftime("%m/%d/%Y").split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            self.julianDay = 0
            assert self.is_valid_Gregorian(month , day, year), \
                "Invalid Gregorian Date"


    # The first line of the equation, T = (M - 14) / 12, has to be changed
    # since Python's implementation of integer division is not the same
    # as the mathematical definition.
    # T = (M - 14) / 12
    # jday = D - 32075 + (1461 * (Y + 4800 + T) / 4) +
    # (367 * (M - 2 - T * 12) / 12) -
    # (3 * ((Y + 4900 + T) / 100) / 4)
            tmp = 0
            if month < 3:
                tmp = -1
            self.julianDay = day - 32075 + \
            (1461 * (year + 4800 + tmp) // 4) + \
            (367 * (month - 2 - tmp * 12) // 12) - \
            (3 * ((year + 4900 + tmp) // 100) // 4)
    #Returns the Julian Day
    def julian_day(self, date):
            return self.julianDay

    # Extracts the appropriate Gregorian date component.
    def month(self):                # returning M from (M, d, y)
        return (self.toGregorian())[0]

    def day(self):                      # returning D from (m, D, y)
        return (self.toGregorian())[1]

    def year(self):                     # returning Y from (m, d, Y)
        return (self.toGregorian())[2]

    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def day_of_week(self):
        month, day, year = self.toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day \
             + year + year // 4 - year // 100 + year // 400)% 7

    def day_of_week_name(self):
        day = self.day_of_week()
        days = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday",\
                4 : "Friday", 5 : "Saturday", 6 : "Sunday"}
        for key, value in days.items():
            if key == day:
                return value

    # Returns the date as a string in Gregorian format
    def __str__ (self):
        month, day, year = self.toGregorian()
        return "%02d/%02d/%04d" % (month , day, year)

    def as_Gregorian(self, divchar = "/"):
        month, day, year = self.toGregorian()
        data = [str(month), str(day), str(year)]
        return divchar.join(data[0:])


    # Logically compares the two dates.
    def __eq__(self, other_date):
        return self.julianDay == other_date.julianDay

    def __lt__(self, other_date):
        return self.julianDay < other_date.julianDay

    def __le__(self, other_date):
        return self.julianDay <= other_date.julianDay

    def is_valid_Gregorian(self, month , day, year):
        if (year >= 1582) & (day <=31) & (month <=12):
            return  True
    def month_name(self):
        month, day, year = self.toGregorian()
        Month_name = {1: "January", 2: "Feburary", 3 : "March", \
        4: "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August",\
        9 : "September", 10 : "October", 11: "November", 12: "December"}
        for key, value in Month_name.items():
            if month == key:
                return value


    def is_leap_year(self):
        month, day, year = self.toGregorian()
        if year%4 == 0:
            return "This Year is a Leap Year"
        else:
            return "This Year is not a Leap Year"


    def day_of_year(self):
        month, day, year = self.toGregorian()
        Month_num = {1: 1, 2: 32, 3 : 61, \
        4: 91, 5 : 121, 6 : 152, 7 : 182, 8 : 213,\
        9 : 244, 10 : 274, 11: 305, 12: 335}
        if year%4 == 0:
            for k , v in Month_num.items():
                if k == month:
                    return (v - 1 + day)
        else:
            for k, v in Month_num.items():
                if Month_num[1] ==  month:
                    return (v - 1 + day)
                elif k == month:
                    Month_num[month] = v - 1
                    return (v - 1 + day)

    def num_days(self, other_date):
        return self.julianDay - other_date.julianDay

    def num_days_in_month(self):
        month, day, year = self.toGregorian()
        Month_num = {1: 31, 2: 29, 3 : 31, \
        4: 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31,\
        9 : 30, 10 : 31, 11: 30, 12: 31}
        if year%4 == 0:
            for k , v in Month_num.items():
                if k == month:
                    return v
        else:
            for k , v in Month_num.items():
                Month_num[2] = 28
                if k == month:
                    return v


    def advanceBy(self, days):
        self.julianDay = self.julianDay + days
        return self.toGregorian()

    def is_week_day(self):
        if self.day_of_week() < 5:
            return "This date is a week day"
        else:
            return "This date is not a week day"


    def is_Solistice(self):
        month, day, year = self.toGregorian()
        month = self.month_name()
        if (month == "December") & (day == 21 or 22):
            return "Date is Winter Solistice"
        elif (month == "June") & (day == 20 or 22):
            return "Date is Summer Solistice"
        else:
            return "Not Winter nor Summer Solistice"


    def is_Equinox(self):
        month, day, year = self.toGregorian()
        month = self.month_name()
        if (month == "September") & (day == 22 or 23):
            return "Date is Automnal Equinox"
        elif (month == "March") & (day == 20 or 21):
            return "Date is Spring Equinox"
        else:
            return "Not Spring nor Automnal Equinox"


    def toGregorian(self):
        A = self.julianDay + 68569
        B = 4 * A// 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1)// 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A  // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year
