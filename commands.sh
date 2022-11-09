#!/usr/bin/env bash

mkdir $1
cd $1
pip install virtualenv
virtualenv env
source env\bin\activate

pip install -r requirements.txt
django-admin startproject $1 .
clear