# PR Checker 

Built for [Code Challenge 38 - Build Your Own Hacktoberfest Checker With Bottle](https://pybit.es/codechallenge38.html)

It's a [Hacktoberfest](https://hacktoberfest.digitalocean.com) like checker that does two things:

* Shows open PRs for [PyBites Code Challenges](https://pybit.es/pages/challenges.html) ([repo](https://github.com/pybites/challenges)) - typically for running month.
* Type in a name and find PRs for the user submitted current month (so we have a bit of  *Hacktoberfest* year round)

Deployed to [https://pybites-prs.herokuapp.com/](https://pybites-prs.herokuapp.com/).

## Heroku

Fork this repo if you want to extend it. To deploy it to Heroku:

* heroku apps:create app-name
* chmod a+x app.py
* echo 'web: python ./app.py' > Procfile
* echo 'python-3.6.2' > runtime.txt
* pip freeze > requirements.txt
* git add .
* git commit -m "heroku prep"
* git push heroku master
* heroku config:set APP_LOCATION=heroku
* heroku config:set GH_USER=abc
* heroku config:set GH_PW=def
