import requests,json

"""
Example file for calling the API
Uses the "requests" module for HTTP calls
"""
#ami
#base_url = 'http://192.168.0.7:8080'

base_url = 'http://192.168.43.79:8080'



def one_user(name):
    url = base_url + '/hue_bulb_users/' + name
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    else:
        return 'fetch one user did not work'

def get_user_preference(name):
    url = base_url + '/hue_bulb_users/' + name +'/preference'

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    else:
        return 'fetch one user did not work'

def get_user_id(id):
    id = one_user(id)['userID']
    return id
def get_user_flag(id):
    flag=one_user(id)['user_flag']
    return flag

def get_light_id(id):
    light_id = one_user(id)['light_id']
    return light_id

def get_light_status(id):
    light_status = one_user(id)['light_status']
    return light_status

def get_user_status(id):
    status = one_user(id)['user_status']
    return status

def get_user_door_status(id):

    door_status = one_user(id)['user_door_status']
    return door_status

def upload_light_status(id,newstatus):

    url = base_url + '/hue_bulb_users/' + id
    user = one_user(id)
    user["light_status"] = newstatus
    return requests.put(url, json = user)

def upload_door_status(id,newstatus):

    url = base_url + '/hue_bulb_users/' + id
    user = one_user(id)
    user["user_door_status"] = newstatus
    print(user)
    return requests.put(url, json = user)



def light_preference(id):
    return get_user_preference(id)['user_light_preference']

def door_preference(id):
    return get_user_preference(id)['user_door_preference']

    #user = {'id': get_user_id(id), 'light_id': get_light_id(id),'light_status': newstatus,'user_flag':get_user_flag(id),'user_status':get_user_status(id)}


if __name__ == '__main__':






    """
    
    
    print(get_user_preference('1'))
    print('aaa',light_preference('1'))
    print('bbb',door_preference('1'))

    print(get_user_door_status('2'))
    print(one_user('2'))
    upload_light_staus('2',0)
    upload_light_staus('2',1)
    print(get_light_status('2'))
    print(one_user('2'))
    print(get_user_flag('2'))
    print(get_user_status('2'))
    print('luce',get_light_id('1'))


    if get_user_status('2')=='2_2':
        print('ok')
    """