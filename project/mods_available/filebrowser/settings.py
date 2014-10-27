# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'filebrowser', before="ckeditor")

FILEBROWSER_VERSIONS_BASEDIR = '_uploads_versions'

FILEBROWSER_MAX_UPLOAD_SIZE = 10*1024*1024 # 10 Mb

FILEBROWSER_NORMALIZE_FILENAME = True