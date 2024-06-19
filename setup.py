#!/usr/bin/env python3
from distutils.core import setup

setup(name='pyar',
      version='1.0',
      packages=['pyar', 'pyar.data_analysis', 'pyar.interface', 'pyar.data', 'pyar.mlatom', 'pyar.mlatom.aiqm1_model', 'pyar.mlatom.interfaces', 'pyar.AIMNet2', 'pyar.AIMNet2.calculators', 'pyar.AIMNet2.data','pyar.AIMNet2.models'],
      scripts=['pyar/scripts/pyar-cli', 'pyar/scripts/pyar-optimiser', 'pyar/scripts/pyar-tabu',
               'pyar/scripts/pyar-clustering', 'pyar/scripts/pyar-similarity'],
      url='https://github.com/sandipgiri576/pyar',
      license='GPl v3',
      author='Anoop et al',
      author_email='anoop@chem.iitkgp.ac.in',
      description='A Python Code for Aggregation and Reaction',
      install_requires=['autograd', 'numpy', 'sklearn', 'scipy', 'pandas', 'matplotlib'],
      keywords='computational chemistry global minima aggregation automated reaction',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Chemistry'
      ],
      python_requires='>=3.6'
      )
