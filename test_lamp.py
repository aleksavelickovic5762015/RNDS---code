import rest
import time




if __name__ == '__main__':
    # the base URL
    """
    # if you are using the emulator, probably the base_url will be:
    base_url = 'http://localhost:8000'
    username = 'newdeveloper'
    """
    base_url = 'http://192.168.0.201'
    username = '5PwJW21H0f2-oaPzcB7mPfFyhd9RVOZElLPeOCfb'

    #do not change ligths url
    lights_url = base_url + '/api/' + username + '/lights/'
    all_the_lights = rest.send(url=lights_url)
    print(all_the_lights)
    light_id = '9'
    url_to_call = lights_url + light_id + '/state'
    body = '{ "on" : false }'
    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
    flag=1
   #for changing ligths you have to change ligth_id

    a=int(input())
    while a!=2:
        if a==1:
            body = '{ "on" : true }'
            rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
            a = int(input())

        if a==0:
            body = '{ "on" : false }'
            rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
            a = int(input())
    
    """
    for i in range (0,10):

        if flag == 1:
                print('ciao')
                # allarm
                for j in range(0, 1):
                    body = '{ "on" : true, "hue" : 0, "sat":200, "bri":254,"transitiontime": 0}'
                    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
                    time.sleep(1)
                for j in range(0, 1):
                    body = '{ "on" : false, "hue" : 0, "sat":200,"bri":254,"transitiontime": 0 }'
                    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
                    time.sleep(1)

   """
    body = '{ "on" : false, "hue" : 0, "sat":200,"bri":254,"transitiontime": 0 }'
    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})