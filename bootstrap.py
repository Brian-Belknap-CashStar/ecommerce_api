#!/usr/bin/env python

# bootstrap.py
# Bootstrap and setup a virtualenv with the specified requirements.txt
import json
import os
import sys
import subprocess
from optparse import OptionParser


usage = """usage: %prog [options]"""
parser = OptionParser(usage=usage)
parser.add_option("-c", "--clear", dest="clear", action="store_true",
                  help="clear out existing virtualenv")
parser.add_option("-u", "--upgrade", dest="upgrade", action="store_true",
                  help="Upgrade")
parser.add_option("-m", "--make", dest="make",
                  help="Make virtual environment", metavar="ENV NAME")
parser.add_option("-j", "--javascript-only", dest="javascript_only",
                  action="store_true",
                  help="Only build the javascript environment")
parser.add_option("-p", "--python-only", dest="python_only",
                  action="store_true",
                  help="Only build the python environment")
parser.add_option("-n", "--no-sym", dest="no_sym",
                  action="store_true",
                  help="Prevent node from creating sym-links on install.")


def exit_in_error(msg, show_usage=False):
    sys.stderr.write("Error: {}\n".format(msg))

    if show_usage:
        parser.print_usage()

    sys.exit(-1)


def execute(project_root_dir):
    (options, pos_args) = parser.parse_args()
    if options.make:
        env_name = os.path.expanduser("~/.virtualenvs/%s" % options.make)
        print("Making environment: %s" % env_name)
        retval = subprocess.call("virtualenv --distribute --no-site-packages %s" % env_name, shell=True)
        if retval:
            exit_in_error('Failed to construct virtualenv. See error(s) above.')

        print("Activating: %s/bin/activate" % env_name)
        retval = subprocess.call("source %s/bin/activate" % env_name, shell=True)
        if retval:
            exit_in_error('Failed to active virtualenv. See error(s) above.')

        os.environ['VIRTUAL_ENV'] = env_name

    if "VIRTUAL_ENV" not in os.environ:
        exit_in_error("$VIRTUAL_ENV not found.\n\n", show_usage=True)

    virtualenv = os.environ["VIRTUAL_ENV"]
    if options.clear:
        retval = subprocess.call(["virtualenv", "--clear", "--distribute", virtualenv])
        if retval:
            exit_in_error('Failed to clean virtualenv. See error(s) above.')


    requirements_files = list(filter(os.path.exists, [os.path.join(project_root_dir, "conf/requirements.txt"), os.path.join(project_root_dir, "conf/test_requirements.txt")]))

    if not requirements_files:
        exit_in_error("Couldn't find suitable requirements file")

    pip_args = ["pip", "install", "--requirement", requirements_files[0]]

    if options.upgrade:
        pip_args.append("--upgrade")

    sym_links = True
    if options.no_sym:
        sym_links = False

    if not options.javascript_only:
        print("Installing python libs")
        retval = subprocess.call(pip_args)
        if retval:
            exit_in_error('Pip failed to install one more libs. See error(s) above.')

    if not options.python_only:
        # install js libs
        javascript_install(project_root_dir, sym_links)


def cmd_exists(cmd):
    return any(os.access(os.path.join(path, cmd), os.X_OK) for path in os.environ["PATH"].split(os.pathsep))


def javascript_install(project_root_dir, sym_links=True):
    if os.path.exists(os.path.join(project_root_dir, 'package.json')):

        npm_command = ["npm", "install"]
        if not sym_links:
            npm_command.append("--no-bin-links")
        print("Installing NPM libs")
        retval = subprocess.call(npm_command)
        if retval:
            exit_in_error('NPM install failed. See error(s) above.')

    if os.path.exists(os.path.join(project_root_dir, 'bower.json')):
        print("Installing Bower libs")
        retval = subprocess.call(["bower", "install", "--config.interactive=false"], cwd=project_root_dir)
        if retval:
            exit_in_error('Bower install failed. See error(s) above.')


if __name__ == "__main__":
    execute(os.path.dirname(__file__))
    sys.exit()
