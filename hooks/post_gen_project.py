import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', '{{cookiecutter.repo_name}} init'])

subprocess.call(['yarn', 'install'])
