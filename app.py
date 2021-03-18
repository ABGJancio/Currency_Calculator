import current_rates
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

rates = current_rates.rates_list()
currency_code = [[i[1], i[0]] for i in rates]

@app.route("/calc/", methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        input_data = request.form
        code = input_data.get('code')
        how_much = float(input_data.get('how_much'))
        rate = float([i[3] for i in rates if i[1] == code][0])
        result = round(rate * how_much, 2)
        return render_template("result.html", result=f'{result:.2f}', rate=rate, code=code, how_much=f'{how_much:.2f}', currency_code=currency_code)
    return render_template("calculator.html", currency_code=currency_code)

if __name__ == "__main__":
    app.run(debug=True)

