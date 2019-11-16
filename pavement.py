#!/usr/bin/python

from paver.easy import *
import paver.doctools
import os
import glob
import shutil
from time import sleep

@task
def setup():
  sh('python3 setup.py -q install')
  pass

@task
def test():
  sh('nosetests test')
  pass

@task
def clean():
  for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
  for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
  for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
  try:  
    shutil.rmtree(os.getcwd() + "/cover")
  except:
    pass
  pass
  
@task
def run():
  test()
  sleep(2)
  sh('python3 ./src/game_of_life.py')
  pass

@task
@needs(['setup', 'clean', 'test'])
def default():
  pass
