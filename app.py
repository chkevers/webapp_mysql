from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Kokomo007&'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'localflask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

db = MySQL(app)

@app.route('/')
def index():
    cur = db.connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS testdb (id int , name varchar(255))''')
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def new_data():
    if request.method == 'POST':
        cur = db.connection.cursor()
        id = request.form['id']
        name = request.form['name']
        cur.execute(f'''insert into testdb (id, name) values ({id}, "{name}")''')
        db.connection.commit()
        return redirect('/')
    else:
        return render_template('form.html')

@app.route('/df')
def visualize():
    cur = db.connection.cursor()
    cur.execute('''SELECT * FROM testdb''')
    img = cur.fetchall()
    print(img)
    print(type(img))
    return render_template('df.html', img = img)



if __name__== "__main__":
    app.run(debug=True)