from datetime import datetime


def calc_weeks(start_year):
    """ Calculate the number of weeks since the beginning of set year """
    years_count = datetime.now().year - start_year
    week_counts = 0
    for year in range(years_count):
        year1 = start_year + year
        currens_date_set = datetime(year=year1, month=12, day=31).date()
        weeks_count = int(currens_date_set.strftime("%U")) + 1
        week_counts += weeks_count

    week_now = int(datetime.today().strftime("%U"))
    count = week_counts + week_now

    return count


def main():
    """ Main function """
    weeks = calc_weeks(2019)
    print(weeks)


if __name__ == '__main__':
    main()
