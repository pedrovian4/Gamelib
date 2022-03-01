from flask import Flask, redirect, render_template,request,redirect

app = Flask(__name__)

class Game:
    def __init__(self,name, console, type) -> None:
        self.__name= name
        self.__console= console
        self.__type = type
    
    def get_name(self):
        return self.__name
    def get_console(self):
        return self.__console
    def get_type(self):
        return self.__type
    
    
game1 = Game('Mario Bros','SNES', 'Plataform')
game2 = Game('Pokemon Gold','Game Boy', 'MMO RPG')
games_list= [game1,game2]



@app.route('/')
def index():

    return render_template('list.html',title='Games', games= games_list)


@app.route('/assign')
def assign():
    return render_template('assign.html', title='New Game')

@app.route('/create',methods=['POST',])
def create():
    name = request.form['name']
    typee = request.form['type']
    console = request.form['console']
    new_game = Game(name,console, typee)
    games_list.append(new_game)
    return redirect('/')

app.run(debug=True,host='0.0.0.0', port=6060)