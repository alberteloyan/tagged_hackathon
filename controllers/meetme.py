# coding=utf-8
import requests

from flask import request

def get_suggestions(request, params):
    """
        This will actually make the connection to tagged system
        :param uid — tagged id of the user for whom we are getting suggestions
    """
    #TODO - for now just return
    uid = params.get('uid')


    #session_token = request.cookies.get('S')
    #assert session_token == request.args.get('session_token')

    session_token = request.args.get('session_token')

    data = {
        'method'    : 'tagged.apps.meetme.browse',
        'limit'         : 10,
        'gender'        : 'm',
        'min_age'       : 18,
        'max_age'       : 25,
        'country'       : 'us',
        'distance'      : '50',
        # 'location'      : false,
        # 'location_nd'   : false,
        # 'newlocation'   : false,
        # 'newlocation_id': false,
        'counter'       : 3,
        'reset'         : 'true',
        # 'init_uid'      : false,
        # 'debug'         : false,
        # 'return_as'     : false,
        'clear_alert'   : 'true',
        # 'it_model'      : array('required' : false, 'filter' : 'string'),
        # 'ethnicity'     : array('required' : false, 'filter' : 'filterEthnicity', 'class' : 'search'),
        'counts'        : 'true'
    }

    args = {
        'application_id' : 'user',
        'session_token'  : session_token,
        'format'         : 'JSON',
    }

    cookies = {
        'S' : session_token
    }
    response = requests.post('http://www.tag-local.com/api/', data, cookies = cookies, params=args)
    print(response.text)

    if not response:
        return False

    return response.json()
