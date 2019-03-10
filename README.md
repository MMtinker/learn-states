# Learn States

Flask Python code

Deployment to Heroku

TODO - multi user capability

HEROKU deployment:
https://realpython.com/flask-by-example-part-1-project-setup/#project-setup

-----------------------------------

https://learn-states-prod.herokuapp.com/ | https://git.heroku.com/learn-states-prod.git

https://learn-states.herokuapp.com/ | https://git.heroku.com/learn-states.git

https://learn-states-staging.herokuapp.com/ | https://git.heroku.com/learn-states-staging.git

---------------

For staging: git push stage master
For production: git push prod master

-----

If issues with Heroku GIT keys:
heroku keys:add ~/.ssh/id_rsa.pub
If you don't have a public key, Heroku will prompt you to add one automatically which works seamlessly. Just use:

heroku keys:add
To clear all your previous keys do :

heroku keys:clear
To display all your existing keys do :

heroku keys

