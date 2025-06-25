from datetime import datetime
from dateutil.relativedelta import relativedelta

def renewal_date(timestamp):
    dt = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
    next_month_date = dt + relativedelta(months=1)
    return next_month_date.date()

timestamp = "20250624164247"

def is_overdue(date_str):
    given_date = datetime.strptime(date_str, "%Y%m%d").date()
    current_date = datetime.today().date()
    return current_date > given_date

print(renewal_date(timestamp))


