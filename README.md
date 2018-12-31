# NGINX Pilot - API
A flask based API for serving and editing nginx configuration

# Tasks to be done
*  [ ] Release v1.0.0 - Being able to manage a reverse proxy
*  [ ] Release v2.0.0 - Being able to manage available and enabled sites

# Requirements
*  python >=3.6
*  (nginx-conf-parser)[https://github.com/Querdos/nginx-conf-parser]

# Contributing
Create a merge request or check the existing ones. Create a virtual environment
with python3:
```bash
$ virtualenv venv
$ source venv/Script/activate # on windows
$ source venv/bin/activate # on *nix

$ make install-dev
```

You're ready to work ! Don't hesitate to contact me if needed.

# Useful commands
Before trying to launch any command, set environment variables:
```bash
$ export FLASK_APP=manage.py
$ export FLASK_SECRET
```

Launch tests:
```bash
$

# Contributors
*  Hamza ESSAYEGH (@querdos)
