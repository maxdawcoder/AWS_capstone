# Used to define configs that should be used across all configurations.
class BaseConfig:
    pass

# This inherits from our base config
class DevelopmentConfig(BaseConfig):
    # We define the development database URI here. We'll use SQLite in this case.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todos.db'

class ProductionConfig(BaseConfig):
    # We define the production database URI as None temporarily till we have a production DB.
    SQLALCHEMY_DATABASE_URI = None