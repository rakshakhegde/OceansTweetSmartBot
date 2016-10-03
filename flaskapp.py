import flask

app = flask.Flask(__name__)

import hacks.oceanstweet
app.register_blueprint(hacks.oceanstweet.app, url_prefix='/oceanstweet')

@app.route('/')
def home():
	return 'App is alive!'

@app.route('/<path:resource>')
def serveStaticResource(resource):
	return flask.send_from_directory('static/', resource)

@app.route('/env/')
def env():
	import os
	response_body = ['%s: %s' % (key, value)
		for key, value in sorted(os.environ.items())]
	return '\n'.join(response_body), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
