# durkheim
A sandbox for IoT device programming using a Flask webapp as an interface.

"Collective conscious", the term was introduced by the French sociologist Émile Durkheim.


ENVIRONMENT:
    
    Python 2.7
        virtualenv
        Flask
        AWS IoT Python SDK
            http://docs.aws.amazon.com/iot/latest/developerguide/protocols.html
        



TOOO:
    
    Web App
        
        - Implement AWS IoT API
            https://github.com/aws/aws-iot-device-sdk-python

        - Build out home page

        - Deploy to AWS cloud server

    IoT
        - Build first IoT device to connect to web app


SET UP:
    
    - Install Python 2.7

    - in Terminal...
        $ cd /durkheim-github/root-directory/
        $ . /venv/bin/activate
        $ export FLASK_APP=routes.py
        $ python2.7 -B -m flask run

    - in browser visit...
        http://127.0.0.1:5000/

