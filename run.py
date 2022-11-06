from flask import Flask, render_template, request,send_from_directory, redirect
import os,openpyxl
path = ''

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['.xlsx'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def getObjectsFromImport(path):
    table = openpyxl.load_workbook(path)
    ws = table.active
    obj_list = []
    if os.path.isfile(path):
        l = [row for row in ws.iter_rows(min_row=2,max_col=11, values_only=True)]
        for row in l:
            obj = {
                'location':row[0],
                'rooms_count':row[1],
                'segment': row[2],
                'floors': row[3],
                'walls': row[4],
                'floor_number': row[5],
                'square': row[6],
                'kitchen': row[7],
                'balcony': row[8],
                'from_metro': row[9],
                'wall_decoration': row[10]
            }
            obj_list.append(obj)
        return obj_list

@app.route('/')
def index():
    path = ''
    if os.path.isfile(os.getcwd()+'/uploads/input.xlsx'):
        path = os.getcwd()+'/uploads/input.xlsx'
    else:
        path = os.getcwd()+'/uploads/empty.xlsx'
    
    objects = getObjectsFromImport(path)
    return render_template('main/index.html',objects=objects)

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
        return redirect('http://localhost:5000/')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/export')
def exportFile():
    pass

if __name__ == '__main__':
    app.run()