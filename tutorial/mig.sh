#!/bin/bash
# Xiang Wang @ 2016-08-16 11:20:00

./manage.py makemigrations tieba snippets
./manage.py migrate
