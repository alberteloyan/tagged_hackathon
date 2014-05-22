# coding=utf-8
import requests

from flask import request

def get_suggestions(request, params):
    """
        This will actually make the connection to tagged system
        :param uid — tagged id of the user for whom we are getting suggestions
    """
    #TODO - for now just return
    #uid = params.get('uid')

    #session_token = request.cookies.get('S')
    #assert session_token == request.args.get('session_token')

    session_token = request.args.get('session_token')
    counter = request.args.get('counter')
    limit = request.args.get('limit')

    data = {
        'method'    : 'tagged.apps.meetme.browse',
        'limit'         : limit,
        'gender'        : 'm',
        'min_age'       : 18,
        'max_age'       : 25,
        'country'       : 'us',
        'distance'      : '50',
        # 'location'      : false,
        # 'location_nd'   : false,
        # 'newlocation'   : false,
        # 'newlocation_id': false,
        'counter'       : counter,
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


def vote(request, params) :
    uid             = params.get('uid')
    target_uid      = params.get('tuid')

    session_token   = request.args.get('session_token')
    interest        = request.json.get('interest')

    data = {
        'user_id'       : target_uid,
        'interest'      : interest,
        'counter'       : 2,
        'streak'        : 2,
        #'previousView'  : array('filter' : 'filterPreviousViews', 'required' : false),
        #'msgSent'       : array('filter' : 'bool', 'required' : false),
        #'clickSource'   : array('required' : false, 'filter' : 'string'),
    }

    args = {
        'method'    : 'tagged.apps.meetme.interested',
        'application_id' : 'user',
        'session_token'  : session_token,
        'format'         : 'JSON',
    }

    cookies = {
        'S' : session_token
    }

    response = requests.post('http://www.tag-local.com/api/', data, cookies = cookies, params=args)
    print(response.text)

    if not response :
        return False

    return response.json()
