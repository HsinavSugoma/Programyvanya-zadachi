import os
import re
import datetime
import sys
from datetime import date
import glob
import shutil
import tarfile

DIR = "."

DATE1 = r"(\d{1,2})/(\d{1,2})/(\d{4})"

rgx = re.compile(DATE1)

def get_files_with_date(folder):

    lst = os.listdir(folder)
    res = []
    now = datetime.datetime.now()

    for item in lst:
        if rgx.match(item) is not None:
            if os.path.getmtime(item) < now:
                res.append(os.normpath(item))

    return res

def get_files_with_date2(folder):

    res = []
    now = datetime.datetime.now()

    for root, dirs, files in os.walk():
        for item in files:
            if rgx.match(item) is not None:
                if os.path.getmtime(item) < now:
                    res.append(os.normpath(item))

    return res

def get_files_with_date3(folder, recursive = False):
    res = []
    now = datetime.datetime.now()

    lst = glob.glob("*[0-9]+/[0-9]+/[0-9]+*", recursive=recursive)

    for item in lst:
        if os.path.getmtime(item) < now:
            res.append(os.normpath(item))

    return res

def create_backup(files):
    today = date.today()
    tfile = tarfile.open(f"Log_{today.year}_{today.month}_{today.day}")
    for file in files:
        tfile.add(file)
        shutil.rmtree(file)

    tfile.close()

# T22_5
def find_logs(folder, rec):
    lst = glob.glob('*.tar.gz', recursive=rec)
    lst += glob.glob('*.log', recursive=rec)
    return lst

if __name__ == '__main__':
    if len(sys.argv) > 1:
        DIR = sys.argv[1]

    for item in find_logs():
        # os.remove(item)
        shutil.rmtree(item)

    files_to_arc = get_files_with_date(DIR)

    create_backup(files_to_arc)

