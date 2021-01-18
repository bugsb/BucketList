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
	return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
	if request.method =='POST':
		data = request.form.get('text')
		myDict = {}
		myDict["name"] = data
		mycol.insert_one(myDict)
	return redirect('/')

@app.route('/see',methods=['GET','POST'])
def see():
	data = []
	myquery = { "name": { "$regex": "^[a-z]|^[A-Z]" } }
	for i in mycol.find(myquery):
		data.append(i["name"])
		data = sorted(data)
	return render_template('base.html',data=data)
if __name__ == '__main__':
	app.run(debug=True)
	print(l)
