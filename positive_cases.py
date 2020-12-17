from flask_restful import Resource, reqparse
import pandas as pd
import json

import utils


class PositiveCases(Resource):
    """ positive cases class """

    def get(self):
        # parser = reqparse.RequestParser()
        #
        # parser.add_argument('rows', required=True)
        #
        # args = parser.parse_args()
        #
        # new_data = pd.DataFrame({
        #     'rows': args['rows']
        # })

        data_obj = utils.csv_to_json('conposcovidloc.csv', 20)

        # data = pd.read_csv('conposcovidloc.csv')  # read CSV

        data = json.dumps(data_obj)  # convert dataframe to dictionary

        return {
                   'data': data_obj
               }, 200  # return data & 200 OK code...
