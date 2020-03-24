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
1. Create a droplet (use $5 plan) and make sure port 80 is open
2. Run ```sudo apt update && sudo apt install apache2```
3. Run this:
    ```sh
    $ sudo apt-get install libapache2-mod-wsgi-py3 
    $ sudo a2enmod wsgi # this might say: "Module wsgi already enabled"
    $ sudo service apache2 restart
    ```
4. Run this:
    ```sh
    $ cd /var/www/
    $ git clone https://github.com/StuyCSDojo/slackbot.git
    $ cd slackbot
    $ chgrp -R www-data slackbot
    $ chmod -R g+w slackbot
    $ cp /var/www/slackbot/slackbot.conf /etc/apache2/sites-available/slackbot.conf
    $ a2ensite slackbot
    $ service apache2 restart
    ```
