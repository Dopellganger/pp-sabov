from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/hello-world-26')
def welcome():
    return 'Hello world 26'
#Ти долбойоб ааа аа

if __name__ == '__main__':
    app.run()
