# slack-bot

## Features:
1. When user joins, tell them to update profile with: full name, course, teacher
2. When user types "!help" ping senpai

## Prereq:
- apache
- python3
    ```sh
    $ sudo apt-get install libapache2-mod-wsgi-py3 
    $ sudo a2enmod wsgi 
    $ sudo service apache2 restart
    ```

## How to set up
Dumping some stuff
root@vmhost:/var/www/appname# 
$ chgrp -R www-data <appname>
root@bender:/var/www/appname#
$ chmod -R g+w <appname>
$ mv /var/www/<appname>/<appname>.conf /etc/apache2/sites-available/ 
$ a2ensite slackbot

