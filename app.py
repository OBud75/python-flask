from flask import Flask, render_template, request, redirect, url_for, flash
from models.person import Person
from models.score import Score
from db.db import get_db, init_db

app = Flask(__name__)
app.secret_key = "secret_key"

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/people')
def list_people():
    search = request.args.get('search')
    conn = get_db()
    cursor = conn.cursor()
    if search:
        cursor.execute("SELECT * FROM people WHERE name LIKE ?", ('%' + search + '%',))
    else:
        cursor.execute("SELECT * FROM people")
    people = cursor.fetchall()
    people_list = [Person(id=row['id'], name=row['name'], age=row['age']) for row in people]
    return render_template('list_people.html', people=people_list)

@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        flash('Person added successfully')
        return redirect(url_for('list_people'))
    return render_template('add_person.html')

@app.route('/edit_person/<int:id>', methods=['GET', 'POST'])
def edit_person(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM people WHERE id = ?", (id,))
    row = cursor.fetchone()
    person = Person(id=row['id'], name=row['name'], age=row['age'])

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor.execute("UPDATE people SET name = ?, age = ? WHERE id = ?", (name, age, id))
        conn.commit()
        flash('Person updated successfully')
        return redirect(url_for('list_people'))

    return render_template('edit_person.html', person=person)

@app.route('/delete_person/<int:id>')
def delete_person(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM people WHERE id = ?", (id,))
    conn.commit()
    flash('Person deleted successfully')
    return redirect(url_for('list_people'))

@app.route('/scores')
def list_scores():
    search = request.args.get('search')
    conn = get_db()
    cursor = conn.cursor()
    if search:
        cursor.execute("SELECT scores.*, people.name as person_name FROM scores LEFT JOIN people ON scores.person_id = people.id WHERE people.name LIKE ?", ('%' + search + '%',))
    else:
        cursor.execute("SELECT scores.*, people.name as person_name FROM scores LEFT JOIN people ON scores.person_id = people.id")
    scores = cursor.fetchall()
    score_list = [Score(id=row['id'], person_id=row['person_id'], score=row['score']) for row in scores]
    return render_template('list_scores.html', scores=score_list)

@app.route('/add_score', methods=['GET', 'POST'])
def add_score():
    if request.method == 'POST':
        person_id = request.form['person_id']
        score = request.form['score']
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (person_id, score) VALUES (?, ?)", (person_id, score))
        conn.commit()
        flash('Score added successfully')
        return redirect(url_for('list_scores'))
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM people")
    people = cursor.fetchall()
    people_list = [Person(id=row['id'], name=row['name'], age=row['age']) for row in people]
    return render_template('add_score.html', people=people_list)

@app.route('/edit_score/<int:id>', methods=['GET', 'POST'])
def edit_score(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores WHERE id = ?", (id,))
    row = cursor.fetchone()
    score = Score(id=row['id'], person_id=row['person_id'], score=row['score'])

    if request.method == 'POST':
        person_id = request.form['person_id']
        score_value = request.form['score']
        cursor.execute("UPDATE scores SET person_id = ?, score = ? WHERE id = ?", (person_id, score_value, id))
        conn.commit()
        flash('Score updated successfully')
        return redirect(url_for('list_scores'))

    cursor.execute("SELECT * FROM people")
    people = cursor.fetchall()
    people_list = [Person(id=row['id'], name=row['name'], age=row['age']) for row in people]
    return render_template('edit_score.html', score=score, people=people_list)

@app.route('/delete_score/<int:id>')
def delete_score(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scores WHERE id = ?", (id,))
    conn.commit()
    flash('Score deleted successfully')
    return redirect(url_for('list_scores'))

if __name__ == '__main__':
    app.run(debug=True)
