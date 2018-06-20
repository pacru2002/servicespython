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

if __name__ == '__main__':
 app.run(debug=True)
