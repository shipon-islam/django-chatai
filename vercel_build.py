import subprocess
import sys

# Ensure collectstatic is run during deployment
subprocess.check_call([sys.executable, "manage.py",
                      "collectstatic", "--noinput"])
