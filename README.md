# Flask Web Application

This is an example flask web application for ubuntu server

## Installation for server configuration
```bash
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
```

## Configuration for Apache2 conf file
Append these configuration after DocumentRoot line of /etc/apache2/sites-enabled/000-default.conf file
```bash
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi
<Directory flaskapp>
    WSGIProcessGroup flaskapp
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
```

## Download the Flask App and Configure for Apache2
```bash
git clone https://github.com/chuuhtetnaing/rsbpi_flask.git
sudo ln -sT ./rsbpi_flask /var/www/html/rsbpi_flask
cd rsbpi_flask
pip install -r requirements.txt
```

## Restart the Apache server
```bash
sudo service apache2 restart
```