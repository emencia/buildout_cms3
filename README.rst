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

* Buildout configs for all environment with config options we use in Epaster projects;
* DjangoCMS 3 is working with all stuff (ckeditor, plugins, etc..);
* Basic mods like emencia_utils and site_metas;
* Use a recent "django-filebrowser-no-grapelli" version in all apps;
* Enables debug-toolbar;
* Enabled ckeditor customization;
* Zinnia and its cms plugin are enabled;
* Accounts is enabled;
* Contact form is enabled;
* recaptcha mod is enabled;
* admin-tools is enabled;
* sitemap is enabled;
* staticpages is enabled;
* slideshows is enabled;
* porticus is enabled;
* socialaggregator is enabled;
* Zinnia use ckeditor;
* Active Codemirror plugin in ckeditor;
* googletools is enableed;

To resume, all things are back and working. The only app that have not been enabled is our custom cms snippet plugin, we will see in future if it's required.

Install
=======

This is our common procedure, so you just have to use the common way with ``make install`` and everything is installed.

Django 1.7
==========

For now, this is not ready, 1.7 support in DjangoCMS is noted "experimental" and some other apps does not seems to support it, mostly like django-googletools that is unmaintened.

We must wait some months to watch again for a full and clean 1.7 support everywhere.