#!/bin/bash
# Xiang Wang @ 2016-08-16 11:20:00

http http://localhost:8000/snippets/
http --form POST http://localhost:8000/snippets/ code="$(date +%y-%m-%d\ %H:%M:%S)"
http --json DELETE http://localhost:8000/snippets/1/
http --json PUT http://localhost:8000/snippets/2/ code="$(date +%y-%m-%d\ %H:%M:%S)"

http http://localhost:8000/users/
http http://localhost:8000/users/1/
