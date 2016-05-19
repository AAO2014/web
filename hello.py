def wsgi_application(env, start_response):
    import re
    status = '200 OK'
    headers = [
      ('Context-Type', 'text/plain')
    ]
    body = env.QUERY_STRING
    body = re.sub(r'&', body, '\n')
    start_response(status, headers)
    return [ body ]
