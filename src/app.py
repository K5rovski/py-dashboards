import io
import os
import seaborn as sns
import flask
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
from flask import Flask, redirect, url_for, render_template, request, flash
from jinja2 import Environment
import mpld3

app = Flask(__name__)

HTML = '''

<img src="{{myimg}}">

'''

@app.route('/testimg',methods=['GET'])
def test():

    img = io.BytesIO()
    sns.set_style("dark") #E.G.

    y = [1,2,3,4,5]
    x = [0,2,1,3,4]
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(x,y)
    fig.savefig(img, format='png')
    # fig.close('all')
    img.seek(0)

    plot_url = 'data:image/png;base64,'+ base64.b64encode(img.getvalue()).decode('ascii')
    nhtml = io.StringIO()
    mpld3.save_html(fig,nhtml)
    nhtml.seek(0)
    return nhtml.getvalue()
    # return Environment().from_string(HTML).render(myimg=plot_url)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT',5000), debug=True)


