from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys
import os


class PyTest(TestCommand):
    def finalize_options(self):
        os.system('printf "\033c"')
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

requires = [
    'pyramid',
    'pyramid_chameleon'
]

tests_requires = [
    'pytest',
    'webtest'
]

# TODO figure out how to ignore if not in development mode
development_requires = [
    'pyramid_debugtoolbar'
]
requires += development_requires

setup(name='TDF',
      install_requires=requires,
      tests_require=tests_requires,
      cmdclass={'test': PyTest},
      entry_points="""\
      [paste.app_factory]
      main = tdf:main
      """)
