import os

SECRET_KEY = 'dfasfj9wer@45635sdG#!#TAY&()@$VCb3563rsdgfsa#$%34'

# MySql settings
DB_USER = os.environ.get("DB_USER") or 'myuser'
DB_PASSWORD = os.environ.get("DB_USER") or '123456'
DB_HOST = os.environ.get("DB_HOST") or '127.0.0.1'
DB_PORT = os.environ.get("DB_PORT") or '3306'
DB_URL = os.environ.get('DB_ULR') or f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/notes"

