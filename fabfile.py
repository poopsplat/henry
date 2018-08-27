from fabric.api import *
import os

env.hosts = ['henry.firebelly.co']
env.user = 'firebelly'
env.path = '~/Sites/henry'
env.remotepath = '/home/firebelly/webapps/henry'
env.git_branch = 'master'
env.warn_only = True
env.remote_protocol = 'http'

def deploy():
  update()

def update():
  with cd(env.remotepath):
    run('git pull origin {0}'.format(env.git_branch))
