from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, home_views, setting_views, learning_views,simulation_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(home_views.bp)
    app.register_blueprint(simulation_views.bp)
    app.register_blueprint(setting_views.bp)
    app.register_blueprint(learning_views.bp)

    return app

