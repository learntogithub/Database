from flask import Flask
from .confi import app_config
from .models import db, bcrypt
def create_app(env_name):
	#app initiliazation 
	app = Flask(__name__)

	app.config.from_object(app_config[env_name])

	bcrypt.init_app(app)
	db.init_app(app)

	@app.route('/', methods=['GET'])
	def index():
		return 'Connection successed'

	return app




