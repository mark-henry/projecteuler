import datetime

startdate = datetime.date(1901, 1, 1)
enddate = datetime.date(2000, 12, 31)

sundaycount = 0
date = startdate
while date <= enddate:
	if date.day == 1 and date.weekday() == 6:
		sundaycount += 1
	date += datetime.timedelta(days=1)

print sundaycount