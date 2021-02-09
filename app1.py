from flask import Flask, request, render_template
import yfinance as yf

app = Flask(__name__)


@app.route("/quote")
def display_quote():
    symbol = request.args.get('symbol', default="GME")

    quote = yf.Ticker(symbol)

    return quote.info

@app.route("/history")
def display_history():

    symbol = request.args.get('symbol', default="GME")
    period = request.args.get('period', default="1y")
    interval = request.args.get('interval', default="1mo")
    quote = yf.Ticker(symbol)
    hist = quote.history(period=period, interval=interval)
    data = hist.to_json()
    return data


# run the flask app.
if __name__ == "__main__":
    app.run(debug=True)
