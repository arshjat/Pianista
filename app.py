from flask import Flask,render_template,request,flash,redirect,url_for,jsonify
import subprocess
from flask import after_this_request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import os
import audio
app = Flask(__name__)
@app.route("/download/<var>")
def hello(var):
    cmd = ['spotdl','--song',var,'-f','./','--avconv']
    p = subprocess.Popen(cmd,stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        stdin = subprocess.PIPE)
    out,err = p.communicate()

    if out:
        return redirect(url_for('convert'))
    else:
        return "Failure"

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')
    
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
        result = request.form.to_dict()
        # @after_this_request
        # def removefile(response):
        #     os.remove('./converted.tta')
        #     os.remove('./converted_audio.wav')
        return redirect(url_for('hello',var=result['query']))

@app.route('/conv')
def convert():
    
    os.system('ls | grep \.m4a$ > m.txt')
    
    for line in open('m.txt'):
        var = line.split('\n')[0]

    cmd4 = ['ffmpeg','-i',var,'converted.tta']
    p = subprocess.Popen(cmd4,stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        stdin = subprocess.PIPE)
    out,err = p.communicate()
    @after_this_request
    def removefile(response):
        os.remove('./' + var)
        os.remove('./m.txt')
        return response
    return redirect(url_for('extract'))
    # else :
    #     return err


@app.route('/extract')
def extract():
    # check()
    # cmd = ['python','audio.py']
    # p = subprocess.Popen(cmd,stdout = subprocess.PIPE,
    #                     stderr = subprocess.PIPE,
    #                     stdin = subprocess.PIPE)
    # out,err = p.communicate()
    # return "I am here"
    var = json.dumps(audio.dunc())
    print(var)
    return render_template('piano.html',name=var)
    

@app.route('/dump')
def dump(msg):
    return(jsonify(msg))
        
@app.route('/check')
def check():
    # dump(audio.dunc())
    return render_template('piano.html',name = json.dumps(audio.dunc()))

if __name__ == '__main__':
    app.run(debug=True)