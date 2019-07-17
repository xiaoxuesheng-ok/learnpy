import csv
import os

COMMENT_FILE_PATH = 'test.csv'

outpul_list = ['1','2','3','4']

if os.path.exists(COMMENT_FILE_PATH) :
    os.remove(COMMENT_FILE_PATH)


# 写
with open(COMMENT_FILE_PATH,'a+',encoding='UTF-8',newline='') as csvfile :
    w = csv.writer(csvfile)
    w.writerow(outpul_list)


# 读

with open(COMMENT_FILE_PATH,'r',encoding='UTF-8',newline='') as csvfil :
    csv_reader = csv.reader(csvfil)
    for row in csv_reader :
        print(row)
        print(row[0])
