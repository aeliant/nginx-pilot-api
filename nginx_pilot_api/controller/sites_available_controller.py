# coding=utf-8
from flask import request
from flask_restplus import Resource


class SiteCollection(Resource):
    def get(self):
        pass

    def post(self):
        pass


class SiteItem(Resource):
    def get(self, public_id):
        pass

    def put(self, public_id):
        pass

    def delete(self, public_id):
        pass
