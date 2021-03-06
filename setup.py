from distutils.core import setup

PYBASICBAYES_VERSION = "0.1.2"

# NOTE: cython and moviepy are optional dependencies

setup(name='pybasicbayes',
      version=PYBASICBAYES_VERSION,
      description="Basic utilities for Bayesian inference",
      author='Matthew James Johnson',
      author_email='mattjj@csail.mit.edu',
      url="http://github.com/mattjj/pybasicbayes",
      maintainer='Matthew James Johnson',
      maintainer_email='mattjj@csail.mit.edu',
      packages=['pybasicbayes',
                  'pybasicbayes.internals',
                  'pybasicbayes.examples',
                  'pybasicbayes.util',
                  'pybasicbayes.testing'],
      platforms='ALL',
      keywords=['bayesian', 'inference'],
      install_requires=[
          "numpy",
          "scipy",
          "matplotlib",
          "nose",
      ],
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
      ])

