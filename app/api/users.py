from flask_restful import Resource


class UserAPi(Resource):
    def get(self):
        return "GET /api/users"

    def post(self):
        return "POST /api/users"
