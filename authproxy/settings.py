from decouple import config, Csv

host = config('HOST', default='0.0.0.0')
port = config('PORT', default=5000, cast=int)
debug = config('DEBUG', default=False, cast=bool)
secret_key = config('SECRET_KEY')
username = config('USERNAME')
password = config('PASSWORD')
session_token = config('SESSION_TOKEN')
api_key = config('API_KEY')
