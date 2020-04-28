from presentation.api import api


if __name__ == "__main__":
    # Only for debugging while developing
    api.run(host="0.0.0.0", debug=True, port=80, use_reloader=True)
