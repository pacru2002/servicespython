from __future__ import print_function
import sys
from flask import Flask
from flask import jsonify
from flask import request
import cv2

app = Flask(__name__)
app.debug = True
empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 },
 {
 'id':'301',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 },
{
 'id':'401',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 },
{
 'id':'501',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }

 ]
@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    print("mytest")
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ]
    return jsonify({'emp':usr})

@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    return jsonify({'emp':em[0]})

@app.route('/empdb/employee',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
       abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})


@app.route('/empdb/fileProcess',methods=['POST'])
def videoFileProcess():
    print("inside video file process")
    if request.method == 'POST':
        #if 'file' not in request.files['file']:
            #print('No file part')
            #return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            #return redirect(request.url)
        #if file and allowed_file(file.filename):
        filename = file.filename
        print("file name is "+filename)
        blob = request.files['file'].read()
        size = len(blob)
        print(size)
        print("after vc")
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("after save")
            #return redirect(url_for('uploaded_file',filename=filename))

    return jsonify({'response':filename})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
 app.run(debug=True)
