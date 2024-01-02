import os
import datetime

print(os.environ.get("GITHUB_ACTIONS", "false") == "true")