from flask import Flask,request,render_template,redirect

app =  Flask(__name__)
l=['ola','nick']
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
	if request.method =='POST':
		data = request.form.get('text')
		l.append(data)
	return redirect('/')

@app.route('/see',methods=['GET','POST'])
def see():
	
	data = l
	return render_template('base.html',data=data)
if __name__ == '__main__':
	app.run(debug=True)
	print(l)
