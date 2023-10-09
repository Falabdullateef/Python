import threading

def run_nuker():
    import requests
    import string
    import json
    import os
    import random

    random_seed = (os.urandom(1024))
    chars_string = string.ascii_letters + string.digits + '!@#$%^&*()'

    url_string = 'url.com'

    names_list = json.loads(open('names.json').read())

    for name in names_list:
        name_extra = ''.join(random.choice(string.digits))

        username_string = name.lower() + name_extra + '@gmail.com'
        password_string = ''.join(random.choice(chars_string) for i in range(8))

        requests.post(url_string, allow_redirects=False, data={
            'Username_data': username_string,
            'Password_data': password_string
        })

        print 'sending username %s and password %s' % (username_string, password_string)

t = threading.Thread(target=run_nuker)
t.start()