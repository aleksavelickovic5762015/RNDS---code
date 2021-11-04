import pymysql


##INIZIO SELENA####
import pymysql

def all_users():
    sql = "" \
          "SELECT users.name, users.completeName, userstatuses.name, defaultstatuses.description, users.isDisturbing, users.actualNoiseLevel " \
          "FROM rnds.users " \
          "left JOIN rnds.userstatuses on  users.actualUserStatus = userstatuses.name " \
          "left JOIN rnds.defaultstatuses on userstatuses.Defaultstatus = defaultstatuses.name "
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    users = []
    for t in result:
        user = {}
        user["userID"] = str(t[0])
        user["userName"] = t[1]
        user["currentStatusID"] = t[2]
        user["currentStatus"]= t[3]
        user["disturbing"]= t[4]
        user["noiseLevel"]=t[5]
        users.append(user)

    conn.close()
    return users


def get_user_setting(status):
    sql = "" \
          "SELECT isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel " \
          "FROM rnds.usersettings WHERE name = %s"
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql, (status))

    result = cursor.fetchall()
    conn.close()
    return result


def put_user_setting(isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, name):
    sql1 = "UPDATE rnds.usersettings set isWindowsOpen=%s , isDoorOpen=%s, isLightsOn=%s, noiseLevel=%s WHERE name = %s"

    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql1, (isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, name))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

def statuses():
    sql = "" \
          "SELECT * " \
          "FROM defaultstatuses "
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    statuses = []
    for t in result:
        status = {}
        status["statusID"] = str(t[0])
        status["statusDescription"] = t[1]
        statuses.append(status)
    conn.close()
    return statuses

def put_user_status(username, status):
    sql1 = "UPDATE rnds.users set actualUserStatus=%s WHERE name = %s"

    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql1, (status, username))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result


def get_user_setting2(status):
    sql = "" \
          "SELECT usersettings.name, isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, customisedDescription " \
          "FROM rnds.usersettings LEFT JOIN rnds.userstatuses ON usersettings.name = userstatuses.name " \
          "WHERE usersettings.name = %s"
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    cursor = conn.cursor()
    cursor.execute(sql, (status))

    result = cursor.fetchall()
    for t in result:
          status = {}
          status["StateID"] = t[0]
          status["isWindowsOpen"] = t[1]
          status["isDoorOpen"] = t[2]
          status["isLightsOn"] = t[3]
          status["noiseLevel"] = t[4]
          status["customisedDescription"] = t[5]

    conn.close()
    return status


def put_user_setting2(name, newUserSettings):
    isWindowsOpen= newUserSettings['isWindowsOpen']
    isDoorOpen = newUserSettings['isDoorOpen']
    isLightsOn = newUserSettings['isLightsOn']
    noiseLevel = newUserSettings['noiseLevel']
    description = newUserSettings['customisedDescription']
    sql1 = "UPDATE rnds.usersettings set isWindowsOpen=%s , isDoorOpen=%s, isLightsOn=%s, noiseLevel=%s WHERE name = %s"
    sql2 = "UPDATE rnds.userstatuses set customisedDescription = % s WHERE name = %s"
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    cursor = conn.cursor()
    cursor.execute(sql1, (isWindowsOpen, isDoorOpen, isLightsOn, noiseLevel, name))
    cursor.execute(sql2, (description, name))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result


def getNoiseLevel(name):
    sql1 = "SELECT users.name, usersettings.noiseLevel, users.isDisturbing FROM rnds.users " \
           "LEFT JOIN rnds.usersettings on users.actualUserStatus = usersettings.name WHERE users.name = %s"
    sql2 = "SELECT users.name, usersettings.noiseLevel, users.isDisturbing FROM rnds.users " \
           "LEFT JOIN rnds.usersettings on users.actualUserStatus = usersettings.name WHERE users.name NOT IN (%s)"
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    cursor = conn.cursor()
    cursor.execute(sql1, name)
    result = cursor.fetchall()
    Allusernoiselevel= []
    for t in result:
          NoiseLevel = {}
          NoiseLevel["userID"] = str(t[0])
          NoiseLevel["noiseLevel"] = str(t[1])
          NoiseLevel["isDisturbing"] = t[2]
          Allusernoiselevel.append(NoiseLevel)
    cursor.execute(sql2, name)
    result2 = cursor.fetchall()
    for t in result2:
        NoiseLevel = {}
        NoiseLevel["userID"] = str(t[0])
        NoiseLevel["noiseLevel"] = str(t[1])
        NoiseLevel["isDisturbing"] = t[2]
        Allusernoiselevel.append(NoiseLevel)
    conn.close()
    return Allusernoiselevel

