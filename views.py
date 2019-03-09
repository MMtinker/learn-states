from MyApp import *

@app.route('/')
def index():

    return '<h1>Hello</h1>'

@app.route('/states/', methods=['post', 'get'])
def states(statesGuess=[], statesLeft=len(stateList)-len(statesGuess)):
    message =''

    if session.get('reset'):
        session['reset'] = False
        statesGuess.clear()

    if request.method == 'POST':
        # read the posted values from the UI
        _name = request.form.get('stateName')
        _reset = request.form.get('reset') != None
        # print(f'Got value: {_name}')
        # print(f'Check box: {_reset}')
        if _reset:
            session['statesGuess'] = statesGuess
            print(f'SESSIONS STATESGUESS VALUE: {session["statesGuess"]}')
            return redirect(url_for('reset'))

        if _name in stateList:
            if _name in statesGuess:
                message = f'You already have guessed {_name}. Try again...'
            else:
                message = 'You got it!'
                statesGuess.append(_name)
        else:
            message = 'Try again...'

    statesLeft = len(stateList) - len(statesGuess)
    if statesLeft == 0:
        message = 'YOU DID IT! GREAT JOB!'

    return render_template('states.html', message=message, statesLeft=statesLeft, statesGuess=statesGuess)


@app.route('/reset', methods=['post', 'get'])
def reset():

    session['reset'] = True
    statesGuess = session.get('statesGuess')


    return render_template('giveup.html', stateList=stateList, statesGuess=statesGuess)