This is a buildout which attempts to integrate "DjangoCMS 3.0.x" and "Django 1.6.x". This repository should be temporary and probably will be removed when all things will works in `emencia-paste-django <https://github.com/emencia/emencia-paste-django>`_.

Obstacles to overcome
=====================

* Check and validate that all used apps are compatible with "Django 1.6", seems there is no major backward incompatible changes, but for some apps it could happen on some little features. Also if possible, we should see if the apps can be Django 1.7 compatible too.
* Re-implement all settings, plugins and code for DjangoCMS that was used with our 2.4.x installs;

So this buildout has started with a basic CMS structure to work then step by step we enable mods and eventually correct them.

.. WARNING::
           DjangoCMS 3.x suffers from a major bug with it's frontend interface that don't work with some Firefox versions (probably version<32), but seems to work well with Webkit.
           
           But be sure to check the `DjangoCMS documentation <http://docs.django-cms.org/en/latest/getting_started/integrate.html#up-and-running>`_ before to report bugs to ensure to know how the interface works, as it's very different from previous version.

What have been done
===================

* Basic buildout for default environment with config we use in Epaster projects;
* Basic DjangoCMS 3 working with minimal stuff (default ckeditor, no plugins, etc..);
* Basic mods like emencia_utils and site_metas;
* Use Django-filer to manage images instead of filebrowser and its cms plugin is enabled;
* Enables debug-toolbar;
* Re-enabled ckeditor customization;
* Zinnia and its cms plugin are enabled;
* Accounts is enabled;
* Contact form is enabled;
* admin-tools is enabled;
* sitemap is enabled;
* staticpages is enabled;
* slideshows is enabled;
* porticus is enabled;
* socialaggregator is enabled;
* Zinnia use ckeditor;
* Active Codemirror plugin in ckeditor;

Notes
=====

* Should see to use filebrowser instead of django-filer that is not really as good as FB was, plus filebrowser-no-grapelli package is maintained and packaged again !
* Ckeditor in Zinnia does not have the exact same display than the ckeditor in CMS;
* ReCaptcha 1.0.2 usage in contact form seems broken, the captcha image is not added to the DOM despite it is effectively loaded;

Install
=======

This is our common procedure, so you just have to use the common way with ``make install`` and everything is installed.

