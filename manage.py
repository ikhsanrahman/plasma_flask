import os
import unittest

from flask_migrate  import Migrate, MigrateCommand
from flask_script   import Manager, Shell


from app.api.routers.routers import blueprint
from waitress import serve

from app.api.create_app import create_app, db

app = create_app(os.getenv("ENV") or "dev")

app.register_blueprint(blueprint, url_prefix="/api")

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
	host = '127.0.0.1'
	#serve(app, host="0.0.0.0", port=os.getenv("PORT_ENV") or 5555)
	app.run(host=host, debug=True, port=os.getenv("PORT_ENV") or 5000)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
	manager.run()
