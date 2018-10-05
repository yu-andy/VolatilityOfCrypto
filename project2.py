from flask import Flask,render_template
import pygal
from pygal.style import Style
import json
import time
import pandas as pd
import sys
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/xBar")
def xBar():
    # Charting code will be here
    with open('bar.json','r') as bar_file:
        data = json.load(bar_file)
    custom_style = Style(
        colors=('#991515','#1cbc7c'),
        background='#d2ddd9',
        legend_font_size=6,
        font_family='googlefont:Raleway'
        )
    chart = pygal.Bar(width=600, height=300, style=custom_style)
    chart.title = 'This is a title'
    #this is the y axis
    mark_list = [x['mark'] for x in data]
    chart.add('Hello',mark_list)
    #this is the x axis
    chart.x_labels = [x['year'] for x in data]
    tourn_list = [x['tournament'] for x in data]
    chart.add('Tournament Score',tourn_list)
    chart.render_to_file('static/images/xBar_chart.svg')
    img_url = 'static/images/xBar_chart.svg?cache=' + str(time.time())
    return render_template('app.html',image_url = img_url)

@app.route("/line")
def line():
    with open('us_exchange_extracted.json','r') as data_file:
        us_exchange_data = json.load(data_file)
    with open('bitcoin_prices.json', 'r') as data_file:
        bitcoin_data = json.load(data_file)
    with open('ethereum_prices.json', 'r') as data_file:
        ethereum_data = json.load(data_file)
    custom_style = Style(
        colors=('#6699ff','#1cbc7c'),
        background='#000000',
        plot_background='#1a1a1a',
        foreground='#ffffff',
        foreground_subtle='#ffffff',
        foreground_strong='#ffffff',
        legend_font_size=10,
        font_family='googlefont:Raleway',
        major_label_font_size=7,
        label_font_size=8
        )
    chart = pygal.Line(width=600, height=300, style=custom_style, dots_size=0.8, label_font_size=6, x_title = 'Time', y_title = 'Price', x_labels_major_every=300, y_labels_major_every=None, x_label_rotation=20, show_minor_x_labels=False)
    chart.title = 'Exchange rates of US Dollar'

    coin_chart = pygal.Line(width=600, height=300, style=custom_style, dots_size=0.8, label_font_size=10, x_title = 'Time', y_title = 'Price', x_labels_major_every=200, y_labels_major_every=None, x_label_rotation=20, show_minor_x_labels=False)
    coin_chart.title = 'Prices of coins'
    francs_list = []
    for x in us_exchange_data:
        temp = {
        'value': x['FRANCS/US$'],
        'label': x['YEAR']
        }
        francs_list.append(temp)

    chart.add('Francs/USD', francs_list)

    singapore_list = []
    for x in us_exchange_data:
        temp = {
        'value': x['SINGAPORE/US$'],
        'label': x['YEAR']
        }
        singapore_list.append(temp)

    chart.add('Singapore/USD', singapore_list)

    kroner_list = []
    for x in us_exchange_data:
        temp = {
        'value': x['KRONER/US$'],
        'label': x['YEAR']
        }
        kroner_list.append(temp)

    chart.add('Kroner/USD', kroner_list)

    ethereum_list = []
    for x in ethereum_data:
        temp = {
        'value': x['Open'],
        'label': x['Date']
        }
        ethereum_list.append(temp)

    ethereum_list.reverse()

    coin_chart.add('Ethereum', (ethereum_list))

    coin_chart.x_labels = [x['label'] for x in ethereum_list]

    bitcoin_list = []
    for x in bitcoin_data:
        temp = {
        'value': x['Open'],
        'label': x['Date']
        }
        bitcoin_list.append(temp)

    bitcoin_list.reverse()

    coin_chart.add('Bitcoin', (bitcoin_list))

    chart.x_labels = [x['YEAR'] for x in us_exchange_data]

    coin_chart.render_to_file('static/images/coin_line_chart.svg')
    chart.render_to_file('static/images/line_chart.svg')
    img_url = 'static/images/line_chart.svg?cache=' + str(time.time())
    coin_url = 'static/images/coin_line_chart.svg?cache=' + str(time.time())
    return render_template('line_chart.html', image_url = img_url, coin_chart = coin_url)

