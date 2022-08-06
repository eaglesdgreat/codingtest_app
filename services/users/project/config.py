import os
class BaseConfig:
    """Base configurations"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(BaseConfig):
    """Development configurations"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """Testing configurations"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
    TESTING = True
    
class ProductionConfig(BaseConfig):
    """Production configurations"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')