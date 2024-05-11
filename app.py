from flask import Flask, render_template, request, flash
from converter import convert_currency, get_exchange_rates

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    currencies = get_exchange_rates().keys()
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form['amount']
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    # Convert amount to a decimal number when passing it to the conversion function
    converted_amount = convert_currency(int(amount) / 1, from_currency, to_currency)
    
    if converted_amount is None:
        flash('Conversion failed. Please try again agian.', 'error')
    else:
        flash(f'Converted amount: {converted_amount} {to_currency}', 'success')

    currencies = get_exchange_rates().keys()
    return render_template('index.html', currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
