import random
from datetime import datetime, timedelta

# Choose your start and end dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 12, 31)

# Find the number of seconds between the two dates
time_between = end_date - start_date
seconds_between = time_between.total_seconds()

# Pick a random number of seconds to add
random_seconds = random.randint(0, int(seconds_between))

# Add those seconds to the start date
random_date = start_date + timedelta(seconds=random_seconds)

print("Random date and time:", random_date)
