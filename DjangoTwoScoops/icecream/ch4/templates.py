# -*- coding: UTF-8 -*-
from django import template

__author__ = 'ielkin'

# Stand alone templates test
def test():
    t = template.Template('My name is {{ name }}!')
    c = template.Context({'name': 'Adrian'})
    print t.render(c)
    c = template.Context({'name': 'Ivel'})
    print t.render(c)

    # Passing complex data types using .
    person = {'name': 'Sally', 'age': '43'}
    t = template.Template('{{ person.name }} is {{ person.age }} years old.')
    c = template.Context({'person': person})
    print t.render(c)

    # Calling methods with no params using .
    t = template.Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
    t.render(template.Context({'var': 'hello'}))
    # u'hello -- HELLO -- False'
    t.render(template.Context({'var': '123'}))
    # u'123 -- 123 -- True'