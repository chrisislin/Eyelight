import pyrebase
from flask import *

app = Flask(__name__)
config = {
  # confidential
  "apiKey": "AIzaSyBfJeaQjeU2q_g1zaC_rvJ2D2jEDq58umI",
  "authDomain": "eyelight-vids.firebaseapp.com",
  "databaseURL": "https://eyelight-vids.firebaseio.com",
  "projectId": "eyelight-vids",
  "storageBucket": "eyelight-vids.appspot.com",
  "messagingSenderId": "359657414936",
  "appId": "1:359657414936:web:f24f7ad0acd3a27a2afe6d",
  "measurementId": "G-RHHY80M6DP"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])

def basic():
	unsuccessful = 'Incorrect email or password entered'
	successful = 'Login successful'
	if request.method == 'POST':
		email = request.form['name']
		password = request.form['pass']
		try:
			auth.sign_in_with_email_and_password(email, password)
			return render_template('login.html', s=successful)
		except:
			return render_template('login.html', us=unsuccessful)

	return render_template('login.html')


if __name__ == '__main__':
	app.run()

# email = input('Please enter your email\n')
# password = input('Please enter your password\n')
# user = auth.create_user_with_email_and_password(email, password)
# user = auth.sign_in_with_email_and_password(email, password)
# auth.send_email_verification(user['idToken'])
# print(auth.get_account_info(user['idToken']))
