import pymysql, pymysql.cursors
import dbconfig as dbconfig 

def addToDatabase(netid, fname, pname, things, met, year, fb, ig, wa):

    met = met.split(',')
    for i in range(len(met)):
        met[i] = met[i].strip()
    alrmet = netid+","+",".join(met)
    if len(met)==1:
        alrmet = netid+","+met[0]
        if met[0]=='': alrmet=netid
    print(alrmet)

    try:
        connection = pymysql.connect(host = 'localhost', 
            database = 'socialite',
            user = dbconfig.USERNAME, 
            password = dbconfig.PASSWORD)

        sql_query = '''
            INSERT INTO `user_data` (`net_id`, 
            `full_name`, 
            `pref_name`, 
            `3_things`, 
            `already_met`, 
            `class_year`, 
            `check_fb`, 
            `check_ig`, 
            `check_wa`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = [netid, fname, pname, things, alrmet, year, fb, ig, wa]

        cur = connection.cursor()
        result = cur.execute(sql_query, params)
        connection.commit()
        output ="Inserted successfully"

    except (pymysql.Error, pymysql.Warning) as error:
        connection.rollback()
        output = "Something went wrong in the insertion" + str(error)

    connection.close()
    return output
    


def getFromDatabase():
    try:
        connection = pymysql.connect(host='localhost',
        db='socialite',
        user=dbconfig.USERNAME,
        passwd=dbconfig.PASSWORD,
        cursorclass = pymysql.cursors.DictCursor)

        query = "select * from user_data"
        cur = connection.cursor()
        cur.execute(query)
        records = cur.fetchall()
        # print(records)

        userDictionary = {}

        # Make the netid as a key for all data for each user
        # Store all users in userDictionary with netid as key
        
        for record in records:
            # print(record)
            userDictionary[record['net_id']] = record
        
        # print(userDictionary)

        return userDictionary



    except (pymysql.Error, pymysql.Warning) as e:
        print ("Error while connecting to MySQL", e)
        return None

    connection.close()



def updateDatabase(n1, n1_dont_match):
    
    try:
        p1_dont_match = ",".join(n1_dont_match)
        if len(n1_dont_match)==1:
            p1_dont_match = n1_dont_match[0]

        # print n1, p1_dont_match
        query = "update user_data set already_met = %s where net_id = %s ;"

        connection = pymysql.connect(host='localhost',
        db='socialite',
        user=dbconfig.USERNAME,
        passwd=dbconfig.PASSWORD)

        cur = connection.cursor()
        cur.execute(query,[p1_dont_match, n1])

        print("Update complete")

        connection.commit()
        connection.close()

    except (pymysql.Error, pymysql.Warning) as e:
        print("Error in DB: ", e)