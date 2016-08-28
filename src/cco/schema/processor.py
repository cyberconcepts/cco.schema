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

from zope.component import adapts
from zope.interface import implements

from cybertools.composer.schema.interfaces import ISchemaFactory, ISchemaProcessor
from loops.common import baseObject


class SchemaProcessor(object):

    implements(ISchemaProcessor)
    adapts(ISchemaFactory)

    view = None

    def __init__(self, context):
        self.schemaFactory = context
        self.adapted = context.context
        #print '**1', self.adapted

    def setup(self, view, **kw):
        self.view = view
        #print '**2', kw, self.view.request.form
        typeToken = getattr(self.view, 'typeToken', None)
        if typeToken is None:
            self.type = baseObject(self.adapted).conceptType
        else:
            self.type = self.view.loopsRoot.loopsTraverse(typeToken)
        #print '***', self.type.__name__

    def process(self, field, **kw):
        if self.view is None:
            view = kw.pop('manager')
            if view is not None:
                self.setup(view, **kw)
        #print '**3', field.name
        return field
