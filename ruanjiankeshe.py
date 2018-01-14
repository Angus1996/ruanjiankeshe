from flask import Flask,request,render_template

app = Flask(__name__)



@app.route('/',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/first',methods=['GET','POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='1234':
        return render_template('first.html', username=username)
    return render_template('form.html', message='Bad name or password', username=username)




@app.route('/first/employee',methods=['GET'])
def employee():
    return render_template('employee.html')

@app.route('/first/product',methods=['GET'])
def product():
    return render_template('product.html')

@app.route('/first/sensor',methods=['GET'])
def sensor():
    return render_template('sensor.html')

if(__name__)=='__main__':
    app.run(host='0.0.0.0')