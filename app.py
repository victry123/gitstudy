from flask import Flask

app =Flask(__name__)


app.config['key']='123456'
num1 =100
num2 =200
if __name__ == '__main__':
    app.run()