@app.route("/scatter")
def scatter():
    with open('bitcoin_prices.json', 'r') as data_file:
        bitcoin_data = json.load(data_file)
    with open('ethereum_prices.json', 'r') as data_file:
        ethereum_data = json.load(data_file)
    with open('litecoin_prices.json', 'r') as data_file:
        litecoin_data = json.load(data_file)
    with open('monero_prices.json', 'r') as data_file:
        monero_data = json.load(data_file)
    with open('dash_prices.json', 'r') as data_file:
        dash_data = json.load(data_file)
    with open('iota_prices.json', 'r') as data_file:
        iota_data = json.load(data_file)
    with open('nem_prices.json', 'r') as data_file:
        nem_data = json.load(data_file)
    with open('omisego_prices.json', 'r') as data_file:
        omisego_data = json.load(data_file)
    with open('qtum_prices.json', 'r') as data_file:
        qtum_data = json.load(data_file)
    with open('stratis_prices.json', 'r') as data_file:
        stratis_data = json.load(data_file)
    with open('waves_prices.json', 'r') as data_file:
        waves_data = json.load(data_file)

    custom_style = Style(
        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'),
        background='#000000',
        plot_background='#1a1a1a',
        foreground='#ffffff',
        foreground_subtle='#ffffff',
        foreground_strong='#ffffff',
        legend_font_size=10,
        font_family='googlefont:Raleway',
        major_label_font_size=7,
        label_font_size=8
        )
    chart = pygal.Line(width=600, height=300, style=custom_style, dots_size=0.2, label_font_size=6, x_title = 'Time', y_title = 'Price', y_labels_major_every=None, x_label_rotation=20, show_minor_x_labels=False, stroke=False)
    chart.title = 'Comparison of lesser known coins'
    bitcoin_list = []
    for x in bitcoin_data:
        temp = {
        'value': x['Open']/100,
        'label': x['Date']
        }
        bitcoin_list.append(temp)
    bitcoin_list.reverse()
    chart.add('Bitcoin/100', bitcoin_list)

    nem_list = [x['Open'] for x in nem_data]
    # nem_list = []
    # for x in nem_data:
    #     temp = {
    #     'value': x['Open'],
    #     'label': x['Date']
    #     }
    nem_list.reverse()
    chart.add('Nem', nem_list)

    stratis_list = [x['Open'] for x in stratis_data]
    # stratis_list = []
    # for x in stratis_data:
    #     temp = {
    #     'value': x['Open'],
    #     'label': x['Date']
    #     }
    stratis_list.reverse()
    chart.add('Stratis', stratis_list)

    waves_list = [x['Open'] for x in waves_data]
    # waves_list = []
    # for x in waves_data:
    #     temp = {
    #     'value': x['Open'],
    #     'label': x['Date']
    #     }
    waves_list.reverse()
    chart.add('Waves', waves_list)

    iota_list = [x['Open'] for x in iota_data]
    # iota_list = []
    # for x in iota_data:
    #     temp = {
    #     'value': x['Open'],
    #     'label': x['Date']
    #     }
    iota_list.reverse()
    chart.add('Iota', iota_list)

    label_list = []
    for x in nem_data:
        temp = {
        'value': x['Open'],
        'label': x['Date']
        }
        label_list.append(temp)

    label_list.reverse()
    chart.x_labels = [x['label'] for x in label_list]

    chart.render_to_file('static/images/scatter_chart.svg')
    img_url = 'static/images/scatter_chart.svg?cache=' + str(time.time())
    return render_template('template.html', image_url = img_url)

