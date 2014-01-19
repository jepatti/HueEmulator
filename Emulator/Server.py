import cherrypy
import simplejson
from collections import OrderedDict


num_lights = 5
lights = {str(x):{'hue':0, 'bri':100} for x in range(1, num_lights+1)}

class Lights:

    exposed = True

    def GET(self, light_id=None):

        if light_id == None:
            return('Here are all the lights we have: %s' % lights)
        elif light_id in lights:
            light = lights[light_id]
            return('Light with the ID %s has %s params' % (light_id, light))
        else:
            return('No light with the ID %s :-(' % light_id)

    def PUT(self, light_id, state):
        data = simplejson.loads(cherrypy.request.body.read())
        print light_id, state, data

        if light_id in lights:
            light = lights[light_id]

            light.update(data)

            return('Light with the ID %s now has parameters: %s' % (light_id, light))
        else:
            return('No song with the ID %s :-(' % light_id)

if __name__ == '__main__':

    cherrypy.tree.mount(
        Lights(), '/api/newdeveloper/lights',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()