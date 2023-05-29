import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

def errorPage(title, info, file):
    return render_template("error.html", titlee=title, infoo=info, filee=file)



def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        response = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None
def lookup2(symbol):
    api_key = os.environ.get("API_KEY")
    try:
        logo = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/logo?token={api_key}")
        company_info = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/company?token={api_key}")
        stats = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/stats?token={api_key}")
        company_news = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/news/last/20?token={api_key}")
        quote = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}")

        dividends = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/dividends/5y?token={api_key}")
        # institutional = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/institutional-ownership?token={api_key}")
        # insider_transactions = requests.get(f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/insider-transactions?token={api_key}")
    except requests.RequestException:
        return None
    # return logo.json()
    return {
    "logo" : logo.json(),
    "company_info" : company_info.json(),
    "stats" : stats.json(),
    "company_news" : company_news.json(),
    "quote" : quote.json(),
    "dividends" : dividends.json(),
    }

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
