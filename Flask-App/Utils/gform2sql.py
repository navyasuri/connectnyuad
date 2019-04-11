import pymysql
import db_helpers as db

fp = open('test_data.csv')

for line in fp:
    fb, wa, ig = False, False, False
    data = line.split('^')
    if data[5] == '/': data[5] = ''
    if "Messenger" in data[-1]: fb = True
    if "Whatsapp" in data[-1]: wa = True
    if "Instagram" in data[-1]: ig = True
    db.addToDatabase(data[0], data[1], data[2], data[4], data[5], data[3], fb, ig, wa)

print("done")