from flask import Flask
import redis
from database import db
from models.user import User
import psycopg2
from config import ProductionConfig

app = Flask(__name__)
redis_store = redis.Redis(host="redis", db=0, decode_responses=True)

db.init_app(app)
# conn = psycopg2.connect(database='demo',user='postgres',password='xtyy123',host='127.0.0.1')
app.config.from_object(ProductionConfig)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xtyy123@postgres:5432/postgres'
#app.config['SQLALCHEMY_ECHO'] = False
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/index/<int:user_id>')
def index(user_id):
    count = redis_store.incr('count')
    #count = 1
    user = User.query.filter(User.id == user_id).first()
    if not user:
        return 'hello , you have visit this page {} times'.format(count)
    return 'hello {}, you have visit this page {} times'.format(user.name, count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

