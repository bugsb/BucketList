
from flask import Flask,request,render_template,redirect
import pymongo


app =  Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://admin:raina111@cluster0.rg8a7.mongodb.net/mydb?retryWrites=true&w=majority"
# mongo = PyMongo(app)
myclient = pymongo.MongoClient("mongodb+srv://admin:raina111@cluster0.rg8a7.mongodb.net/mydb?retryWrites=true&w=majority")
mydb = myclient["mydb"]
mycol = mydb["bucket"]

# mycol.insert_one(mydict)
@app.route('/')
def index():
	data = []
	myquery = { "name": { "$regex": "^[a-z]|^[A-Z]" } }
	for i in mycol.find(myquery):
		data.append(i["name"])
		print(i["_id"])
		data = sorted(data)
	return render_template('index.html',data=data)

@app.route('/submit',methods=['GET','POST'])
def submit():
	if request.method =='POST':
		data = request.form.get('text')
		myDict = {}
		myDict["name"] = data
		mycol.insert_one(myDict)
	return redirect('/admin/fjewiewirw4i3ri')

@app.route('/view',methods=['GET','POST'])
def see():
	data = []
	myquery = { "name": { "$regex": "^[a-z]|^[A-Z]" } }
	for i in mycol.find(myquery):
		data.append(i["name"])
		data = sorted(data)
	return render_template('view.html',data=data)

@app.route('/admin/fjewiewirw4i3ri',methods=['GET','POST'])
def admin():
	user=""
	passwd=""
	data = []
	myquery = { "name": { "$regex": "^[a-z]|^[A-Z]" } }
	for i in mycol.find(myquery):
		data.append(i["name"])
		data = sorted(data)
	if request.method =='POST':
		user = request.form.get('login')
		passwd = request.form.get('pass')
		if user == 'mani' and passwd == 'pass123':
			return render_template('admin.html',data=data)
		else:
			return "<h1>Not Allowed</h1>"
	else:
		return render_template('admin.html',data=data)

@app.route('/admin/auth',methods=['GET','POST'])
def auth():
	return render_template('login.html')

@app.route('/del/<val>')
def delete(val):
	myquery = { "name": val }
	mycol.delete_one(myquery)
	return redirect('/admin/fjewiewirw4i3ri')


if __name__ == '__main__':
	app.run(debug=True)
