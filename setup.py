from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon'
]

# TODO figure out how to ignore if not in development mode
development_requires = [
    'pyramid_debugtoolbar'
]
requires += development_requires

setup(name='TDF',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tdf:main
      """)
