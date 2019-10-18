from bottle import route, run, request

@route('/hello')
def hello():
    return "Hello World!"

@route('/')
def index():
    """ Display welcome & instruction messages """
    return "<p>Welcome to my extra simple bottle.py powered server !</p> \
    	   <p>The Web service can convert a string into UPPERCASE or lowercase. \
    	   There are two ways to invoke the web service :\
	   <ul> \
	      <li>http://localhost:8080/convert/action_name/your string</li> \
              <li>http://localhost:8080/convert?action=action_name&sentence=your string</li>\
	   </ul> \
	   action_name can be UPPER or lower."


@route('/convert/<action>/<sentence>')
def conversion(action, sentence):
    if action == "UPPER":
        sentence = sentence.upper()
    elif action == "lower":
        sentence = sentence.lower()
    else:
        sentence = "There is something wrong with the service call."

    return sentence

@route('/convert')
def conversion_parameters():
    action = request.query.action
    sentence = request.query.sentence
    if action == "UPPER":
        sentence = sentence.upper()
    elif action == "lower":
        sentence = sentence.lower()
    else:
        sentence = "There is something wrong with the service call."

    return sentence


run(host='localhost', port=8080, debug=True)
