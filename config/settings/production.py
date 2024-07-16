DEBUG = False

ALLOWED_HOSTS = ["https://linopandemic.com"]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = ["https://d7cu5e2dioocp.cloudfront.net/videos"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = ["https://d7cu5e2dioocp.cloudfront.net/videos"]
