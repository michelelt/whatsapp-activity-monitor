import json
import pyrebase

class DBManager:
    def __init__(self, config_path):

        with open('%sconfig.json' %config_path) as fp:  config = json.load(fp)
        with open('%scred.json' % config_path) as fp:  cred = json.load(fp)

        self.config = config
        self.cred = cred

        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        self.user = auth.sign_in_with_email_and_password(cred["email"], cred["password"])
        self.db = firebase.database()

    def insert_observation(self, obs):
        results = self.db.child("users").push(obs, self.user['idToken'])
