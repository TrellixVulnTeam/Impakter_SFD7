from flask import Flask, render_template,request, flash, redirect, url_for
import os.path
import json
from werkzeug.utils import secure_filename

import mysql.connector
from mysql.connector import errorcode


kwargs = {}
try:
    connection  = mysql.connector.connect(
        host = '127.0.0.1',
        port = '3306',
        user = 'aravind',
        password = 'impakter',
        database = 'impakter_index',
    )

    cursor = connection.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        kwargs['status'] = "Something is wrong with your user name or password"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        kwargs['status'] = "Database does not exist"
    else:
        kwargs['status'] = f'{err}'

app = Flask(__name__)
app.secret_key = 'sfasdgafgdfgdggdaf'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_company',methods = ['GET','POST'])
def add_company():

    return render_template('add_company.html')

@app.route('/credentials',methods = ['GET','POST'])
def credentials():
    return render_template('credentials.html')

@app.route('/companies',methods = ['GET','POST'])
def display_companies():

    try:
        connection  = mysql.connector.connect(
        host = '127.0.0.1',
        port = '3306',
        user = 'aravind',
        password = 'impakter',
        database = 'impakter_index',
    )
        cursor = connection.cursor()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            kwargs['status'] = "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            kwargs['status'] = "Database does not exist"
        else:
            kwargs['status'] = f'{err}'

    try:  
        cursor.execute("select * from companies") 
        data = cursor.fetchall()
        connection.close()
        kwargs['status'] = 'Fetched ProjectData successfully'
    except:
        kwargs['status'] =  'Unable to execute'


    return render_template('companies.html',value = data,status = kwargs['status'])

@app.route('/research',methods = ['GET','POST'])
def research():
    return render_template('research.html')


@app.route('/upload_company',methods = ['GET','POST'])
def upload_company():
    if request.method == 'POST':

        info = {}
        info = {
            'id': request.form['company_name'][0:3]+request.form['ticker'],
            'company_name': request.form['company_name'],
            'company_url': request.form['company_url'],
            'address': request.form['address'],
            'country': request.form['country'],
            'stock_market':request.form['stock_market'],
            'ticker': request.form['ticker'],
            'revenue': request.form['company_revenue'],
            'financial_year': request.form['financial_year'],
            'desc': request.form['company_description'],
            'desc_long': request.form['company_description_long'],
            'sus': request.form['sustainability'],
            'sus_long': request.form['sustainability_long'],
            'critical_points': request.form['critical_points'],
            'outlook':request.form['outlook'],
            'notes':request.form['notes'],
            'rating':request.form['rating'],

        }
        kwargs = {}
        kwargs['company'] = info['company_name']

        if request.form['submit_button'] == 'update':

            try:
                connection  = mysql.connector.connect(
                host = '127.0.0.1',
                port = '3306',
                user = 'aravind',
                password = 'impakter',
                database = 'impakter_index',
            )
                cursor = connection.cursor()

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    kwargs['status'] = "Something is wrong with your user name or password"
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    kwargs['status'] = "Database does not exist"
                else:
                    kwargs['status'] = f'{err}'
                                
            kwargs['status'] = 'Entered if block'
            try:
                sql_query = ("insert into companies"
                            "(Company_ID,Company,Company_Url,Company_address,Revenue,Country,Stock_market,Ticker,Financial_year,Company_description,Desc_long,Sustainability,Sustainability_long,Analyst_Notes,Outlook,Rating)"
                            "values(%(id)s,%(company_name)s,%(company_url)s,%(address)s,%(revenue)s,%(country)s,%(stock_market)s,%(ticker)s,%(financial_year)s,%(desc)s,%(desc_long)s,%(sus)s,%(sus_long)s,%(notes)s,%(outlook)s,%(rating)s)")

                kwargs['status'] =  'updating DB'
                
                cursor.execute(sql_query, info)
                connection.commit()
                connection.close()
                kwargs['status'] =  'Connected and updated ProjectData'
            except:
                kwargs['status'] =  'Unable to execute the commit'
                
            return render_template('updated.html',**kwargs)

@app.route('/updated',methods = ['GET','POST'])
def updated():
    

    return render_template('updated.html',**kwargs)


connection.close()