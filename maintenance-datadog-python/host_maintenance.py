
import requests
import schedule
import time
from datadog import initialize,  api
options = {
    'api_key': 'api_value',
    'app_key': 'app_value'
}

initialize(**options)

def check_status():
    title = "Maintenance"
    text = "Server Maintenance"
    tags = ['version:1', 'application:web']
    r = requests.get("https://m1.svc-stage.appcompany.com/maintenance",  headers = {"X-AppCompany-Maintenance-Request":"True"})
    print r.status_code
    if(int(r.status_code) == 503):
        api.Event.create(title=title, text=text, tags=tags)
        print "Maintenance event created"

schedule.every(2).seconds.do(check_status)

while True:
    schedule.run_pending()
    time.sleep(1)
