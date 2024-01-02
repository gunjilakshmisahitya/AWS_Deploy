from flask import Flask,render_template,request
import pickle
import numpy as np
#create a flask object
app=Flask(__name__)
'''@app.route('/') #@creates a decorator which activate from function to function
def hello():
    """Test Function"""
    return "Welcome to flask"
@app.route('/sahitya',methods=['GET'])
def check():
    "new Function"
    return "Codegan is in KITS"
'''
'''@app.route('/',methods=['Get'])
def home():
    return render_template('index.html')'''
# First let's read the pickle
with open('House_Price.pkl','rb')as f:
    model=pickle.load(f)
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    Rooms=int(request.form['bedrooms'])
    Bathrooms=int(request.form['bathrooms'])
    Place=int(request.form['location'])
    Area=int(request.form['area'])
    Status=int(request.form['status'])
    Facing=int(request.form['facing'])
    P_Type=int(request.form['type'])
    #Rooms=int(request.form['bedrooms'])
    #now take the above form data and convert to array
    input_data=np.array([[Rooms,Bathrooms,Place,Area,Status,Facing,P_Type]])
    #by taking above data will predict the house_price
    prediction=model.predict(input_data)[0]
    #now we will pass above predicted data to template
    return render_template('index.html',prediction=prediction)
    
app.run()

