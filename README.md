# Flask Manage Mechanism

<img align="right" src="https://raw.githubusercontent.com/vroncevic/manage_flask/dev/docs/manage_flask_logo.png" width="25%">

**manage_flask** is toolset for managing Flask App.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![manage_flask_python_checker](https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_python_checker.yml/badge.svg)](https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_python_checker.yml) [![manage_flask_package_checker](https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_package_checker.yml/badge.svg)](https://github.com/vroncevic/manage_flask/actions/workflows/manage_flask_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/manage_flask.svg)](https://github.com/vroncevic/manage_flask/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/manage_flask.svg)](https://github.com/vroncevic/manage_flask/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/manage_flask/dev/docs/debtux.png)

Navigate to **[release page](https://github.com/vroncevic/manage_flask/releases)** download and extract release archive.

To install **manage_flask** type the following

```bash
tar xvzf manage_flask-x.y.z.tar.gz
cd manage_flask-x.y.z/
pip3 install -r requirements.txt
mv manage.py /FlaskApp/
mv /manage_commands/ /FlaskApp/
```

During integration please check comments !

You can use docker to create image/container.

### Dependencies

**manage_flask** requires other modules and libraries

```bash
Flask-Migrate == 2.6.0
Flask-Script  == 2.0.6
```

### Package structure

Expected manage structure

```bash
├── manage.py
manage_commands/
    ├── create_database.py
    ├── create_data.py
    ├── create_superuser.py
    ├── drop_database.py
    └──  __init__.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/manage_flask/badge/?version=latest)](https://manage-flask.readthedocs.io/projects/manage_flask/en/latest/?badge=latest)

More documentation and info at

- [manage_flask.readthedocs.io](https://manage-flask.readthedocs.io/en/latest/)
- [www.python.org](https://www.python.org/)

### Contributing

[Contributing to manage_flask](CONTRIBUTING.md)

### Copyright and Licence

[![license: gpl v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![license apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/manage_flask](https://vroncevic.github.io/manage_flask/)

**manage_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/manage_flask/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
