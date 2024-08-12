from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            hourly_rate = float(request.form['hourly_rate'])
            hours_weekdays = float(request.form['hours_weekdays'])
            hours_weekend = float(request.form['hours_weekend'])
            weekend_bonus_percentage = float(request.form['weekend_bonus']) / 100
            hours_nightshift = float(request.form['hours_nightshift'])
            nightshift_bonus_percentage = float(request.form['nightshift_bonus']) / 100

            # Calculate payments
            payment_weekdays = hourly_rate * hours_weekdays
            payment_weekend = (hourly_rate * (1 + weekend_bonus_percentage)) * hours_weekend
            payment_nightshift = (hourly_rate * (1 + nightshift_bonus_percentage)) * hours_nightshift
            total_payment = payment_weekdays + payment_weekend + payment_nightshift

            return render_template('result.html', total_payment=total_payment)
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
