
from flask import Flask,render_template,request,session,redirect,url_for,flash
from pymongo import MongoClient # mongodb 
from weather import *

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'jaypatel19112001'
# client = MongoClient('localhost', 27017) # connection 
# db = client.Website # create table
# regapi = db.Userdata # triger


@app.route('/')
def HomePage():
    location = Weather.location()
    info = Weather.info()
    temp = Weather.temp()
    humidity = Weather.humidity()
    Moonrise = Weather.Moonrise()
    allDays = Weather.allDays()

    return render_template('Home.html',location=location,info=info,temp=temp,humidity=humidity,Moonrise=Moonrise,allDays=allDays)
   


if __name__=='__main__':
    app.run(debug=True)