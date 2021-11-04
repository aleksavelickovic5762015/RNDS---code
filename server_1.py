from flask import Flask, jsonify, abort, request,json, Response, render_template
import db_int



app = Flask(__name__)


##INIZIO SELENA####
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users')
def api_users():
    users=db_int.all_users()
    return jsonify(users)


@app.route('/users/<name>')
def api_user(name):
    users = db_int.all_users()
    user = []
    for u in users:
        if u['userID'] == name:
            user.append(u)
    if len(user) == 1:
        return jsonify(user)
    else:
        response = jsonify({ 'message': "Invalid user "+name })
        response.status_code = 404
        return response


@app.route('/users', methods=['POST'])
def api_create_user():
    if request.headers['Content-Type'] == 'application/json':
        new_user = request.json
        users.append(new_user)
    else:
        response = jsonify({ 'message': "Invalid Request"})
        response.status_code = 404
        return response


@app.route('/usersettings/<userstatus>')
def api_usersettings(userstatus):
    settings = db_int.get_user_setting2(userstatus)
    print ("aaaa/n/n ", settings)
    """if len(settings) == 1:
        return jsonify(settings)
    else:
        response = jsonify({ 'message': "Invalid user "+name })
        response.status_code = 404
        return response"""
    return jsonify(settings)

@app.route('/statuses')
def api_statuses():
    Stat=db_int.statuses()
    return jsonify(Stat)

@app.route('/statuses/<userID>/<newUserStatus>', methods=['PUT'])
def api_updateUserSettings(userID, newUserStatus):
    db_int.put_user_status(userID, newUserStatus)
    return Response(status=200)


@app.route('/usersettings/<userstatus>', methods=['PUT'])
def api_usepdateUserStatus(userstatus):
    newUserSettings = request.json;
    print (newUserSettings)
    UserStatus = db_int.put_user_setting2(userstatus,newUserSettings )
    return Response(status=200)

@app.route('/noiseLevel/<usersID>')
def api_noiseLevel(usersID):
    noiseLevel = db_int.getNoiseLevel(usersID)
    print("pre-jason noiselevel", noiseLevel)
    a = jsonify(noiseLevel)
    #print ("noiselevel", a)
    return a;

@app.route('/userNoiseCheck/<usersID>', methods=['PUT'])
def api_userNoiseCheck(usersID):
    newUserNoiseCheck = request.json
    maxDB= db_int.getUserNoiseLevel(usersID)
    print ("other user's preferred value", maxDB["dbMax"])
    print ("actual user value", newUserNoiseCheck['dB_VALUE'])
    if int(newUserNoiseCheck['dB_VALUE']) > int(maxDB["dbMax"]):
        flag = 1
        db_int.putIsDisturbing(usersID,flag)
    else:
        flag = 0
        db_int.putIsDisturbing(usersID,flag)
    print ("isDisturbing value updated for user " + usersID + " with value" + str(flag))
    return Response(status=200)

##FINE SELENA####

#ANDREA


@app.route('/hue_bulb_users/<id>', methods =['GET'])
def get_user(id):
    user_inf = db_int.show_id(id)
    user_id=db_int.get_user_id(id)
    light_id=db_int.get_light_id(id)
    light_status = db_int.get_light_status(id)
    user_status = db_int.get_user_status(id)
    user_flag = db_int.get_user_flag(id)
    user_door_status = db_int.get_user_door_status(id)
    if user_inf is None:
        abort(404)
    user = {'id':user_id,'light_id':light_id,'light_status':light_status,'user_status':user_status,'user_flag':user_flag,'user_door_status':user_door_status }
    # convert the task in a JSON representation
    return jsonify(user)

@app.route('/hue_bulb_users/<id>/preference', methods =['GET'])

def light_preference(id):

    light_preference = db_int.get_light_preference(id)
    door_preference = db_int.get_door_preference(id)
    preference = {'user_light_preference': light_preference, 'user_door_preference': door_preference  }
    if light_preference is None:
        abort(404)
    return jsonify(preference)




@app.route('/hue_bulb_users/<id>', methods=['PUT'])

def update_light_status(id):

    user = request.json
    #if user is not None and ('id' and 'light_status') in user:

    new_status = user['light_status']
    db_int.upload_light_status(id,new_status)

    new_door = user['user_door_status']
    db_int.upload_door_status(id,new_door)

    return ' '


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 8080, debug = True)
