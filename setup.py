from setuptools import setup

setup(name="ledtester",
      version="0.1",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Aonghus Lawlor",
      author_email="aonghus.lawlor@ucd.ie",
      licence="GPL3",
      packages=['src'],
      entry_points={
        'console_scripts':['led_tester=src.main:main']
        },
      install_requires=[
          'numpy',
      ],
      )
