import os
import datetime

print(os.environ["GITHUB_ACTIONS"])
print(datetime.datetime.fromisoformat(os.environ["COMMIT_TIMESTAMP"]))
