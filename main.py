from flask import Flask, flash, redirect, render_template,request,redirect, session


app = Flask(__name__)
app.secret_key = 'AWP'
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
    
userLogged=False
game1 = Game('Mario Bros','SNES', 'Plataform')
game2 = Game('Pokemon Gold','Game Boy', 'MMO RPG')
games_list= [game1,game2]



@app.route('/')
def index():
    return render_template('list.html',title='Games', games= games_list)




@app.route('/assign')
def assign():
        #check 
        if 'user_logged' not in session or session['iser_logged']==None:
            return redirect('/login')
        return render_template('assign.html', title='New Game')

@app.route('/create',methods=['POST',])
def create():
    name = request.form['name']
    typee = request.form['type']
    console = request.form['console']
    new_game = Game(name,console, typee)
    games_list.append(new_game)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/auth', methods=['POST',])
def auth():
    #store the information in the cookie

    session['password']= request.form['password']
    session['user_logged']= request.form['user']

    if 'password' == session['password'] and 'Pedro' == session['user_logged']:
        flash( '{} was logged\nlogin was sucessfull'.format(session['user_logged'])) 
        return redirect('/assign')
    else:
        flash('Password or Username wrong')
        return redirect('/login')
    
    
@app.route('/logout')
def logout():
    if userLogged:
        session['user_logged']=None
        session['password']=None
        flash('logged out')
        return redirect('/login')
    else:
        flash("No user in looged in")
        
        
app.run(debug=True,host='0.0.0.0', port=6060)