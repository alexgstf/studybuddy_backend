import jwt
from functools import wraps
from flask import Blueprint, request, jsonify, current_app, g
from flask_restful import Api, Resource
from datetime import datetime, timedelta
from model.post import Post
from model.channel import Channel
from api.jwt_authorize import token_required

# Blueprint for the Post API
post_api = Blueprint('post_api', __name__, url_prefix='/api')
api = Api(post_api)

# JWT token decorator for protecting routes
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message': 'Token is missing'}), 403
        
        try:
            decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            g.current_user = decoded_token['user_id']  # Assuming user_id is saved in the token
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 403
        
        return f(*args, **kwargs)
    return decorated_function

# Helper function to generate JWT tokens
def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

# Post API with CRUD operations
class PostAPI:
    class _CRUD(Resource):
        @token_required()
        def post(self):
            """
            Create a new post.
            """
            current_user = g.current_user
            data = request.get_json()

            # Validate the presence of required keys
            if not data:
                return {'message': 'No input data provided'}, 400
            if 'title' not in data:
                return {'message': 'Post title is required'}, 400
            if 'comment' not in data:
                return {'message': 'Post comment is required'}, 400
            if 'channel_id' not in data:
                return {'message': 'Channel ID is required'}, 400
            if 'content' not in data:
                data['content'] = {}  # Ensure default value for content if not provided

            post = Post(data['title'], data['comment'], current_user.id, data['channel_id'], data['content'])
            post.create()
            return jsonify(post.read())

        @token_required()
        def get(self):
            """
            Retrieve a single post by ID.
            """
            data = request.get_json()
            if data is None or 'id' not in data:
                return {'message': 'Post ID not found'}, 400
            post = Post.query.get(data['id'])
            if post is None:
                return {'message': 'Post not found'}, 404
            return jsonify(post.read())

        @token_required()
        def put(self):
            """
            Update a post.
            """
            current_user = g.current_user
            data = request.get_json()
            post = Post.query.get(data['id'])
            if post is None:
                return {'message': 'Post not found'}, 404

            post._title = data['title']
            post._content = data['content']
            post._channel_id = data['channel_id']
            post.update()
            return jsonify(post.read())

        @token_required()
        def delete(self):
            """
            Delete a post.
            """
            current_user = g.current_user
            data = request.get_json()
            post = Post.query.get(data['id'])
            if post is None:
                return {'message': 'Post not found'}, 404
            post.delete()
            return jsonify({"message": "Post deleted"})

    class _USER(Resource):
        @token_required()
        def get(self):
            """
            Retrieve all posts by the current user.
            """
            current_user = g.current_user
            posts = Post.query.filter(Post._user_id == current_user.id).all()
            json_ready = [post.read() for post in posts]
            return jsonify(json_ready)

    class _BULK_CRUD(Resource):
        def post(self):
            """
            Handle bulk post creation by sending POST requests to the single post endpoint.
            """
            posts = request.get_json()
            if not isinstance(posts, list):
                return {'message': 'Expected a list of post data'}, 400

            results = {'errors': [], 'success_count': 0, 'error_count': 0}

            with current_app.test_client() as client:
                for post in posts:
                    response = client.post('/api/post', json=post)
                    if response.status_code == 200:
                        results['success_count'] += 1
                    else:
                        results['errors'].append(response.get_json())
                        results['error_count'] += 1

            return jsonify(results)

        def get(self):
            """
            Retrieve all posts.
            """
            posts = Post.query.all()
            json_ready = [post.read() for post in posts]
            return jsonify(json_ready)

    class _FILTER(Resource):
        @token_required()
        def post(self):
            """
            Retrieve all posts by channel ID and user ID.
            """
            data = request.get_json()
            if not data or 'channel_id' not in data:
                return {'message': 'Channel and User data not found'}, 400

            posts = Post.query.filter_by(_channel_id=data['channel_id']).all()
            json_ready = [post.read() for post in posts]
            return jsonify(json_ready)

    # Registering the resources with the API
    api.add_resource(_CRUD, '/post')
    api.add_resource(_USER, '/post/user')
    api.add_resource(_BULK_CRUD, '/posts')
    api.add_resource(_FILTER, '/posts/filter')
