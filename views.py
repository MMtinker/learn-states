from MyApp import *

@app.route('/')
def index():

    return '<h1>Hello</h1>'

@app.route('/states/', methods=['post', 'get'])
def states(statesGuess=[], statesLeft=len(stateList)-len(statesGuess)):
    message =''
    if request.method == 'POST':
        # read the posted values from the UI
        _name = request.form.get('stateName')
        _reset = request.form.get('reset') != None
        print(f'Got value: {_name}')
        print(f'Check box: {_reset}')
        if _reset:
            statesGuess.clear()
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


@app.route('/update',methods=['POST'])
def update():

    print("Update method")

    if request.method == 'POST':
        # read the posted values from the UI
        _name = request.form['inputName']
        print(f'Got value: {_name}')
        statesLeft = _name
        return redirect(url_for('states', statesLeft=_name))


    # return redirect(url_for('beginStates', statesLeft=statesLeft))
    return render_template('states.html', statesLeft=statesLeft)