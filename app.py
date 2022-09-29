import os

from flask import Flask, request, render_template, redirect, flash, session
from datetime import datetime as dt
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

c = CurrencyRates()
cc = CurrencyCodes()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)



@app.route("/")
def home_page():
    session['amount']=0
    return render_template("home.html")


@app.route("/p", methods=['POST'])
def show_currency():
    
  
    from_currency = request.form.get('from_currency').upper()
    to_currency = request.form.get('to_currency').upper()
    from_amount = request.form.get('from_amount', 0)

    try: 
        c.get_rates(from_currency)
    except RatesNotAvailableError as error:
        flash(f"Error raised: {error}")
        session['conversion'] = ''
        return redirect ("/")
    except:
        flash(f"Invalid currency: {from_currency}.")
        session['conversion'] = ''
        return redirect ("/")
    
    

    try: 
        c.get_rates(to_currency)
    except:
        flash(f"Invalid currency: {to_currency}.")
        session['conversion'] = ''
        return redirect ("/")
        

    curr1 = cc.get_symbol(from_currency)
    curr2 = cc.get_symbol(to_currency)
  
    session['amount'] = str('{0:.2f}'.format(c.convert(from_currency, to_currency, float(from_amount))))

    amount = session['amount']

    session['conversion'] = f'{curr1}{from_amount} = {curr2}{amount}'

    return redirect('/')