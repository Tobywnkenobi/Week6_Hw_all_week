import os

class Config:
  PROPAGATE_EXCEPTIONS = True
  API_TITLE = 'Matrix_130'
  API_VERSION = 'v1'
  OPENAPI_VERSION = '3.0.3'
  OPENAPI_URL_PREFIX = '/'
  OPENAPI_SWAGGER_UI_PATH = '/'
  OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
  SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://tvxgnhnw:oK3fjFzN0H_gpNe7z-SVk37cSJ3JlcQ3@rajje.db.elephantsql.com/tvxgnhnw')


#   e2621725-fe3d-48f1-9068-2868c038eee0