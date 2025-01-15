data1 = input()
data2 = input()
data1_year, data1_month, data1_day = int(data1[0:4]), int(data1[4:6]), int(data1[6:8])
data2_year, data2_month, data2_day = int(data2[0:4]), int(data2[4:6]), int(data2[6:8])

year_num = data2_year - data1_year

def check(year, month, day):
    if year in (2000, 2012, 2016) and month == 2 and day > 29:
        return False
    elif year in (1900, 2011, 2014) and month == 2 and day > 28:
        return False
    elif month in (1, 3, 5, 7, 8, 10, 12) and day > 31:
        return False
    elif month in (4, 6, 9, 11) and day > 30:
        return False
    return True

cnt = 0
if year_num != 0:
    for year in range(int(data1_year), int(data2_year)):
        stryear = str(year)
        reverse_year = stryear[::-1]
        reverse_month, reverse_day = reverse_year[0:2], reverse_year[2:4]
        if check(year, int(reverse_month), int(reverse_day)):
            cnt += 1
    stryear = str(data2_year)
    reverse_year = stryear[::-1]
    reverse_month, reverse_day = int(reverse_year[0:2]), int(reverse_year[2:4])
    if data2_month > reverse_month or (reverse_month == data2_month and data2_day > reverse_day):
        cnt += 1

print(cnt)
