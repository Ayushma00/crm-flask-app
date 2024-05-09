
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    AIRTABLE_KEY='this-is-secret-key'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
