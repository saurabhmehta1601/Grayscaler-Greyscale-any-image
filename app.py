from flask import Flask,render_template,redirect,request
from werkzeug.utils import secure_filename
import os


app=Flask(__name__)

UPLOAD_FOLDER='./static/process'
ALLOWED_EXTENTIONS={'png','jpg','jpeg'}

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['ALLOWED_EXTENTIONS']=ALLOWED_EXTENTIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process',methods=["GET","POST"])
def process():
    f=request.files['file']
    if f.filename.split('.')[1] in app.config['ALLOWED_EXTENTIONS']:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        return redirect(request.referrer)
    else:
        return "File extention not allowed "
if __name__ == "__main__":
    app.run(debug=True)

