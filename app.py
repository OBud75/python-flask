from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from tesla_action import StockData, StockGraph
from models.person import Person
from models.score import Score
from db.db import get_db, init_db
from tic_tac_toe import Game, Board
from date_calculator import GestionDate


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

@app.route('/morpion', methods=['GET', 'POST'])
def morpion():
    if 'board' not in session:
        session['board'] = [[" " for _ in range(3)] for _ in range(3)]
    if 'player' not in session:
        session['player'] = "X"
    if 'completed_games' not in session:
        session['completed_games'] = []

    board = Board(position=session['board'])
    game = Game()
    game.board = board
    game.current_player = session['player']

    result = None

    if request.method == 'POST':
        try:
            row_col = request.form['row']
            row, col = map(int, row_col.split('-'))
        except KeyError:
            flash('Invalid move. Please try again.')
            return redirect(url_for('morpion'))

        if game.board.position[row][col] == " ":
            game.board = game.board.make_move(row, col, "X") 
            if game.board.is_won("X"):
                result = 'X a gagné !'
                session['completed_games'].append((game.board.position, result))
                session.pop('board', None)
                session.pop('player', None)
            elif game.board.is_full():
                result = "Match nul !"
                session['completed_games'].append((game.board.position, result))
                session.pop('board', None)
                session.pop('player', None)
            else:
                game.play_computer_move() 
                if game.board.is_won("O"):
                    result = 'L\'ordinateur a gagné !'
                    session['completed_games'].append((game.board.position, result))
                    session.pop('board', None)
                    session.pop('player', None)
                elif game.board.is_full():
                    result = "Match nul !"
                    session['completed_games'].append((game.board.position, result))
                    session.pop('board', None)
                    session.pop('player', None)
            session['board'] = game.board.position

    return render_template('morpion.html', board=game.board.position, player="X", result=result, completed_games=session['completed_games'])


@app.route('/reset_board')
def reset_board():
    session['board'] = [[" " for _ in range(3)] for _ in range(3)]
    session['player'] = "X"
    return redirect(url_for('morpion'))

@app.route('/clear_history')
def clear_history():
    session.pop('completed_games', None)
    return redirect(url_for('morpion'))




@app.route('/show_date_page')
def show_date_page():
    return render_template('show_date_page.html')


@app.route('/generate_stock_graph')
def generate_stock_graph():
    tesla_stock = StockData("TSLA")
    tesla_stock.fetch_data(start_date="2023-01-01", end_date="2023-12-01")
    StockGraph.plot_stock(tesla_stock.data, title="Évolution de l'action Tesla (TSLA)", output_file="models/tesla_stock_2023.png")
    return redirect(url_for('show_stock_graph'))

@app.route('/show_stock_graph')
def show_stock_graph():
    return render_template('show_stock_graph.html')

@app.route('/get_stock_image')
def get_stock_image():
    return send_from_directory('models', 'tesla_stock_2023.png')





@app.route('/date_calculator', methods=['GET', 'POST'])
def date_calculator():
    date_result = None
    if request.method == 'POST':
        try:
            days = int(request.form['days'])
            gestion_date = GestionDate()
            date_result = gestion_date.date_il_y_a_x_jours(days)
        except ValueError:
            flash('Veuillez entrer un nombre valide.')
    return render_template('date_calculator.html', date_result=date_result)


if __name__ == '__main__':
    app.run(debug=True)
