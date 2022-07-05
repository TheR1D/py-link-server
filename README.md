# PyLinkServer
Simple URL shortener server written in Python using Flask. Allows you to create/open generated short URLs.
  
### Install
Start server using Docker
```bash
git clone https://github.com/TheR1D/py-link-server.git
cd py-link-server
docker build -t py-link-server .
docker run -d py-link-server
```
  
Or manual start:
```bash
git clone https://github.com/TheR1D/py-link-server.git
cd py-link-server
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python init_database.py
python server.py
```
  
### Usage
There is handy swagger Web UI available at: http://127.0.0.1/ui
