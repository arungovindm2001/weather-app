from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('secret_key')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/city", methods=["POST", "GET"])
def city():
    if request.method == "POST":
        cityname = request.form["city"]

        api_key = os.environ.get('api_key')

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_url + "q=" + cityname + "&appid=" + api_key

        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            currentTemperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            return(
                " Temperature : " + str(currentTemperature - 273.15) + u"\N{DEGREE SIGN}" + "C" + "<br>" +
                "Atmospheric pressure : " + str(current_pressure) + " hPa" + "<br>" +
                "Humidity : " + str(current_humidiy) + "%" + "<br>" +
                "Description : " + str(weather_description)
            )
        else:
            return "City Not Found"
    else:
        return render_template("city.html")


if __name__ == "__main__":
    app.run(debug=True)
