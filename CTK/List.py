# -*- coding: utf-8 -*-
#
# CTK: Cherokee Toolkit
#
# Authors:
#      Alvaro Lopez Ortega <alvaro@alobbs.com>
#
# Copyright (C) 2010-2011 Alvaro Lopez Ortega
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public
# License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from Widget import Widget
from Container import Container
from util import props_to_str

ENTRY_HTML = '<%(tag)s id="%(id)s" %(props)s>%(content)s</%(tag)s>'

class ListEntry (Container):
    def __init__ (self, _props={}, tag='li'):
        Container.__init__ (self)
        self.tag   = tag
        self.props = _props.copy()

    def Render (self):
        render = Container.Render (self)

        if 'id' in self.props:
            self.id = self.props['id']

        props = {'id':      self.id,
                 'tag':     self.tag,
                 'props':   props_to_str(self.props),
                 'content': render.html}

        render.html = ENTRY_HTML %(props)
        return render


class List (Container):
    def __init__ (self, _props={}, tag='ul'):
        Container.__init__ (self)
        self.tag   = tag
        self.props = _props.copy()

    def Add (self, widget, props={}):
        assert isinstance(widget, Widget) or widget is None or type(widget) is list

        entry = ListEntry (props.copy())
        if widget:
            if type(widget) == list:
                for w in widget:
                    entry += w
            else:
                entry += widget

        Container.__iadd__ (self, entry)

    def __iadd__ (self, widget):
        self.Add (widget)
        return self

    def Render (self):
        render = Container.Render (self)

        props = {'id':      self.id,
                 'tag':     self.tag,
                 'props':   props_to_str(self.props),
                 'content': render.html}

        render.html = ENTRY_HTML %(props)
        return render
