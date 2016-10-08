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
from zope.traversing.api import getName

from cco.schema.interfaces import ISchemaController
from cybertools.composer.schema.interfaces import ISchemaFactory, ISchemaProcessor
from loops.browser.common import BaseView
from loops.common import adapted, baseObject


class SchemaProcessor(object):

    implements(ISchemaProcessor)
    adapts(ISchemaFactory)

    logger = getLogger('cco.schema.SchemaProcessor')
    view = None

    def __init__(self, context):
        self.schemaFactory = context
        self.adapted = context.context
        self.schemaData = {}

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
                if data[0] not in self.scsetup:
                    self.logger.warn('unknown schema controller: %s.' % data[0])
                    return
                setupSctype = self.scsetup[data[0]]
                params = data[1:]
                setupSctype(self, params)

    def setupParentBasedSchemaController(self, params):
        self.logger.info('parent based, params: %s.' % params)

    def setupTypeBasedSchemaController(self, params):
        self.logger.info('type based, params: %s.' % params)
        predicateName = 'use_schema'
        if params:
            predicateName = params[0]
        predicate = self.view.conceptManager.get(predicateName)
        if predicate is None:
            self.logger.warn('predicate %s not found.' % predicateName)
            return
        for c in self.type.getParents([predicate]):
            adp = adapted(c)
            if not ISchemaController.providedBy(adp):
                self.logger.warn('no valid schema controller: %s.' % getName(c))
                return
            sc = adp.schemaData
            for row in sc:
                row = dict(row)     # copy to avoid changing original data
                key = row.pop('fieldName', None)
                if not key:
                    self.logger.warn('empty field name in schema controller: %s.'
                                     % getName(c))
                    continue
                if key in self.schemaData:
                    self.logger.warn('duplicate field name: %s.' % key)
                else:
                    self.schemaData[key] = row

    scsetup = dict(parent=setupParentBasedSchemaController,
                   type=setupTypeBasedSchemaController)

    def process(self, field, **kw):
        if self.view is None:
            view = kw.pop('manager')
            if isinstance(view, BaseView):
                self.setup(view, **kw)
        #print '**3', field.name
        cinfo = self.schemaData.get(field.name)
        if cinfo is not None:
            #print '***', field.name, cinfo
            self.processRequired(field, cinfo.get('required'))
            self.processEditable(field, cinfo.get('editable'))
            self.processDisplay(field, cinfo.get('display'))
        return field

    def processRequired(self, field, setting):
        if setting:
            field.required = ((setting == 'required') or False)

    def processEditable(self, field, setting):
        if setting:
            field.readonly = ((setting == 'hidden') or False)

    def processDisplay(self, field, setting):
        if setting:
            field.visible = ((setting == 'visible') or False)

