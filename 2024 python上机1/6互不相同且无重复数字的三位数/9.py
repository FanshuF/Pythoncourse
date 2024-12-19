def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)#能被4整除但不能被100整除，或者能被400整除
def day_of_the_year(day, month, year):
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = sum(days_in_month[:month - 1])
    total_days += day
    return total_days
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

# 检查输入的月份和日期是否有效
if month < 1 or month > 12:
    print("输入的月份不正确，请输入1-12之间的数字。")
elif day < 1 or day > 31:
    print("输入的日期不正确，请输入1-31之间的数字。")
else:
    if month == 2 and is_leap_year(year) and day > 29:
        print("输入的日期不正确，闰年的2月也只有29天。")
    elif month in [4, 6, 9, 11] and day > 30:
        print("输入的日期不正确，这些月份只有30天。")
    else:
        print(f"{year}年{month}月{day}日是这一年的第 {day_of_the_year(day, month, year)} 天。")