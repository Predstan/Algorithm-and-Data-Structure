from Julian import date

class activities_calendar:

    def __init__(self, dateFrom, DateTo):
        self.startDate = dateFrom
        self.enddate = DateTo
        self.Activities = list()
        self.dates = dict()


    def length(self):
        return len(self.Activities)


    def getActivity(self, date):
        assert self.enddate.julianDay >= date.julianDay >= self.startDate.julianDay, 'Date not in Range of Calendar'
        for k, v in self.dates.items():
            if date.toGregorian() == k:
                return v
        return 'No Activity for this Date'


    def addActivity(self, date, activity):
        assert self.enddate.julianDay >= date.julianDay >= self.startDate.julianDay, 'Date not in Range of Calendar'
        self.Activities.append(activity)
        self.dates[date.toGregorian()] = activity


    def displayMonth(self, month):
        Month_name = {1: "January", 2: "Feburary", 3 : "March", \
        4: "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August",\
        9 : "September", 10 : "October", 11: "November", 12: "December"}
        month, year = month
        if month in Month_name.keys():
            months = Month_name[month]
            print (months+",", str(year))

            for k, v in self.dates.items():
                if k[1] == month and k[2] == year:
                    if k[1] in Month_name.keys():
                        months = Month_name[month]
                        print (months + ", " + str(k[0])+ ", " + str(k[2]))
                        print ("Activities:", v)
                else:
                    return print("No Activity for this Month")


    def displayAll(self):
        for k, v in self.dates.items():
            print(k ,":" , v)

sport = activities_calendar(date(1, 3, 2020), date(3, 5, 2020))
print(sport.length())
print(sport.getActivity(date(1, 5, 2020)))
sport.addActivity(date(1,3,2020), 'Football')
sport.addActivity(date(2,3,2020), 'Rent Payment')
sport.addActivity(date(3,3,2020), 'Tenth')

print(sport.getActivity(date(1, 3, 2020)))
print(sport.length())
sport.displayMonth((3, 2020))
sport.displayAll()
Fall_2020 = activities_calendar(date(5, 2, 2020), date(7, 2, 2020))
Fall_2020.addActivity(date(5, 30, 2020), 'Data Abstraction')
print(Fall_2020.length())
