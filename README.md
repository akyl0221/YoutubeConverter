<h1>Web App to download and convert Youtube file to MP3</h1>
<h2>Install</h2>

<p>$ git clone https://github.com/akyl0221/YoutubeConverter.git</p>
<p>$ virtualenv venv -p python3</p>
<p>$ source venv/bin/activate <br>
    $ pip install django celery redis youtube-dl python-decouple<br>
    $ sudo apt redis-server <br>
    $ cd YoutubeConverter <br>
    create .env file and add <br>
    SECRET_KEY = yourSecretKey <br>
    EMAIL_HOST_USER = yourGmail@gmail.com <br>
    EMAIL_HOST_PASSWORD = yourPassword <br>
    $ python manage.py migrate <br>
    $ python manage.py runserver <br>
    $ celery -A youtube_converter.celery worker -l DEBUG -E    
</p>

<h2>Requarements</h2>
<ul>
    <li>Python 3.7.3</li>
    <li>Youtube-dl</li>
    <li>Django v.2.2.1</li>
    <li>Celery v.4.3.0</li>
    <li>Redis v.3.2.1</li>
</ul>
