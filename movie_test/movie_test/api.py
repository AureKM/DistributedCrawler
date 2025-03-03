from flask import Flask, jsonify
import redis
app = Flask(__name__)
redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
@app.route('/movies/<int:start>/<int:end>', methods=['GET'])
def get_movies(start, end):
    movies = redis_client.lrange('movie_test:items', start, end)
    return jsonify(movies)
if __name__ == '__main__':
    app.run(debug=True)
