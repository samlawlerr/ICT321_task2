from bottle import route, run, request, response
from xml.dom import minidom, Node

@route('/getroute/<planeroute>')
def get_route(planeroute):
    print(planeroute)
    DOMTree = minidom.parse("planeroute.xml")

    route = DOMTree.getElementsByTagName("book")
    for child in DOMTree.childNodes:
        if child.nodeType == 1:
            for child2 in child.childNodes:
                if child2.nodeType == 1:
                    for child3 in child2.childNodes:
                        if child3.nodeType == 1:
                            if child3.nodeName == "title":
                                if child3.childNodes[0].nodeValue == planeroute:
                                    print(child3.parentNode.toxml())
                                    route = child3.parentNode.toxml()

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-type'] = 'application/xml'
    return route

@route('/saveRoute')
def save_route():


    routes = request.query.route
    print(routes)
    DOMTree = minidom.parseString(routes)
    fileName = request.query.routeName
    print(fileName)

    for child in DOMTree.childNodes:
        if child.nodeType == 1:
            for child2 in child.childNodes:
                if child2.nodeType == 1:
                    for child3 in child2.childNodes:
                        if child3.nodeType == 1:
                            print("   ", child3.nodeName, ", ", child3.childNodes[0].nodeValue)
                            if child3.nodeName == "LatLon":
                                aArray = (child3.childNodes[0].nodeValue)
                                Latitude = minidom.parseString("<Latitude>%s</Latitude>" % aArray[0]).documentElement
                                Longitude = minidom.parseString("<Longitude>%s</Longitude>" % aArray[1]).documentElement
                                child3.parentNode.appendChild(Latitude)
                                child3.parentNode.appendChild(Longitude)

    fileName = "routeName"  # change to route name in the future
    with open(fileName + '.xml', 'w') as f:
        f.write(DOMTree.toxml())


    with open(fileName + '.xml', 'w') as f:
        f.write(DOMTree.toxml())


run(host='localhost', port=8080, debug=True)