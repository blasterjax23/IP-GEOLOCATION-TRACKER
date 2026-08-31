# IP Geolocation Tracker 🌐

A simple Flask web app that looks up the approximate geographic location of any IP address — built as a cybersecurity awareness demonstration.

## 📖 About

Enter an IP address, and the app returns its approximate city, region, country, ISP, and coordinates by querying a public IP geolocation API. It's meant to illustrate, in a hands-on way, how much information can be inferred from just an IP address — a common talking point in cybersecurity awareness sessions.

> ⚠️ **Note:** IP-based geolocation is approximate. It typically reflects the location of the ISP or data center serving that IP, not the exact physical location of the device.

## ✨ Features

- Simple, single-page web interface
- Validates the entered IP address before doing a lookup
- Fetches city, region, country, ISP, latitude, and longitude
- Clear error handling for invalid IPs or failed lookups
- Clean, dark-themed UI — no external CSS frameworks needed

## 🛠️ Tech Stack

- **Python 3**
- **Flask** — web framework
- **Requests** — for calling the geolocation API
- **[ip-api.com](http://ip-api.com/)** — free IP geolocation service

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/blasterjax23/IP-GEOLOCATION-TRACKER.git
   cd IP-GEOLOCATION-TRACKER
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask requests
   ```

### Run it

```bash
python3 app.py
```

The app will start on `http://0.0.0.0:8080`. Open **http://localhost:8080** in your browser.

## 🖥️ Usage

1. Open the app in your browser.
2. Enter an IP address (e.g. `8.8.8.8`).
3. Click **Lookup**.
4. View the returned city, region, country, ISP, and coordinates.

## 📂 Project Structure

```
app.py          # Main Flask application (routes, HTML template, geolocation logic)
```

## ⚙️ How It Works

1. The user submits an IP address through the web form.
2. The app validates it using Python's built-in `ipaddress` module.
3. A request is sent to `ip-api.com` for that IP's geolocation data.
4. The result (or an error message) is rendered back on the same page.

## 🎓 Learning Context

Built as a mini-project / cybersecurity awareness demo to show how IP-based tracking works in practice, and to reinforce good input-validation habits in a web app.

## 👤 Author

**ABHIJITH S**

## 📄 License

This project is open for educational use.
