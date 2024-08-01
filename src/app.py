from flask import Flask, render_template, request
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

def get_clothing_recommendation(temp, description):
    recommendation = ""
    if 'rain' in description.lower():
        recommendation += "Bring an umbrella. "
    if temp < 50:
        recommendation += "Wear a heavy jacket."
    elif temp < 70:
        recommendation += "A light jacket will do."
    else:
        recommendation += "It's warm enough for shorts and a t-shirt."
    return recommendation

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = None
    weather_data = {}
    error_message = ''
    recommendation = ''
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        api_key = 'f563bc3eac39764c5f83a70176ec01ad'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=imperial'
        
        try:
            response = requests.get(url)
            data = response.json()
            if data.get('cod') != 200:
                error_message = data.get('message', 'Error retrieving data.')
            else:
                weather_data = {
                    'temperature': data['main']['temp'],
                    'weather': data['weather'][0]['main'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'wind_speed': data['wind']['speed'],
                    'sunrise': data['sys']['sunrise'],
                    'sunset': data['sys']['sunset']
                }
                recommendation = get_clothing_recommendation(data['main']['temp'], data['weather'][0]['description'])
        except Exception as e:
            error_message = str(e)
            logging.error(f"Error fetching data: {str(e)}")

    return render_template('index.html', user_input=user_input, weather_data=weather_data, error_message=error_message, recommendation=recommendation)

@app.before_request
def log_request_info():
    logging.info(f"Handling request for {request.url} - {request.method}")

@app.errorhandler(500)
def handle_500_error(e):
    logging.error(f"Internal server error: {str(e)}")
    return "Internal server error", 500

if __name__ == '__main__':
    app.run(debug=True)