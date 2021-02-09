FROM python:3.7 as base
RUN apt-get update;yes | apt-get install emacs

RUN pip install pipenv

COPY . .
RUN pipenv install

FROM base as wizard
CMD pipenv run python wizard.py

FROM base as normal
CMD pipenv run python solution.py
