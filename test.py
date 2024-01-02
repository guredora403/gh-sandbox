import os

print(os.environ["GITHUB_ACTIONS"] == True)
print(type(os.environ["GITHUB_ACTIONS"]))