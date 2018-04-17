# -*- coding: iso-8859-15 -*-

"""
routes
======

This module establishes and defines the Web Handlers and Websockets
that are associated with a specific URL routing name. New routing
associations must be defined here.

Notes
-----
For more information regarding routing URL and valid regular expressions
visit: http://www.tornadoweb.org/en/stable/guide/structure.html
"""

import os
import sys
import candax.web as web
import candax.rest.alarms_rest as alarms_rest
import candax.rest.residential_units_rest as residential_units_rest
import candax.rest.houses_rest as houses_rest
import candax.rest.locks_rest as locks_rest
import candax.rest.hubs_rest as hubs_rest
import candax.rest.alarms_owner_rest as alarms_owner_rest
import candax.rest.alarms_admin_rest as alarms_admin_rest
import candax.rest.administrators_rest as administrators_rest
import candax.rest.owners_rest as owners_rest
# import candax.rest as rest

# Define new rest associations
REST = [
    (r'/alarms(/?(.+)?)', alarms_rest.MainHandler), #YALE
    (r'/residentialUnits(/?(.+)?)', residential_units_rest.MainHandler),
    (r'/houses(/?(.+)?)', houses_rest.MainHandler),
    (r'/hubs(/?(.+)?)', hubs_rest.MainHandler),
    (r'/locks(/?(.+)?)', locks_rest.MainHandler),
	(r'/owners/?(.+)?/passwords/(/?(.+)?)', password_rest.MainHandler),
    (r'/owners(/?(.+)?)', owners_rest.MainHandler),
    (r'/administrators(/?(.+)?)', administrators_rest.MainHandler),
    (r'/history/owners/?(.+)?', alarms_owner_rest.MainHandler), #Propietario
    (r'/history/administrators/?(.+)?', alarms_admin_rest.MainHandler) #Admin
]

# Define new web rendering route associations
WEB = [
    (r'/flights', web.flights_handler.MainHandler)
]

ROUTES = REST + WEB
