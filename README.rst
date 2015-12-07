# django-debug-toolbar-vcs-info 

[![Build Status](https://travis-ci.org/giginet/django-debug-toolbar-vcs-info.svg)](https://travis-ci.org/giginet/django-debug-toolbar-vcs-info) [![Coverage Status](https://coveralls.io/repos/giginet/django-debug-toolbar-vcs-info/badge.svg?branch=master&service=github)](https://coveralls.io/github/giginet/django-debug-toolbar-vcs-info?branch=master)

A Django Debug Toolbar panel to show VCS info

![](https://raw.githubusercontent.com/giginet/django-debug-toolbar-vcs-info/master/images/vcs_info_panel.png)

# Requirements

- Supported Python versions are **2.7**, **3.2-3.5**
- Supported Django versions are **Django1.7-1.9**
- Currently, Git support only

# Installation

- Install using `pip`

```sh
$ pip install django-debut-toolbar-vcs-info
```

- Add `vcs_info_panel` into `INSTALL_APPS` in `settings.py` file

```python
INSTALLED_APPS += (
    'vcs_info_panel',
)
```

- Add the panel you want to use
    - Currently, you can use `GitInfoPanel` only.

```python
DEBUG_TOOLBAR_PANELS = (
...
    'vcs_info_panel.panels.GitInfoPanel',
)
```

# LICENSE

MIT License
