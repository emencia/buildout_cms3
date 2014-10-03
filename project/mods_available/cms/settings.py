# -*- coding: utf-8 -*-

MIDDLEWARE_CLASSES = add_to_tuple(MIDDLEWARE_CLASSES,
    'django.middleware.locale.LocaleMiddleware',
    before='django.middleware.common.CommonMiddleware')


MIDDLEWARE_CLASSES += (
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'south',  # intelligent schema and data migrations
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'djangocms_snippet',
    'cmsplugin_filer_image',
    #'reversion', # raise error on south migration, there is a bug with the last version and django1.6
)

TEMPLATE_CONTEXT_PROCESSORS = add_to_tuple(TEMPLATE_CONTEXT_PROCESSORS,
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

CMS_TEMPLATES = (
    ('cms/1_cols.html', '1 column'),
    ('cms/2_cols.html', '2 columns'),
    ('cms/3_cols.html', '3 columns'),
)

# Enable 'cmsplugin_filer_image' usage in ckeditor
TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'
