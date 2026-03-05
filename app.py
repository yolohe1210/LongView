from flask import Flask, render_template, request, redirect
import portfolio

app = Flask(__name__)

@app.route("/")
def index():
    data = portfolio.get_portfolio_summary()
    data["portfolio_history"] = portfolio.get_portfolio_history()
    return render_template("index.html", data=data)


@app.route("/add", methods=["GET", "POST"])
def add_trade():
    if request.method == "POST":
        portfolio.add_trade(
            request.form["date"],
            request.form["asset"],
            request.form["quantity"],
            request.form["price"],
            request.form["note"]
        )
        return redirect("/")
    return render_template("add.html")


@app.route("/history")
def history():
    trades = portfolio.get_trade_history()
    return render_template("history.html", trades=trades)


@app.route("/update", methods=["GET", "POST"])
def update_price():
    if request.method == "POST":
        portfolio.update_price(
            request.form["asset"],
            request.form["price"],
            request.form["date"]
        )
        return redirect("/")
    return render_template("update.html")


if __name__ == "__main__":
    portfolio.initialize_files()
    app.run(debug=True)