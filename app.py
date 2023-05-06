from flask import Flask, request

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/')
def index():
    return 'BOTTY Controller'

# -----------------------------------------------------------


@app.route('/controller')
def controller():
    query = str(request.args.get('q'))
    return query


# -----------------------------------------------------------


@app.route('/update_instance_id')
def update_instance_id():
    with open('instance_id.txt', 'w') as instance_id:
        instance_id.write(str(request.args.get('id')))
        return 'updated', 200


@app.route('/get_instance_id')
def get_instance_id():
    with open('instance_id.txt', 'r') as instance_id:
        return instance_id.read(), 200


if __name__ == '__main__':
    app.run()
