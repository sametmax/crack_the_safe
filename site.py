#!/usr/bin/env python
# -*- coding: utf-8 -*-


import string
import pickle
import base64
import random

from path import path
from bottle import run, Bottle, view, static_file, request, redirect

from wsgiserver2 import CherryPyWSGIServer

ROOT_DIR = path(__file__).realpath().parent
GAME_WON = ROOT_DIR / 'game_won.txt'
app = Bottle()


# areyouhuman game
NextUrlContainer = type(str("NextUrlContainer"), (), {'__init__': (lambda s, n: setattr(s, 'next', n))})
MAP = {}
FIRST = PREVIOUS = random.randint(1000000, 10000000)
for x in xrange(666):
    MAP[PREVIOUS] = random.randint(1000000, 10000000)
    PREVIOUS = MAP[PREVIOUS]

MAP[PREVIOUS] = 'wololo.zip'

# api game

API = {}
chars = {l: (i + 1) * 10 for i, l in enumerate('cheating'[::-1])}
chars.update({l: random.randint(1, 3) for l in string.printable if l not in 'cheating'})

API = {c: ['.'] * t for c, t in chars.iteritems()}



@app.route('/', method='POST')
@app.route('/', method='GET')
@view('index')
def index():

    if request.query.get('code'):
        return {'message': "I don't GET it."}

    code = request.forms.get('code')

    if code:
        if code == 'konami':
            if not int(open(GAME_WON).read()):
                with open(GAME_WON, 'w') as f:
                    f.write('1')
                redirect("/konami")
            redirect("/toolate")
        else:
            return {'message': 'Error log : areyouhuman'}

    try:
        return {'message': base64.decodestring(request.query['message'])}
    except:
        return {'message': 'Y U NO OPEN ?'}



@app.route('/areyouhuman')
@app.route('/areyouhuman/<code:int>')
def areyouhuman(code=None):

    global FIRST

    if code is None:
        val = base64.encodestring(pickle.dumps(NextUrlContainer(FIRST)))
        return ("""<p>No log found. Found that instead :</p>
                NextUrlContainer = type("NextUrlContainer",
                                        (),
                                        {'__init__':
                                         (lambda s, n: setattr(s, 'next', n))})
                 # %s"""
                ) % val

    try:
        return base64.encodestring(pickle.dumps(NextUrlContainer(MAP[code])))
    except KeyError:
        return "NOPE"


@app.route('/konami')
@view('winner.html')
def winner():
    return {}


@app.route('/toolate')
@view('toolate.html')
def winner():
    return {}


@app.route('/api.json')
def api():
    global API
    return API


@app.route('/cheating')
def cheating():
    return redirect("/?message=%s" % base64.encodestring('↑↑↓↓←→←→BA'))


@app.route('/wololo.zip')
def serve_wololo():
    return static_file('wololo.zip', root=ROOT_DIR / 'static')


@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root=ROOT_DIR / 'static')


server = CherryPyWSGIServer(
            ('0.0.0.0', 8070), app)
server.start()
