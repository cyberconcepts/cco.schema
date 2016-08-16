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
Interfaces for controlling and configuring schemas.
"""

from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope import schema

from cybertools.composer.schema.grid.interfaces import KeyTable


_ = MessageFactory('cco.schema')


class ISchemaController(Interface):

    schemaData = KeyTable(title=_(u'Schema Data'),
        description=_(u'Schema Data'),
        required=False)
