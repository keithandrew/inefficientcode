def get_earliest(*dates):
    """return the earliest of formatted date strings"""

    def date_key(date):
        (month, day, year) = date.split("/")
        return (year, month, day)

    return min(dates, key=date_key)