def getUserNoiseLevel(name):
    sql1 = "SELECT users.name, users.actualUserStatus, lu_noise.dbmax " \
           "FROM rnds.users " \
           "LEFT JOIN rnds.usersettings on users.actualUserStatus = usersettings.name " \
           "LEFT JOIN rnds.lu_noise on lu_noise.name = usersettings.noiseLevel " \
           "WHERE users.name = %s"
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    cursor = conn.cursor()
    cursor.execute(sql1, name)
    result = cursor.fetchall()
    conn.close()
    for t in result:
          NoiseLevel = {}
          NoiseLevel["userID"] = str(t[0])
          NoiseLevel["actualUserStatus"] = str(t[1])
          NoiseLevel["dbMax"] = t[2]
    return NoiseLevel


def putIsDisturbing(usersID, flag):
    sql1 = "UPDATE rnds.users set isDisturbing=%s WHERE name NOT IN (%s)"
    conn = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    cursor = conn.cursor()
    cursor.execute(sql1, (flag, usersID))
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

##FINE SELENA####

def show_id(id):
    connection1 = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    sql = "select name,lightId,lightStatus,actualUserStatus,isDisturbing,doorStatus from rnds.users WHERE name = %s"
    cursor = connection1.cursor()
    # 4. execute the query
    cursor.execute(sql,(id,))
    # 5. fetch the results from the DB
    result = cursor.fetchone()
    # 6. print the results
    # 7. close the cursor
    cursor.close()
    connection1.close()
    return result

def get_user_preference(id):
    connection = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    status = get_user_status(id)
    sql = "SELECT isLightsOn,isDoorOpen FROM rnds.usersettings WHERE name = %s "
    cursor = connection.cursor()
    # 4. execute the query
    cursor.execute(sql,(status,))
    light_pref = cursor.fetchone()
    # close the connection
    cursor.close()
    connection.close()
    return light_pref

def upload_light_status(id,new_light_status):
    connection = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    sql= "UPDATE rnds.users set lightStatus = %s  WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(sql,(new_light_status,id))
    connection.commit()
    cursor.close()
    connection.close()

def upload_door_status(id,new_door_status):
    connection = pymysql.connect(user="root", password="", host="localhost", database="rnds")
    sql= "UPDATE rnds.users set doorStatus = %s  WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(sql,(new_door_status,id))
    connection.commit()
    cursor.close()
    connection.close()


def get_user_id(id):
    id1 = show_id(id)[0]
    return id1

def get_light_id(id):
    light_id = show_id(id)[1]
    return light_id

def get_light_status(id):
    light_status = show_id(id)[2]
    return light_status

def get_user_status(id):
    status = show_id(id)[3]
    return status

def get_user_flag(id):
    flag=show_id(id)[4]
    return flag

def get_user_door_status(id):
    door_status = show_id(id)[5]
    return  door_status

def get_light_preference(id):

    return get_user_preference(id)[0]
    
def get_door_preference(id):

    return get_user_preference(id)[1]








if __name__ == "__main__":
   # connection = pymysql.connect(user="root", password="", host="localhost", database="rnds")

    print(get_user_door_status('1'))
    id='2'
    on= '1'
    off= '0'
    close = 1
    open = 0
    upload_door_status('1',1)

    print(get_light_preference('1'))
    """
   
    a = getNoiseLevel(1)
    print(a)
    users = all_users()
    print(users)
    user_settings1 = get_user_setting('1_1')
    print(user_settings1)
    put_user_setting(1, 0, 0, 4, '1_1')
    user_settings1 = get_user_setting('1_1')
    print(user_settings1)
    Availablestatuses = statuses()
    print(Availablestatuses)

    put_user_status('1', '1_4')

    # put_user_setting(1, 0, 0, 3,'shopping at supermarket', '1_1')
    user_settings2 = get_user_setting2('1_1')
    print(user_settings2)
    """

