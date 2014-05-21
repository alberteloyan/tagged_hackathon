# coding=utf-8
import requests

def get_suggestions(request, params):
    """
        This will actually make the connection to tagged system
        :param uid — tagged id of the user for whom we are getting suggestions
    """
    #TODO - for now just return
    uid = params.get('uid')

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
    cookies = {
        'S' : 'too9n3nrafqiq4io9umaor0314'
    }
    response = requests.post('http://www.tag-local.com/api/?application_id=user&format=JSON&session_token=too9n3nrafqiq4io9umaor0314', data, cookies = cookies
    print(response.text)

    if not response:
        return False

    return response.json()
