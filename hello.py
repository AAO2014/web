def wa(env, start_response):
    import re
    resp = env['QUERY_STRING'].split("&")
    r = ''
    for i in resp:
        r += i + "\n"
    status = '200 OK'
    headers = [
        ('content-type', 'text/plain'),
        ('content-lenght', len(r)),
    ]

    start_response(status, headers)
    return [ r ]
