import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# cred = credentials.Certificate("serviceaccount.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': "Firebase db link paste here"
# })

ref = db.reference('Students')

data = {
    "000000":
        {
            "name": "Asher Javed",
            "Dept": "CS",
            "starting_year": 2019,
            "total_attendance": 2,
            "standing": "G",
            "year": "4th",
            "last_attendance_time": "2022-12-21 01:06:55"
        },
    "000000":
        {
            "name": "Syed Saqib Ali",
            "Dept": "IT",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "G",
            "year": "3rd",
            "last_attendance_time": "2022-12-21 01:08:9"
        },
    "000000":
        {
            "name": "Agha Kashif Raza",
            "Dept": "CS",
            "starting_year": 2019,
            "total_attendance": 9,
            "standing": "G",
            "year": "4th",
            "last_attendance_time": "2022-12-21 01:13:00"
        }
}
for key, value in data.items():
    ref.child(key).set(value)