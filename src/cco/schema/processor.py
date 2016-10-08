#
#  Copyright (c) 2016 Helmut Merz helmutm@cy55.de
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

"""
Schema processor.
"""

from logging import getLogger
from zope.component import adapts
from zope.interface import implements

from cybertools.composer.schema.interfaces import ISchemaFactory, ISchemaProcessor
from loops.browser.common import BaseView
from loops.common import baseObject


class SchemaProcessor(object):

    implements(ISchemaProcessor)
    adapts(ISchemaFactory)

    logger = getLogger('cco.schema.SchemaProcessor')
    view = None

    def __init__(self, context):
        self.schemaFactory = context
        self.adapted = context.context

    def setup(self, view, **kw):
        self.view = view
        self.schemaControllers = []
        typeToken = getattr(self.view, 'typeToken', None)
        if typeToken is None:
            self.type = baseObject(self.adapted).getType()
        else:
            self.type = view.loopsRoot.loopsTraverse(typeToken)
        opts = view.typeOptions('schema_controller')
        if opts:
            for opt in opts:
                data = opt.split('.')
                sctype = self.scsetup[data[0]]
                params = data[1:]
                sctype(self, params)

    def setupParentBasedSchemaController(self, params):
        msg = 'parent based: %s' % params
        self.logger.info(msg)

    def setupTypeBasedSchemaController(self, params):
        msg = 'type based: %s' % params
        self.logger.info(msg)

    scsetup = dict(parent=setupParentBasedSchemaController,
                   type=setupTypeBasedSchemaController)

    def process(self, field, **kw):
        if self.view is None:
            view = kw.pop('manager')
            if isinstance(view, BaseView):
                self.setup(view, **kw)
        #print '**3', field.name
        return field
