def wa(env, start_response):
    import re
    status = '200 OK'
    headers = [
      ('Context-Type', 'text/plain')
    ]
    resp = env['QUERY_STRING'].split("&")
    r = ''
    for i in resp:
        r += i + "\n"
    start_response(status, headers)
    return [ r ]
