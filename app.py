from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "dc39da6ca917abb325609e8af713840b"

@app.route("/", methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()
            if data.get('cod') == 200:
                weather = {
                    
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                error = 'City not found. Please enter a valid city name.'
        else: 
            error = 'Please enter a city name.'
            
    return render_template('index.html', weather=weather, error=error)

if __name__ == '__main__':
    app.run(debug=True)