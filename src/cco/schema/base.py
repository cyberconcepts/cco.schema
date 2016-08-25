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
A concept adapter to be used as a schema controller.
"""

from zope.app.pagetemplate import ViewPageTemplateFile
from zope.cachedescriptors.property import Lazy
from zope import component
from zope.i18n import translate
from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from cco.schema.interfaces import ISchemaController
from cybertools.composer.schema.browser.common import schema_macros
from cybertools.composer.schema.browser.form import Form
from cybertools.composer.schema.schema import FormState, FormError
from loops.browser.concept import ConceptView
from loops.browser.node import NodeView, getViewConfiguration
from loops.common import AdapterBase
from loops.interfaces import IConcept


_ = MessageFactory('cco.schema')

#template = ViewPageTemplateFile('auth.pt')


class SchemaController(AdapterBase):

    implements(ISchemaController)

    _contextAttributes = AdapterBase._contextAttributes + list(ISchemaController)

    #schemaData = []
