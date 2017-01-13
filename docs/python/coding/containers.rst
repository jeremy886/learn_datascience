Containers
##########

https://www.safaribooksonline.com/library/view/python-data-structures/9781771373517/part62.html


namedtuple
==========

https://docs.python.org/3/library/collections.html#collections.namedtuple

The field_names are a single string with each fieldname separated by whitespace and/or commas, for example 'x y' or 'x, y'. Alternatively, field_names can be a sequence of strings such as ['x', 'y'].

>>> # Basic example
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
>>> p[0] + p[1] 

defaultdict
===========

>>> from collections import defaultdict
>>> ice_cream = defaultdict('Vanilla')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: first argument must be callable or None
>>> ice_cream = defaultdict(lambda: 'Vanilla')
>>> ice_cream['Sarah'] = 'Chunky Monkey'
>>> ice_cream['Abdul'] = 'Butter Pecan'
>>> ice_cream['Sarah']
'Chunky Monkey'
>>> ice_cream['Joe']
'Vanilla'
