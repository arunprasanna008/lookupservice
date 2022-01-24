from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine

# URL Lookup service URL
API_PREFIX = 'urlinfo/1'

# Initiates the database
engine = create_engine('sqlite:///malware.db', case_sensitive=False)

# Flask for the webservice
app = Flask(__name__)
api = Api(app)

class CheckUrl(Resource):

    @staticmethod
    # method to connect, and query from the database
    def sql_query(sql='', params=''):
        if sql:
            query = None
            try:
                connection = engine.connect()

                if params:
                    query = connection.execute(sql, params)
                else:
                    query = connection.execute(sql)
                return query.cursor.fetchall()

            finally:
                if query:
                    query.cursor.close()
        else:
            pass


    def get(self, path):
        global API_PREFIX
        api_path = [API_PREFIX, API_PREFIX + '/']
        result = {'error': False}
        sql = []
        url = path.split('/')

        # return the whole database when this page is requested
        if path in api_path:
            sql.append("select domain, uri from malware")
        # builds the query for a specific valid requests
        elif path.startswith(API_PREFIX):
            try:
                host, uri = url[2], '/' + '/'.join(url[3:])
            except IndexError:
                host, uri = url[2], '/'

            sql.append("select domain, uri, result from malware "
                       "where domain=(:host) and uri=(:uri)")
            sql.append((host, uri,))
        else:
            # handles invalid requests
            result['error'] = True
            result['message'] = 'bad request'
            return result, 400

        # retrives information from the database
        output = self.sql_query(*sql)

        # builds the response
        if path in api_path:
            result['urls'] = [i[0] + i[1] for i in output]
        else:
            # response for url in database
            try:
                result['url'] = output[0][0] + output[0][1]
                result['reputation'] = output[0][2]
            # response for a url that is not in database, we are allowing it since it is not identified to be a malware yet
            except IndexError as e:
                result['url'] = host + uri
                result['reputation'] = 'OK'
                result['error'] = True
                result['message'] = 'passing since ' + host + uri + ' not found in database'

        return result, 200

api.add_resource(CheckUrl, '/<path:path>')

if __name__ == '__main__':
    app.run()