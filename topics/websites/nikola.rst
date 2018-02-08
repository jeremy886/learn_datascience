Nikola - Static Site Generator
##############################


Code: `Github <https://getnikola.com/>`_

Docs: `Getting started <https://getnikola.com/getting-started.html>`_


Get started
===========

Steps::

   nikola init --demo datamofa_site
   cd datamofa_site
   vi conf.py
   nikola build
   nikola new_post -e
   export EDITOR=emacs
   nikola new_post -e
   nikola build

   nikola serve --browser

   # remove demo content
   # rm posts/1.rst
   
   nikola check --clean-files
   nikola build
   nikola orphans

   # after setting up github repo (see below)
   nikola github_deploy

Github
------

Git::

   cd datamofa_site
   git init .
   git remote add origin https://github.com/jeremy886/datamofa_site.git



Setup branches and remotes in conf.py::

   GITHUB_SOURCE_BRANCH = 'master'
   GITHUB_DEPLOY_BRANCH = 'gh-pages'
   GITHUB_REMOTE_NAME = 'origin'
   GITHUB_COMMIT_SOURCE = True

Add to .gitignore::

   cache
   .doit.db
   __pycache__
   output

Add CNAME
   echo "www.datamofa.club" > files/CNAME


