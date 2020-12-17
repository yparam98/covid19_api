from flask_restful import Resource, reqparse
import pandas as pd
import json

import utils


class PercentPositive(Resource):
    """ positive cases class """

    def get(self):

        data_obj = utils.csv_to_json('percent_positive_by_agegrp.csv', 20)

        # data = json.dumps(data_obj)  # convert dataframe to dictionary

        return {
                   'data': data_obj
               }, 200  # return data & 200 OK code...
