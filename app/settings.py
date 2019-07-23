from environs import Env

env = Env()
env.read_env()

with env.prefixed('APP_'):
    APP_NAME = env.str('NAME', 'pShopChannel')
    APP_SLOGAN = env.str('SLOGAN', 'A Robust Storefront CMS.')
    APP_URL = env.str('URL', 'https://example.com')
    # python -c "import uuid; print(uuid.uuid4().hex);"
    SECRET_KEY = env.str('SECRET_KEY')

with env.prefixed('SOCIAL_'):
    SOCIAL_TWITTER = env.str('TWITTER', '')
    SOCIAL_FACEBOOK = env.str('FACEBOOK', '')

with env.prefixed('DATABASE_'):
    SQLALCHEMY_DATABASE_URI = env.str('URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
