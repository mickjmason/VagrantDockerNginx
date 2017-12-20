#!/bin/bash

vagrant ssh-config > ./tests/ssh-config
py.test -v ./tests/tests.py
py.test -v --hosts=default --ssh-config=./tests/ssh-config ./tests/remote-tests.py

