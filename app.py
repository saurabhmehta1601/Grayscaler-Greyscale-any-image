from flask import (Flask,redirect,render_template,request,send_file)
from werkzeug.utils import secure_filename
from processor import processor
import os

# Creating flask app instance
app=Flask(__name__)

# Setting Upload folder and extentions for file 
ALLOWED_EXTENTIONS={'png','jpg','jpeg'}
UPLOAD_FOLDER='./images/'
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
    # uploaded file store in varible f
    f=request.files['file']
    # if f have appropriate extention save uploaded file in image directory
    if f.filename.split('.')[1] in app.config["ALLOWED_EXTENTIONS"]:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        # After saving uploaded image process the image applying processor method on it
        processor(f.filename,app.config['UPLOAD_FOLDER'])
        # redirect to route which downloads the final grayscale image
        return redirect('/download/'+f.filename)
    else:
        return "Invalid file extention"
# route to download image
@app.route('/download/<filename>')
def download(filename):
    filename=app.config['UPLOAD_FOLDER']+filename
    # downloads image
    return send_file(filename,as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
