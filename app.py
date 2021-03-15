import get_rates
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

rates = get_rates.rates_list()

@app.route("/calc/", methods=["GET", "POST"])
def calc():
    if request.method == "GET":
        currency_code = [[i[1], i[0]] for i in rates]
        return render_template("calculator.html", currency_code=currency_code)
    if request.method == "POST":
        input_data = request.form
        code = input_data.get('code')
        how_much = input_data.get('how_much')
        rate = [i[3] for i in rates if i[1] == code][0]
        result = round(float(rate) * float(how_much), 2)
        return render_template("result.html", result=result, rate=rate, code=code, how_much=how_much)


if __name__ == "__main__":
    app.run(debug=True)

