# apistar-example

this [apistar](https://github.com/encode/apistar) app is an example for my apistar talk.
the slides are [here](http://lucianoratamero.github.io/talks/2017/apistar:%20novo%20framework%20REST%20feito%20para%20python3/) (in pt_BR).

## installation
create a virtualenv with python3 (no python2 support), then install the requirements.
```
pip install -r requirements.txt
```
with the packages installed, you may create your db:
```
apistar migrate
```
then, run the app:
```
apistar run
```