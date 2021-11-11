from flask import blueprints


api = blueprint('api',__name__, url_prefix='/api' )

@api.route('/getdata')
def getdata():
    return { 'some': "value"}