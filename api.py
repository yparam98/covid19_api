from flask import Flask
from flask_restful import Api
import ast

from positive_cases import PositiveCases
from percent_positive import PercentPositive

app = Flask(__name__)
api = Api(app)

api.add_resource(PositiveCases, '/covid_api/positive_cases')
api.add_resource(PercentPositive, '/percent_positive')


if __name__ == '__main__':
    app.run()   # run out Flask app




