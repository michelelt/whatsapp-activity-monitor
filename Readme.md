## NOT maintend

# Contact Activity Monitor

## Intro
This web tool is an automatic cralwer able to store all the times a contact in your whatsapp library is online.

## Configuration
- Install Firefox
- Download geckodriver
- add to PATH the path to geckodriver
- crete a database and user on firebase
- create Configuration/config.json in the following format \
 {
  "apiKey": "A",
  "authDomain": "namedb.firebaseapp.com",
  "databaseURL": "https://namebd.firebaseio.com",
  "projectId": "namedb",
  "storageBucket": "namedb.appspot.com",
  "messagingSenderId": "B",
  "appId": "C",
  "measurementId": "D"
}
- create Configuration/cred.json in the following format \
{
  "email": "email",
  "password": "passwrod"
}

- create Data/ListOfContacts.txt a txt file with all the contacts you want to track reporting the exact
naame you saved into your device

## Run
python3 __main__.py\
scan the QR code on the browser and press enter
