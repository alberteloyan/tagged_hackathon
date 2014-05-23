#!flask/bin/python
"""
    Flask front controller for Tagged
"""

#load third-party dependencies
from flask import Flask, request, jsonify, Response
import logging
import json

#load project dependencies
import config
import controllers.meetme as meetme

#Initializing
sys_logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(config.DefaultConfig)

#just a test route
@app.route('/')
def test():
    sys_logger.info('Testing logging')
    return jsonify({'status':'ok'})

#get meetme suggestions for a given uid
@app.route('/tagged/api/1/meetme/<int:uid>/browse', methods = ['GET'])
def get_suggestions(uid):
    params = {
        'uid'   :   uid
    }
    #call handler
    result = meetme.get_suggestions(request, params)

    #TODO - generate response
    response = json.dumps([result])
    return Response(response, mimetype='text/html')

#get meetme suggestions for a given uid
@app.route('/tagged/api/1/meetme/<int:uid>/interested/<int:tuid>', methods = ['POST'])
def vote(uid, tuid):
    params = {
        'uid'   : uid,
        'tuid'  : tuid
    }

    #call handler
    result = meetme.vote(request, params)

    #TODO - generate response
    response = json.dumps([result])
    return Response(response, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)
