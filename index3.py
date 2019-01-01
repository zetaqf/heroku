from bottle import route, run, template, static_file, url, request

@route('/',method='GET')
def msg():
    msg = request.query.msg
    return template('index', msg=msg, url=url)

@route('/static/<filepath:path>', name='static_file')
def static(file_path):
	return static_file(filepath, root='./static')

run(host='localhost', port=8080, debug=True)
