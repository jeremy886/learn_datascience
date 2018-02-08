#####################
Working with Python 3
#####################

Development
###########

pyenv
=====

pyenv `github <https://github.com/yyuu/pyenv-virtualenv>`_

commands
--------

install python interpreters
   pyenv install 3.6.0

create virtualenv with pyenv
   pyenv virtualenv 3.6.0 my-virtual-env

Create virtualenv from the current interpreter version::

   ➜  ~ pyenv version   
   3.6.0 (set by /Users/apple/.pyenv/version)
   
   ➜  ~ pyenv virtualenv emacs
   Requirement already satisfied: setuptools in /Users/apple/.pyenv/versions/3.6.0/envs/emacs/lib/python3.6/site-packages
   Requirement already satisfied: pip in /Users/apple/.pyenv/versions/3.6.0/envs/emacs/lib/python3.6/site-packages
   

set the global interpreter (default)
   pyenv global 3.6.0
   
list installed interpreters and virtual environments
   pyenv versions
   
list installed environments
   pyenv virtualenvs

activate and deactivate a virtual environment
   pyenv activate <name>
   
   pyenv deactivate <name>

Delete existing virtualenv
   pyenv uninstall my-virtual-env

Examples:

Show installed interpreters and virtual environments::

   ~ pyenv versions
     system
     2.7.13
     2.7.13/envs/py27-lektor
     3.5.2
   * 3.6.0 (set by /Users/apple/.pyenv/version)
     3.6.0/envs/py36-lektor
     3.6.0/envs/py36-nikola
     3.6.0/envs/pydata
     3.6.0/envs/sphinx
     py27-lektor
     py36-lektor
     py36-nikola
     pydata
     sphinx

When you uninstall an interpreter, it will ask you to remove the associated virtualenv::

    ➜ ~ pyenv uninstall 2.7.13
   pyenv-virtualenv: remove /Users/apple/.pyenv/versions/2.7.13/envs/py27-lektor? y
   pyenv: remove /Users/apple/.pyenv/versions/2.7.13? y

I want to know which virtualenv attaches to which interpreter::

   ➜ ~ pyenv virtualenvs
     3.6.0/envs/py36-lektor (created from /Users/apple/.pyenv/versions/3.6.0)
     3.6.0/envs/py36-nikola (created from /Users/apple/.pyenv/versions/3.6.0)
     3.6.0/envs/pydata (created from /Users/apple/.pyenv/versions/3.6.0)
     3.6.0/envs/sphinx (created from /Users/apple/.pyenv/versions/3.6.0)
     py36-lektor (created from /Users/apple/.pyenv/versions/3.6.0)
     py36-nikola (created from /Users/apple/.pyenv/versions/3.6.0)
     pydata (created from /Users/apple/.pyenv/versions/3.6.0)
     sphinx (created from /Users/apple/.pyenv/versions/3.6.0)

I want to know what packages installed for sphinx::

   ➜  ~ pyenv activate sphinx 
   pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
   (sphinx) ➜  ~ pip list
   DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
   alabaster (0.7.9)
   attrs (15.2.0)
   Babel (2.3.4)
   beautifulsoup4 (4.4.1)
   click (6.3)
   colorama (0.3.7)
   doc2dash (2.1.0)
   docutils (0.13.1)
   imagesize (0.7.1)
   Jinja2 (2.8)
   lxml (3.4.4)
   Markdown (2.6.7)
   Markups (2.0.0)
   MarkupSafe (0.23)
   pip (9.0.1)
   pyenchant (1.6.8)
   Pygments (2.1.3)
   PyQt5 (5.7.1)
   pytz (2016.10)
   requests (2.12.4)
   ReText (6.0.2)
   setuptools (28.8.0)
   sip (4.19)
   six (1.10.0)
   snowballstemmer (1.2.1)
   Sphinx (1.3.5)
   sphinx-rtd-theme (0.1.9)
   zope.interface (4.1.3)

It's getting messy. If I keep a list, can it help?

VirtualEnv targets
==================

I will install co-dependent targets in one virtualenv. For example, I install sphinx to write rst docs and therefore I need a rst editor.

It's okay to break down to too samller chunks. You will have a longer list but no pain when you want to remove an virtual environment.

sphinx
------

* sphinx
* retext (editor)


