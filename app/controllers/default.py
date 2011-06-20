#-*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    return dict(message=T('Hello World'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()

def empleados():
    form=crud.create(db.empleados)
    if form.accepts(request.vars, session):
        response.flash = 'Agregado exitosamente'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Por favor, complete el formulario'
        
    return dict(form=form)

def clientes():
    form=crud.create(db.clientes)
    if form.accepts(request.vars, session):
        response.flash = 'Agregado exitosamente'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Por favor, complete el formulario'
    return dict(form=form)

def peliculas():
    form=crud.create(db.peliculas)
    if form.accepts(request.vars, session):
        response.flash = 'Agregado exitosamente'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Por favor, complete el formulario'    
    return dict(form=form)
    

def prestamos():
    form=crud.create(db.prestamos)
    if form.accepts(request.vars, session):
        response.flash = 'Agregado exitosamente'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Por favor, complete el formulario'
    return dict(form=form)
    
def personal():
    return dict(records=db().select(db.empleados.ALL))

def clientesall():
    return dict(records=db().select(db.clientes.ALL))
    
def peliculasall():
    return dict(records=db().select(db.peliculas.ALL))
    
def prestados():
    return dict(records=db().select(db.prestamos.ALL))

def busqueda():
    "an ajax wiki search page"
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword',
            _onkeyup="ajax('bg_find', ['keyword'], 'target');")),
            target_div=DIV(_id='target'), _type='submit')

def bg_find():
    pattern = '%' + request.vars.keyword.lower() + '%'
    pages = db(db.peliculas.titulo.lower().like(pattern)).select(orderby=db.peliculas.title)
    items = [A(row.titulo, _href=URL('show', args=row.id)) for row in pages]
    return UL(*items).xml()

