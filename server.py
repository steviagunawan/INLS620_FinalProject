from flask import (Flask, Response, request, render_template, make_response,
                   redirect)
from flask_restful import Api, Resource, reqparse, abort

import json
import random
import string
from datetime import datetime
from functools import wraps

with open('data.json') as data:
    data = json.load(data)

def generate_id(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def error_if_review_not_found(review_id,game_id):
    if review_id not in data['games'][game_id]['reviews']:
        message = "No review with ID: {}".format(review_id)
        abort(404, message=message)

def error_if_game_not_found(game_id):
    if game_id not in data['games']:
        message = "No game with ID: {}".format(game_id)
        abort(404, message=message)
# def render_review_list_as_html(reviews):
#     return render_template(
#         'reviewList.html',
#         reviews=reviews)
#
# def render_review_as_html(review):
#     return render_template(
#         'review.html',
#         review = review)

# The next three functions implement simple authentication.

# Check that username and password are OK; DON'T DO THIS FOR REAL
def check_auth(username, password):
    return username == 'admin' and password == 'secret'

# Issue an authentication challenge
def authenticate():
    return Response(
        'Please authenticate yourself', 401,
        {'WWW-Authenticate': 'Basic realm="helpdesk"'})

# Decorator for methods that require authentication
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def nonempty_string(x):
    s = str(x)
    if len(x) == 0:
        raise ValueError('string is empty')
    return s

new_reviewList_parser = reqparse.RequestParser()
for arg in ['author', 'review_name', 'text']:
    new_reviewList_parser.add_argument(
        arg, type=nonempty_string, required=True,
        help="'{}' is a required value".format(arg))

new_gameList_parser = reqparse.RequestParser()
for arg in ['title', 'description']:
    new_gameList_parser.add_argument(
        arg, type=nonempty_string, required=True,
        help="'{}' is a required value".format(arg))

update_review_parser = reqparse.RequestParser()
update_review_parser.add_argument(
    'comment', type=str, default='')

update_gameDesc_parser = reqparse.RequestParser()
update_gameDesc_parser.add_argument(
    'description', type=str, default='')

class UserList (Resource):

    def get(self):
        return make_response(render_template('userList.html',users=data['users']),200)


class User (Resource):

    def get(self,user_id):
        return make_response(render_template('user.html', users = data['users'][user_id]),200)


class GameList (Resource):

    def get(self):
        return make_response(render_template('gameList.html', games=data['games']),200)

    def post(self):
        games = new_gameList_parser.parse_args()
        game_id = generate_id()
        games['date'] = datetime.isoformat(datetime.now())
        games['game_id'] = game_id
        games['reviews'] = {}
        data['games'][game_id]= games
        return make_response(render_template('gameList.html', games=data['games']), 200)


class Game (Resource):

    def get(self,game_id):
        error_if_game_not_found(game_id)
        return make_response(render_template('game.html',games=data['games'][game_id]),200)

    def patch(self, game_id):
        error_if_game_not_found(game_id)
        game =data['games'][game_id]
        update = update_gameDesc_parser.parse_args()
        if len(update['description'].strip()) > 0:
            game.setdefault('description_update', []).append(update['description'])
            # data['games'][game_id]['description'] = update['description']
        return make_response(render_template('game.html', games=data['games'][game_id]), 200)


class ReviewList(Resource):

    def get(self,game_id):
        return make_response(render_template('reviewList.html', reviews=data['games'][game_id]['reviews'], games=data['games'][game_id]),200)

    def post(self,game_id):
        reviews = new_reviewList_parser.parse_args()
        review_id = generate_id()
        reviews['date'] = datetime.isoformat(datetime.now())
        reviews['review_id'] = review_id
        data['games'][game_id]['reviews'][review_id] = reviews
        return make_response(render_template('reviewList.html', reviews=data['games'][game_id]['reviews'], games=data['games'][game_id]),200)


class Review(Resource):

    def get(self,review_id,game_id):
        error_if_review_not_found(review_id,game_id)
        return make_response(render_template('review.html', reviews=data['games'][game_id]['reviews'][review_id],games=data['games'][game_id]),200)


    def patch(self, review_id, game_id):
        error_if_review_not_found(review_id,game_id)
        reviews=data['games'][game_id]['reviews'][review_id]
        update = update_review_parser.parse_args()
        if len(update['comment'].strip()) > 0:
            reviews.setdefault('comments', []).append(update['comment'])
        return make_response(render_template('review.html', reviews=data['games'][game_id]['reviews'][review_id],games=data['games'][game_id]),200)


app = Flask(__name__)
api = Api(app)
api.add_resource(ReviewList, '/reviews/<string:game_id>')
api.add_resource(Review, '/reviews/<string:game_id>/<string:review_id>')
api.add_resource(GameList,'/games')
api.add_resource(Game, '/games/<string:game_id>')
api.add_resource(UserList,'/users')
api.add_resource(User,'/users/<string:user_id>')


@app.route('/')
def index():
    return redirect(api.url_for(UserList), code=303)

@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add(
        'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5555,
        debug=True,
        use_debugger=False,
        use_reloader=False)
