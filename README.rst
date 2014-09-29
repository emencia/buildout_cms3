This is a buildout which attempts to integrate "DjangoCMS 3.0" and "Django 1.6". Their repository should be temporary and probably removed as all things works and implemented in `emencia-paste-django <https://github.com/emencia/emencia-paste-django>`_.

Obstacles to overcome
=====================

* Check and validate that all used apps are compatible with "Django 1.6", seems there is no major backward incompatible changes, but for some apps it could happen on some little features. Also if possible, we should see if the apps can be Django 1.7 compatible too.
* Re-implement all settings, plugins and code for DjangoCMS that was used with our 2.4.x installs;

So at first this buildout implement basic CMS structure to work, then step by step with re-enable plugins and apps and eventually correct them.

.. WARNING::
           DjangoCMS 3.x suffers from a major bug with it's frontend interface that don't work with some Firefox versions, but seems to work well with Webkit.
           
           Be sure to check the DjangoCMS documentation before to report bugs to ensure to know how the interface works, as it's very different from previous version.

What's done
===========

* Basic buildout for default environment with config we use in Epaster projects;
* Basic DjangoCMS 3 working with minimal stuff (default ckeditor, no plugins, etc..);
* Basic mods like emencia_utils and site_metas;
* Django-filer usage to manage images from the editor;
* Enables debug-toolbar;
* Re-enabled ckeditor customization;

Install
=======

This is our common procedure, so you just have to use the common way with ``make install`` and everything is installed.
