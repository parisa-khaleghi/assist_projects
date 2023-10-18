from git import repo
import datetime
import dateutil.tz

# function to commit in costum date
def commit(project_path, file_path, message, year, month, day, hour, minute):
    r = repo.Repo(project_path, search_parent_directories=True)
    r.index.add(file_path)
    r.index.commit(message, commit_date=datetime.datetime(year, month, day, hour, minute, tzinfo=dateutil.tz.tzoffset(u'TRT', 3*3600)))
    origin = r.remotes[0]
    origin.push()

# fill out information for project path and file path on your system
project_path = "/Users/parisakhaleghi/Desktop/Coding/assist-projects"
file_path = "/Users/parisakhaleghi/Desktop/Coding/assist-projects/Python/Git Commit/git-commit.py"

# fill out information for commiting
message = 'test: check for 2 month ago'
year = datetime.datetime.now().year
month = datetime.datetime.now().month-2
day = datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

# call the function with custom data
commit(project_path, file_path, message, year, month, day, hour, minute)
