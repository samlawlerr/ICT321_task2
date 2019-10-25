from bottle import route, run, request, response
from xml.dom import minidom, Node

def get_lat_lon(latLng):
    print("latLng: %s" % latLng)
    a = latLng.replace(",", "")
    latLngArray = a.split()
    return latLngArray


@route('/getRoute/<routeName>')
#get route function
def get_Route(routeName):
    print(routeName)

    DOMTree = minidom.parse(routeName + ".xml")
    routes = DOMTree.getElementsByTagName("routes")
    print(routeName + ".xml")

    for routte in routes:
        for child in routte.childNodes:
            if child.nodeType == 1:
                if child.nodeType == "routeName":
                    print(routte.toxml())
                    reroute = routte.toxml()

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-type'] = 'application/xml'

    return routes[0].toxml()

@route('/saveRoute')
#save route function
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
                    print("here")
                    for child3 in child2.childNodes:
                        if child3.nodeType == 1:
                            print("here3")
                            for child4 in child3.childNodes:
                                if child4.nodeName == "latlng":
                                # print(child3.nodeName)
                                    print("in child 3")
                                    aArray = get_lat_lon(child4.childNodes[0].nodeValue)
                                    latitude = minidom.parseString("<Latitude>%s</Latitude>" % aArray[0]).documentElement
                                    longitude = minidom.parseString("<Longitude>%s</Longitude>" % aArray[1]).documentElement
                                    child4.parentNode.appendChild(latitude)
                                    child4.parentNode.appendChild(longitude)

    with open(fileName + '.xml', 'w') as f:
        f.write(DOMTree.toxml())


run(host='localhost', port=8080, debug=True)