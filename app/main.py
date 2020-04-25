from application.api import api
from application.routes.healthcheck import healthcheck
from application.routes.plane_api import plane_api

api.register_blueprint(plane_api)
api.register_blueprint(healthcheck)

if __name__ == "__main__":
    # Only for debugging while developing
    api.run(host="0.0.0.0", debug=True, port=80, use_reloader=True)
