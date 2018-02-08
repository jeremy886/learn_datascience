Emacs for Python
################

References::

   http://elpy.readthedocs.io/en/latest/introduction.html

Check emacs
===========

version::

   emacs --version
   # if it's too old, install a new emacs by home brew
   brew install emacs
   
   alias emacs=/usr/local/Cellar/emacs/25.1/bin/emacs
   # you should add the alias to .zshrc (or .bashrc)


Install packages
================

packages required::

   pip install elpy jedi rope

   pip install autopep8
   pip install yapf

Modify .emacs::

   (require 'package)
   (add-to-list 'package-archives
   '("marmalade" . "http://marmalade-repo.org/packages/"))
   
   
   (require 'package)
   (add-to-list 'package-archives
                '("elpy" . "http://jorgenschaefer.github.io/packages/"))

In emacs::

   M is meta ("alt", enable it in your terminal perference)
   RET is "enter"
   
   M-x package-install RET elpy RET

Add these to .emacs again:

   (package-initialize)
   (elpy-enable)
