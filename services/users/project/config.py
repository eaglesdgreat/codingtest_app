class BaseConfig:
    """Base configurations"""
    TESTING = False
    
class DevelopmentConfig(BaseConfig):
    """Development configurations"""
    pass

class TestingConfig(BaseConfig):
    """Testing configurations"""
    TESTING = True
    
class ProductionConfig(BaseConfig):
    """Production configurations"""
    pass