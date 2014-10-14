#!/usr/bin/env python
from app import create_app

app = create_app('production')

if __name__ == '__main__':
    app.run()
