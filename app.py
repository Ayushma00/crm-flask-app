from flask import Flask, render_template
import config
import requests
import json
def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

headers={'authorization':'Bearer {}'.format(app.config['AIRTABLE_KEY']),'content-type':"application/json"}
@app.route('/')
def index():
    return render_template('index.html', **locals())

@app.route('/users')
def users():
    url='https://api.airtable.com/v0/appZ8wloM4omloj0T/Team?maxRecords=4&view=Grid%20view'
    r=requests.get(url,headers=headers)
    result=json.loads(r.text)
    print(result)
    return render_template('user.html',**locals())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
