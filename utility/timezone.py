import random
from pytz import timezone

from datetime import datetime as dt
ind_time=dt.now(timezone("Asia/Kolkata"))
s= ind_time.strftime("%d%m%Y%H%M%S")

print(s)
print(type(s))