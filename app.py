from flask import Flask, request, render_template

app = Flask(__name__)

# Sabit ücret ve bonus oranları
HOUR_RATE = 14.89

# Bonus oranları
WEEKEND_BONUS = 0.40
NIGHT_BONUS_25_FREE = 0.25
NIGHT_BONUS_40_FREE = 0.40
NIGHT_BONUS_25_TAXED = 0.25
NIGHT_BONUS_10_TAXED = 0.10
OVERTIME_BONUS = 0.30

# Vergi oranları (örnek)
TAX_RATES = {
    "1": 0.20,
    "2": 0.18,
    "3": 0.15,
    "4": 0.20,
    "5": 0.25,
    "6": 0.30,
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        normal_hours = float(request.form['normal_hours'])
        night_hours_25_free = float(request.form['night_hours_25_free'])
        night_hours_40_free = float(request.form['night_hours_40_free'])
        night_hours_25_taxed = float(request.form['night_hours_25_taxed'])
        night_hours_10_taxed = float(request.form['night_hours_10_taxed'])
        saturday_hours = float(request.form['saturday_hours'])
        sunday_hours = float(request.form['sunday_hours'])
        overtime_hours = float(request.form['overtime_hours'])
        tax_class = request.form['tax_class']
    except ValueError:
        return "Lütfen geçerli saat değerleri girin."

    # Seçilen vergi sınıfına göre vergi oranını al
    tax_rate = TAX_RATES.get(tax_class, 0.20)

    # Normal çalışma ücreti
    normal_pay = normal_hours * HOUR_RATE

    # Gece çalışma ücretleri
    night_pay_25_free = night_hours_25_free * HOUR_RATE * (1 + NIGHT_BONUS_25_FREE)
    night_pay_40_free = night_hours_40_free * HOUR_RATE * (1 + NIGHT_BONUS_40_FREE)
    night_pay_25_taxed = night_hours_25_taxed * HOUR_RATE * (1 + NIGHT_BONUS_25_TAXED) * (1 - tax_rate)
    night_pay_10_taxed = night_hours_10_taxed * HOUR_RATE * (1 + NIGHT_BONUS_10_TAXED) * (1 - tax_rate)

    # Hafta sonu çalışma ücretleri
    saturday_pay = saturday_hours * HOUR_RATE * (1 + WEEKEND_BONUS) * (1 - tax_rate)
    sunday_pay = sunday_hours * HOUR_RATE * (1 + WEEKEND_BONUS)

    # Fazla mesai ücreti
    overtime_pay = overtime_hours * (HOUR_RATE * OVERTIME_BONUS)

    # Toplam ödeme
    total_pay = (normal_pay + night_pay_25_free + night_pay_40_free +
                 night_pay_25_taxed + night_pay_10_taxed +
                 saturday_pay + sunday_pay + overtime_pay)

    total_pay_taxed = total_pay * (1 - tax_rate)

    return render_template('result.html', total_pay=total_pay, total_pay_taxed=total_pay_taxed)

if __name__ == '__main__':
    app.run(debug=True)
