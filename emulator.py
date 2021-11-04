""""
Created on Apr 4, 2014
Updated on May 16, 2018
@author: Dario Bonino
@author: Luigi De Russis
Copyright (c) 2014-2018 Dario Bonino and Luigi De Russis

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
"""

import rest
import time
import caller


def check_user(id,light_id, flag, status, light_state, door_status):
            """
            print('flag',flag)
            print('light',light_state)
            print('status',status)

            """

            url_to_call = lights_url + light_id + '/state'

            if flag == 0:

                if status == 1 and light_state != 1:
                    body = '{ "on": true, "hue" : 0, "bri": 245, "sat": 0,"transitiontime": 0}'
                    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
                    new_status = rest.send(url=lights_url + light_id)

                    if new_status['state']['on'] == True:
                        light = 1


                    elif new_status['state']['on'] == False:
                        light = 0



                    caller.upload_light_status(id,light)



                if status == 0 and light_state != 0:
                    body = '{ "on": false ,"transitiontime": 0}'
                    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

                    new_status = rest.send(url=lights_url + light_id)



                    if new_status['state']['on'] == True:
                        light = 1

                    elif new_status['state']['on'] == False:
                        light = 0

                    caller.upload_light_status(id,light)



            elif flag == 1 and door_status == 1:

                # allarm
                for j in range(0, 1):
                    body = '{ "on" : true, "hue" : 0, "sat":200, "bri":254,"transitiontime": 0}'
                    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
                    time.sleep(0.5)

                for j in range(0, 1):
                    body = '{ "on" : false, "hue" : 0, "sat":200,"bri":254,"transitiontime": 0 }'
                    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
                    time.sleep(0.5)

                new_status =3

                caller.upload_light_status(id, new_status)





if __name__ == '__main__':
    # the base URL

    base_url = 'http://192.168.0.201'
    username = '5PwJW21H0f2-oaPzcB7mPfFyhd9RVOZElLPeOCfb'
    """
    # if you are using the emulator, probably the base_url will be:
    base_url = 'http://localhost:8000'
    username = 'newdeveloper'
    """
    # lights URL
    lights_url = base_url + '/api/' + username + '/lights/'
    all_the_lights = rest.send(url=lights_url)


    if type(all_the_lights) is dict:


        for i in range(0, 2):

            id = str(i + 1)
            user = caller.one_user(id)
            print(user)
            light_id = str(user['light_id'])
            url_to_call = lights_url + light_id + '/state'
            body = '{ "on" : false ,"transitiontime": 0}'
            rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
            caller.upload_light_status(str(i + 1), 0)

        while True:

            for i in range(0, 2):

                id = str(i+1)
                #print('id=',id)
                user = caller.one_user(id)
                #print(user)
                light_state = user['light_status']
                user_flag = user['user_flag']
                light_status = user['light_status']
                user_status = caller.light_preference(id)
                light_id = str(user['light_id'])
                door_status = caller.get_user_door_status(id)

                check_user(id,light_id, user_flag, user_status, light_status,door_status)


    else:
            print('Error:', all_the_lights[0]['error'])












