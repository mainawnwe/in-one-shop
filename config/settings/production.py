# config/settings/production.py
from .base import *
import dj_database_url
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=lambda v: [s.strip() for s in v.split(',')])
CSRF_TRUSTED_ORIGINS = ['https://in-one-shop.onrender.com']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Supabase S3 Storage Settings (အသစ်ပြင်ထားသည်) ---
AWS_ACCESS_KEY_ID = config('SUPABASE_S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = config('SUPABASE_S3_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = 'media'
AWS_S3_ENDPOINT_URL = 'https://timhwtmnyyenzseavshr.supabase.co/storage/v1/s3'
AWS_S3_REGION_NAME = 'ap-southeast-2'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_ADDRESSING_STYLE = 'path'

# ဒီ line က အရေးကြီးဆုံးပါ (Public URL အတွက်)
AWS_S3_CUSTOM_DOMAIN = 'timhwtmnyyenzseavshr.supabase.co/storage/v1/object/public/media'
# ---------------------------------------------------

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
    )
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')