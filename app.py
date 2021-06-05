# from chatbot import chatbot
from flask import Flask, render_template, redirect, url_for, request
import json
import random
import requests

app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'templates'

@app.route("/")
def home():
    return render_template("bot.html")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         user_name = request.form['username']
#         phone = request.form['phone']

#         # if login_mail(user_name=user_name,phone=phone):
#         if user_name and phone:
#         # if request.form['username'] != 'remitai1998@gmail.com' or request.form['password'] != '10111998tai':
#             info = user_name+'###'+phone
#             return redirect(url_for('chatbox',info=info))
#             # return render_template("chatbox.html")
#         #     return render_template('send.html', error=error)
#         else:
#             # error = 'Invalid Credentials. Please try again.'
#             return render_template('index.html', error=error)
#     return render_template('index.html', error=error)

# @app.route("/chatbox/<info>",methods = ['POST'])
# @app.route('', methods=['GET','POST'])
# def chatbox(info):
#     global phone
#     phone = info.split('###')[1]
#     # if request.method == 'POST':
#         # if request.form['btn'] == 'esc':
#             # return redirect(url_for('login'))
#         # else:
#             # return render_template("chatbox.html")
#     # else:
#         # return render_template("chatbox.html")
#     return render_template("chatbox.html")

@app.route("/get")
def get_bot_response():
    
    userText = request.args.get('msg')
    userId = request.args.get('_id')
    # api_url = 'http://0.0.0.0:6969/api/convers-manager'
    api_url = 'https://api-bkbot.herokuapp.com/api/convers-manager'
    input_data = {}
    input_data['message'] = str(userText)
    input_data['state_tracker_id'] = userId
    # print('>'*50,userId)
    # input_data['state_tracker_id'] = str(random.randint(100000, 999999))
    r = requests.post(url=api_url, json=input_data)
    chatbot_respose = r.json()
    mess_response = [item.replace('\n', r'').replace(r'"',r'') for item in chatbot_respose['message']]
    # mess_response = chatbot_respose['message'].replace('\n', r'').replace(r'"',r'')
    # print('mess_response',mess_response)
    return {"message_list":mess_response}

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
