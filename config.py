class Config:
    DEBUG = True
    TESTING = True

    #Configuracion de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://BD2021:BD2021itec@143.198.156.171:3306/blog_salzotto"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True