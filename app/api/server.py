from flask import render_template, request, url_for
from app.db_model import User, VideoUser, PaperUser, StoryUser

from app.create_app import run_app, db



app = run_app(os.getenv("ENV") or 'dev')

@app.route('/home')
def home():
	video = VideoUser.query.all()
	return render_template("templates/home.html", video=video)


@app.route('/register', methods=["POST"])
def register():
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	interesting_field = request.form['interesting_field']

	user = User.query.filter_by(email=email).first()

	if not user :
		new_user = User(username=username, email=email, password=password, interesting_field=interesting_field)
		db.session.add(new_user)
		db.session.commit()
		return render_template('templates/users/register_succes.html')
	if user :
		return "user is available"

	return render_template('templates/users/register.html')

@app.route('/login', methods=["GET"])
def login():
	email = request.form['email']
	password = request.form['password']

	user = User.query.filter_by(email=email).first()

	if user :
		return render_template('templates/users/user_dashboard.html', user=user)
	if not user:
		return "account is not available"

	return render_template('templates/users/login.html')

@app.route('/user/<int:user_id>/edit_profil')
def edit_profil(user_id):
	





