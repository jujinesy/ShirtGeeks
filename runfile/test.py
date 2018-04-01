def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2


# uwsgi --http :8000 --wsgi-file test.py
# uwsgi --http :8000 --home /home/ubuntu/venv --chdir /home/ubuntu/ShirtGeeks/src/ --module conf.wsgi