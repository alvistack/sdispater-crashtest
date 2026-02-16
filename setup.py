# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['crashtest', 'crashtest.contracts', 'crashtest.solution_providers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'crashtest',
    'version': '0.4.1',
    'description': 'Manage Python errors with ease',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sdispater/crashtest',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
