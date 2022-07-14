from flask import Flask, render_template
import pyrebase
from playsound import playsound

config = {
    "apiKey": "AIzaSyBBl_HZgOR1anaymROQ_nyZ8yy1UZs4SKw",
    "authDomain": "saavdhan-3d286.firebaseapp.com",
    "databaseURL": "https://saavdhan-3d286-default-rtdb.firebaseio.com",
    "projectId": "saavdhan-3d286",
    "storageBucket": "saavdhan-3d286.appspot.com",
    "messagingSenderId": "114276883265",
    "appId": "1:114276883265:web:06a3f6af90e8228db7dfc0",
    "measurementId": "G-K37K0EDBGR"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def basic():
    data = db.child("distance").get()
    if(data.val()<=15):
        playsound('/home/yash/python_development/static/beep-02.mp3')
    return render_template('distance.html', distance=data.val())
    


if __name__ == '__main__':
    app.run(debug=True)