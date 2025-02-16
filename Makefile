# Makefile for Sphinx documentation
back:
	python src/back/mistral_diabetes.py
front:
	python -m http.server 5500 --directory ./src/front 
