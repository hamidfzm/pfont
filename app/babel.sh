#!/bin/bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l fa
pybabel update -i messages.pot -d translations
pybabel compile -f -d translations