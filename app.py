# app.py
from flask import Flask, render_template, Response, redirect, request, session, url_for
from camera import generate_frames
from authlib.integrations.flask_client import OAuth
from functools import wraps
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Auth0 configuration
oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=os.getenv('AUTH0_CLIENT_ID'),
    client_secret=os.getenv('AUTH0_CLIENT_SECRET'),
    api_base_url=f'https://{os.getenv("AUTH0_DOMAIN")}',
    access_token_url=f'https://{os.getenv("AUTH0_DOMAIN")}/oauth/token',
    authorize_url=f'https://{os.getenv("AUTH0_DOMAIN")}/authorize',
    jwks_uri=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/jwks.json',
    client_kwargs={
        'scope': 'openid profile email',
        'response_type': 'code',
        'connection': 'google-oauth2'
    },
)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    return auth0.authorize_redirect(
        redirect_uri=url_for('callback', _external=True)
    )

@app.route('/callback')
def callback():
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()
    session['profile'] = userinfo
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    params = {
        'returnTo': url_for('index', _external=True),
        'client_id': os.getenv('AUTH0_CLIENT_ID')
    }
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

@app.route('/dashboard')
@requires_auth
def dashboard():
    return f'Welcome {session["profile"]["name"]}! <a href="/logout">Logout</a>'

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/wardrobe')
def wardrobe():
    return render_template('wardrobe.html')

if __name__ == '__main__':
    app.run(debug=True)