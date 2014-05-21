import requests

def get_suggestions(uid):
    """
        This will actually make the connection to tagged system
        :param uid — tagged id of the user for whom we are getting suggestions
    """
    #TODO - for now just return

    data = {
        'method'    : 'tagged.apps.meetme.browse',
        'limit'     : '15',
        'counter'   : '0',
        'track'     : '123',
    }
    response = requests.post('https://tagged.com/api/index.html', data)

    if not response:
        return False

    return response.get('results')
