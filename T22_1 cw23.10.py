import os
import sys

OUTFILE = "output1.txt"

def folder_cmp3(dir1, dir2):

    files_list1 = []
    for root, dirs, files in os.walk(dir1):
        files_list1 += files

    files_list2 = []
    for root, dirs, files in os.walk(dir1):
        files_list2 += files

    return set(files_list1) ^ set(files_list2)

def folder_cmp3_1(dir1, dir2):

    files_list1 = {}
    for root, dirs, files in os.walk(dir1):
        for f in files:
            files_list1[f] = os.path.getctime(f)

    files_list2 = {}
    for root, dirs, files in os.walk(dir1):
        for f in files:
            files_list2[f] = os.path.getctime(f)

    for filename in files_list1.keys():
        if filename in files_list2:
            if files_list1[filename] < files_list2[filename]:
                print(files_list1[filename])
            else:
                print(files_list2[filename])

    return set(files_list1) ^ set(files_list2)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        DIR1 = input("First folder: ")
        DIR2 = input("Second folder: ")
    else:
        DIR1 = sys.argv[1]
        DIR2 = sys.argv[2]
        if len(sys.argv) > 3:
            OUTFILE = sys.argv[3]

    out_old = sys.stdout

    with open(OUTFILE, "wt") as f:
        sys.stdout = f

    print(folder_cmp3(DIR1, DIR2))
    sys.stdout = out_old