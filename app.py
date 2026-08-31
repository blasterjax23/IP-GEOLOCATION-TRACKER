from flask import Flask, request, render_template_string
import requests
import ipaddress

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Geolocation Demo</title>

    <style>
        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            background: #080b14;
            color: white;
        }

        .box {
            width: 500px;
            max-width: 90%;
            padding: 35px;
            background: #121827;
            border: 1px solid #29344d;
            border-radius: 16px;
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
        }

        h1 {
            text-align: center;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #9aa6bd;
            margin-bottom: 30px;
        }

        form {
            display: flex;
            gap: 10px;
        }

        input {
            flex: 1;
            padding: 13px;
            border-radius: 8px;
            border: 1px solid #3a4660;
            background: #0b101d;
            color: white;
            font-size: 15px;
        }

        button {
            padding: 13px 18px;
            border: none;
            border-radius: 8px;
            background: #4f8cff;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background: #3678ed;
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            background: #0b101d;
            border-radius: 10px;
            border: 1px solid #29344d;
        }

        .result p {
            margin: 10px 0;
        }

        .error {
            margin-top: 20px;
            color: #ff7070;
        }

        .notice {
            margin-top: 25px;
            padding-top: 15px;
            border-top: 1px solid #29344d;
            color: #8995aa;
            font-size: 13px;
            text-align: center;
        }
    </style>
</head>

<body>

<div class="box">

    <h1>🌐 IP Geolocation Demo</h1>

    <p class="subtitle">
        Cybersecurity Awareness Demonstration
    </p>

    <form method="POST">
        <input
            type="text"
            name="ip"
            placeholder="Enter IP address (e.g. 8.8.8.8)"
            value="{{ ip }}"
            required
        >

        <button type="submit">
            Lookup
        </button>
    </form>

    {% if error %}
        <div class="error">
            <strong>Error:</strong> {{ error }}
        </div>
    {% endif %}

    {% if result %}
        <div class="result">

            <h2>📍 Result</h2>

            <p>
                <strong>IP Address:</strong>
                {{ result.ip }}
            </p>

            <p>
                <strong>City:</strong>
                {{ result.city }}
            </p>

            <p>
                <strong>Region:</strong>
                {{ result.region }}
            </p>

            <p>
                <strong>Country:</strong>
                {{ result.country }}
            </p>

            <p>
                <strong>ISP:</strong>
                {{ result.isp }}
            </p>
            <p>
    <strong>Latitude:</strong>
    {{ result.latitude }}
</p>

<p>
    <strong>Longitude:</strong>
    {{ result.longitude }}
</p>\

        </div>
    {% endif %}

    <div class="notice">
        This is a cybersecurity awareness demonstration.
        <br>
        IP-based location information is approximate.
    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None
    ip = ""

    if request.method == "POST":

        ip = request.form.get("ip", "").strip()

        try:

            # Validate the IP address
            ipaddress.ip_address(ip)

            # Query IP geolocation service
            response = requests.get(
                f"http://ip-api.com/json/{ip}",
                timeout=5
            )

            geo = response.json()

            if geo.get("status") != "success":

                error = "No geolocation information was found for this IP."

            else:

                result = {
                    "ip": ip,
                    "city": geo.get("city", "Unknown"),
                    "region": geo.get("regionName", "Unknown"),
                    "country": geo.get("country", "Unknown"),
                    "isp": geo.get("isp", "Unknown"),
"latitude": geo.get("lat", "Unknown"),
"longitude": geo.get("lon", "Unknown")
                }

        except ValueError:

            error = "Please enter a valid IP address."

        except requests.RequestException:

            error = "Could not connect to the geolocation service."

    return render_template_string(
        HTML,
        result=result,
        error=error,
        ip=ip
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )


