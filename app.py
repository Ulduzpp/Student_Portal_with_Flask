from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def Main():
    return render_template('index.html')

@app.route('/profile')
def Profile():
    items=[
        {
            'num':'Student 1',
            'name': 'Ulduz',
            'email':'u.pakpoor@gmail.com',
            'major': 'AI'
        },
        {
            'num' : 'Student 2',
            'name': "Mahsa",
            'email':'mahsa.sanaei@gmail.com',
            'major':'AI'
        }
    ]
    return render_template('profile.html',students=items)

@app.route('/courses')
def Course():
    items=[
        {
            'id':1,
            'name': 'Robotics',
            'description': 'A comprehensive course for getting started with robotics and robot programming.',
            'teacher':'Mr.Ghost'
        },
        {
            'id':2,
            'name': 'GenAI',
            'description': 'A comprehensive course for generative ai.',
            'teacher': 'Ms.Pakpoor'
        }
    ]
    
    
    return render_template('courses.html',courses=items)


@app.route('/courses/<int:course_id>')
def Course_detail(course_id):
    return render_template('course_detail.html',id=course_id)

@app.route('/auth',methods=['POST','GET'])
def select_course():
    if request.method=='POST':
        if request.form['course_num'] == '1' or request.form['course_num']=='2':
            return redirect(url_for('Course_detail',course_id=request.form['course_num']))    
        else:
            return redirect(url_for('Errors'))

@app.route('/error')
def Errors():
    return 'This is the error page'

if __name__=='__main__':
    app.run(debug=True)