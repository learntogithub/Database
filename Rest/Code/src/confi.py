import os 


class Development():
	DEBUG = True
	TESTING = False
	JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class Production():
	DEBUG = False
	TESTING = False
	JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
	'development': Development,
	'production': Production
}