@app.route("/bar")
def bar():
    with open('bitcoin_prices.json', 'r') as data_file:
        bitcoin_data = json.load(data_file)
    with open('ethereum_prices.json', 'r') as data_file:
        ethereum_data = json.load(data_file)
    with open('litecoin_prices.json', 'r') as data_file:
        litecoin_data = json.load(data_file)
    with open('monero_prices.json', 'r') as data_file:
        monero_data = json.load(data_file)
    with open('dash_prices.json', 'r') as data_file:
        dash_data = json.load(data_file)
    with open('iota_prices.json', 'r') as data_file:
        iota_data = json.load(data_file)
    with open('nem_prices.json', 'r') as data_file:
        nem_data = json.load(data_file)
    with open('omisego_prices.json', 'r') as data_file:
        omisego_data = json.load(data_file)
    with open('qtum_prices.json', 'r') as data_file:
        qtum_data = json.load(data_file)
    with open('stratis_prices.json', 'r') as data_file:
        stratis_data = json.load(data_file)
    with open('waves_prices.json', 'r') as data_file:
        waves_data = json.load(data_file)

    custom_style = Style(
        colors=('#0f2c58', '#005a8e', '#008cad','#00677b', '#14837c','#00bdab', '#3cea8d'),
        background='#000000',
        plot_background='#1a1a1a',
        foreground='#ffffff',
        foreground_subtle='#ffffff',
        foreground_strong='#ffffff',
        legend_font_size=10,
        font_family='googlefont:Raleway',
        major_label_font_size=7,
        label_font_size=8,
        title_font_size=12
        )
    chart = pygal.HorizontalBar(width=600, height=300, style=custom_style, x_title = 'Open - Close')
    chart.title = 'Average difference between Open and Close prices'
    #chart.x_labels = ['Bitcoin', 'Ethereum', 'Nem', 'Omisego', 'Qtum', 'Stratis', 'Waves']

    bitcoin_list = []
    for x in bitcoin_data:
        bitcoin_list.append(x['Open'] - x['Close'])
    avg = sum(bitcoin_list)/len(bitcoin_list)
    chart.add('Bitcoin', avg)

    ethereum_list = []
    for x in ethereum_data:
        ethereum_list.append(x['Open'] - x['Close'])
    avg = sum(ethereum_list)/len(ethereum_list)
    chart.add('Ethereum', avg)

    nem_list = []
    for x in nem_data:
        nem_list.append(x['Open'] - x['Close'])
    avg = sum(nem_list)/len(nem_list)
    chart.add('Nem', avg)

    omisego_list = []
    for x in omisego_data:
        omisego_list.append(x['Open'] - x['Close'])
    avg = sum(omisego_list)/len(omisego_list)
    chart.add('Omisego', avg)

    qtum_list = []
    for x in qtum_data:
        qtum_list.append(x['Open'] - x['Close'])
    avg = sum(qtum_list)/len(qtum_list)
    chart.add('Qtum', avg)

    stratis_list = []
    for x in stratis_data:
        stratis_list.append(x['Open'] - x['Close'])
    avg = sum(stratis_list)/len(stratis_list)
    chart.add('Stratis', avg)

    waves_list = []
    for x in waves_data:
        waves_list.append(x['Open'] - x['Close'])
    avg = sum(waves_list)/len(waves_list)
    chart.add('Waves', avg)

    chart.render_to_file('static/images/bar_chart.svg')
    img_url = 'static/images/bar_chart.svg?cache=' + str(time.time())
    return render_template('template.html', image_url = img_url)

@app.route("/stackedline")
def StackedLine():
    with open('us_exchange_extracted.json','r') as data_file:
        us_exchange_data = json.load(data_file)
    with open('bitcoin_prices.json', 'r') as data_file:
        bitcoin_data = json.load(data_file)
    with open('ethereum_prices_extracted.json', 'r') as data_file:
        ethereum_data = json.load(data_file)

    custom_style = Style(
        colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'),
        background='#000000',
        plot_background='#1a1a1a',
        foreground='#ffffff',
        foreground_subtle='#ffffff',
        foreground_strong='#ffffff',
        legend_font_size=10,
        font_family='googlefont:Raleway',
        major_label_font_size=7,
        label_font_size=8,
        title_font_size=12,
        opacity='.6',
        opacity_hover='.9',
        transition='100ms ease-in'
        )

    chart = pygal.StackedLine(width=600, height=300, fill=True, interpolate='cubic', style=custom_style, show_dots=False, x_title = 'Time', y_title = 'Price')
    chart.title = 'Nominal Broad Dollar Index Comparison'
    nominal_list = []
    for x in us_exchange_data:
        y = x['Nominal Broad Dollar Index']
        if (y != None):
            y = y * 10
        temp = {
        'value': y,
        'label': x['YEAR']
        }
        nominal_list.append(temp)

    chart.add('Nominal Broad Dollar Index', nominal_list)

    #print(resample.size, file=sys.stderr)


    bitcoin_list = []
    for x in bitcoin_data:
        temp = {
        'value': x['Open'],
        'label': x['Date']
        }
        bitcoin_list.append(temp)
    bitcoin_list.reverse()
    chart.add('Bitcoin', bitcoin_list)

    ethereum_list = []
    for x in ethereum_data:
        temp = {
        'value': x['Open'],
        'label': x['Date']
        }
        ethereum_list.append(temp)
    ethereum_list.reverse()
    chart.add('Ethereum', (ethereum_list))

    chart.render_to_file('static/images/stacked_line_chart.svg')
    img_url = 'static/images/stacked_line_chart.svg?cache=' + str(time.time())
    return render_template('template.html', image_url = img_url)
if __name__ == "__main__":
    app.run(threaded=True, debug=True)
