
cco.schema - cyberconcepts.org: controlling schema/form appearance via data tables
==================================================================================

  >>> from zope.publisher.browser import TestRequest
  >>> from logging import getLogger
  >>> log = getLogger('cco.schema')

  >>> from loops.setup import addAndConfigureObject, addObject
  >>> from loops.concept import Concept
  >>> from loops.common import adapted

  >>> concepts = loopsRoot['concepts']
  >>> len(list(concepts.keys()))
  10

  >>> from loops.browser.node import NodeView
  >>> home = loopsRoot['views']['home']
  >>> homeView = NodeView(home, TestRequest())


Schema Controller
-----------------

### Type-controlled schemas ###

  >>> from cco.schema.base import SchemaController
