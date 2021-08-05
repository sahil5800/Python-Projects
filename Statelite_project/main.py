import requests
from datetime import datetime
import smtplib

MY_LAT = 25.317644
MY_LONG = 82.973915
my_email = "kidaofspam@gmail.com"
password = "Sahil:05"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

ss_response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
ss_response.raise_for_status()

data = ss_response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
exact_time = time_now.hour

if (MY_LAT - 5 <= latitude <= MY_LAT + 5) and (MY_LONG - 5 <= longitude <= MY_LONG + 5):
    if exact_time <= sunrise or exact_time >= sunset:
        with smtplib.SMTP("smtp.gmail.com") as mail:
            mail.starttls()
            mail.login(user=my_email, password=password)
            mail.sendmail(from_addr=my_email, to_addrs="rajsahil1228@gmail.com",
                          msg="Subject:Satellite Alert\n\nLook Up")
else:
    pass



