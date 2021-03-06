# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('customize me!')

#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Marco Mansilla'
response.meta.description = 'Free and open source full-stack enterprise framework for agile development of fast, scalable, secure and portable database-driven web-based applications. Written and programmable in Python'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2007-2010'


##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    (T('Home'), False, URL('default','index'), [])
    ]

##########################################
## this is here to provide shortcuts
## during development. remove in production
##
## mind that plugins may also affect menu
##########################################

#########################################
## Make your own menus
##########################################

response.menu+=[
    (T('This App'), False, URL('default','index'),
     [
            (T('Controller'), False,
             URL('admin', 'default', 'edit/%s/controllers/%s.py' \
                     % (request.application,request.controller=='appadmin' and
                        'default' or request.controller))),
            (T('View'), False,
             URL('admin', 'default', 'edit/%s/views/%s' \
                     % (request.application,response.view))),
            (T('Layout'), False,
             URL('admin', 'default', 'edit/%s/views/layout.html' \
                     % request.application)),
            (T('Stylesheet'), False,
             URL('admin', 'default', 'edit/%s/static/base.css' \
                     % request.application)),
            (T('DB Model'), False,
             URL('admin', 'default', 'edit/%s/models/db.py' \
                     % request.application)),
            (T('Menu Model'), False,
             URL('admin', 'default', 'edit/%s/models/menu.py' \
                     % request.application)),
            (T('Database'), False,
             URL(request.application, 'appadmin', 'index')),

            (T('Errors'), False,
             URL('admin', 'default', 'errors/%s' \
                     % request.application)),

            (T('About'), False,
             URL('admin', 'default', 'about/%s' \
                     % request.application)),

            ]
   )]

response.menu+= [
    (T('Adding information'), False, URL('default', 'index'),
    [
    (T('Add Users'), False, URL('default','empleados'), []),
    (T('Add Clients'), False, URL('default','clientes'), []),
    (T('Add Movie'), False, URL('default','peliculas'), []),
    (T('Add Rental'), False, URL('default','prestamos'), []),
    ]
   )]

response.menu+= [
    (T('Retreiving information'), False, URL('default', 'index'),
    [
    (T('List Users'), False, URL('default','personal'), []),
    (T('List Clients'), False, URL('default','clientesall'), []),
    (T('List Movies'), False, URL('default','peliculasall'), []),
    (T('List Rentals'), False, URL('default','prestados'), []),
    (T('Search'), False, URL('default','prestamos'), []),
    ]
   )]
   
response.menu+= [
    (T('Modifying information'), False, URL('default','index'),
    [
    (T('Users'), False, URL('default','empleados'), []),
    (T('Clients'), False, URL('default','clientes'), []),
    (T('Movies'), False, URL('default','peliculas'), []),
    (T('Rentals'), False, URL('default','prestamos'), []),
    (T('Search'), False, URL('default','prestamos'), []),
    ]
   )]
