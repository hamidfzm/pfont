#!/usr/bin/env python
from app import create_app
from flask.ext.script import Manager

app = create_app('default')
manager = Manager(app)

if __name__ == '__main__':
    app.run(port=5555)