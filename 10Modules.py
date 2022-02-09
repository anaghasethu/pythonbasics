import datetime

import camelcase

today = datetime.date.today()
print(today)

message = 'anagha'
c = camelcase.CamelCase()
print(c.hump(message))
