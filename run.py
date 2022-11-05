from flask import Flask, render_template, request,send_from_directory
import os 

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['.xls','.xlsx','.csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('main/index.html')

@app.route('/signin')
def signin():
    return render_template('auth/signin.html')

@app.route('/signup')
def signup():
    return render_template('auth/signup.html')

@app.route('/signout')
def signout():
    return 'signout'

@app.route('/import', methods=['POST'])
def importFile():
    if request.method == 'POST':
        f = request.files['file']
        result = f.save(os.getcwd()+'/uploads/'+f.filename)
        return "File saved successfully"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/export')
def exportFile():
    pass

if __name__ == '__main__':
    app.run()