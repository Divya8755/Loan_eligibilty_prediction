import joblib
import numpy as np
loaded_model=joblib.load("C:\\Users\\Divya Negi\\Desktop\\Flask\\saved_model")
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/description')
def des():
    return 'Mental Health prediction'

@app.route('/')
def access():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def products():
    name=request.form.get('inputGroup-sizing-default')
    return render_template('pass.html',name=name)


@app.route('/uploader',methods=['POST'])
def getdata():
    feature=[]
    for x in request.form.values():
        feature.append(int(x)) 
    arr=[np.array(feature,dtype=np.float32)]  
    res=int(loaded_model.predict(arr)) 
    if(res==0):
        str="You are suffering from anxiety\nYou need to seek a pscychologist support"
    if(res==1):
        str="You are suffering from depression\nYou need to seek a pscychologist support"
    if(res==2):
        str="You are suffering from lonliness\n Speak to a counsellor or spend some time with your loved ones"
    if(res==4):
     str="You are normal"
    if(res==4):
     str="You are stressed\npractice yoga or talk to a counsellor" 
    return render_template('predict.html',label=str) 
#@app.route('/',methods=['POST']) 
#def getdetails():
    #l=request.form['inputGroupSelect01'] 
    #print(l)
    #return render_template('predict.html',label=l) 
if __name__=="__main__":
    app.run(debug=True)