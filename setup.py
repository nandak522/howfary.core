import sys
from setuptools import setup, find_packages

VERSION = '0.1.0'

INSTALL_REQUIRES=[
    'requests',
    ]

TESTS_REQUIRE=('pytest', 'coverage')

if sys.version_info[:2] < (2, 7):
    raise RuntimeError('Requires Python 2.7 or later')

setup(
    name='dica.core',
    packages=find_packages(exclude=["tests"]),
    namespace_packages=['dica'],
    version=VERSION,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    entry_points={'console_scripts': ['howfar = dica.core.cli:howfar']}
)
