import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  # set a secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER', '')  # the email server 'smtp.qq.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '') # use this email account to send message 'xxx@xxx.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')  # your email acount will get you a authentication code
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = ''  # 'name <xxx@xxx.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN', '')  # flasky set admin acount according to this setting 'xxx@xxx.com'
    FLASKY_POSTS_PER_PAGE = os.environ.get('FLASKY_POSTS_PER_PAGE', 20)
    FLASKY_FOLLOWERS_PER_PAGE = os.environ.get('FLASKY_FOLLOWERS_PER_PAGE', 20)
    FLASKY_COMMENTS_PER_PAGE = os.environ.get('FLASKY_COMMENTS_PER_PAGE', 20)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

