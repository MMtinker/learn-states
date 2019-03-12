#from flask import Flask, render_template, request, json, redirect, url_for, session
from flask import *
import os
# import itertools

# consequent_integers = itertools.count()
statesGuess = []
stateList=[
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming'
]


app = Flask(__name__)
# app.secret_key = os.urandom(16)
app.secret_key = 'mY_s3cr3t@!'

# from views import *
# TEMP

# def random():
#     session['number'] = consequent_integers.next()
#     return None

@app.route('/')
def index():

    return '<h1>Hello</h1>'

@app.route('/states', methods=['post', 'get'])
def states(statesGuess=[], statesLeft=len(stateList)-len(statesGuess)):
    message =''
    if 'number' not in session:
        session['number'] = os.urandom(6)

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

    return render_template(
        'states.html',
        message=message,
        statesLeft=statesLeft,
        statesGuess=statesGuess,
        sessionNr=session['number']
    )


@app.route('/reset', methods=['post', 'get'])
def reset():

    session['reset'] = True
    statesGuess = session.get('statesGuess')


    return render_template('giveup.html', stateList=stateList, statesGuess=statesGuess)

# TEMP



if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(threaded=True)
    # app.secret_key = consequent_integers.next()
    app.run()