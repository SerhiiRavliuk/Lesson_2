from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    print("Запит на домашню сторінку")
    return render_template('dz.html')

@app.route('/dz_frame1')
def frame1():
    return render_template('dz_frame1.html')

@app.route('/dz_frame2')
def frame2():
    return render_template('dz_frame2.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
