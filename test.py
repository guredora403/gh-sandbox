import os
import datetime

print(os.environ["GITHUB_ACTIONS"])
dt = datetime.datetime.fromisoformat(os.environ["COMMIT_TIMESTAMP"])
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
