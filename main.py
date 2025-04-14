from flask import Flask
from flask_cors import CORS
from API.config import Config
from API.routes import routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

cors_origins = os.getenv("CORS_ORIGINS", "*").split(",")
CORS(app, origins=cors_origins)

app.register_blueprint(routes)

if __name__ == '__main__':
    host = "0.0.0.0"
    port = int(os.getenv("PORT", 5000))

    debug_mode = os.getenv("FLASK_ENV", "production") == "development"

    app.run(host=host, port=port, debug=debug_mode)
