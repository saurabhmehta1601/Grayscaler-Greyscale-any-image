from flask import (Flask,redirect,render_template,request)
from werkzeug.utils import secure_filename
import os

# Creating flask app instance
app=Flask(__name__)

# Setting Upload folder and extentions for file 
ALLOWED_EXTENTIONS={'png','jpg','jpeg'}
UPLOAD_FOLDER='./images'
#################
app.config['ALLOWED_EXTENTIONS']=ALLOWED_EXTENTIONS
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


# Creating homepage route
@app.route('/')
def home():
    return render_template('home.html')

# Route for handling file upload
@app.route('/process',methods=["POST"])
def process():
    f=request.files['file']
    if f.filename.split('.')[1] in app.config["ALLOWED_EXTENTIONS"]:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        return redirect(request.referrer)
    else:
        return "Invalid file extention"


if __name__ == "__main__":
    app.run(debug=True)
