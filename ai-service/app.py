from flask import Flask
from routes.report import report_bp
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["30 per minute"])
app.register_blueprint(report_bp)
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)


@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)