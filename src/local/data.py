#!/usr/bin/env python

# local contains things that are going to be specific to the current machine, so that you can have properly separated data, like database location and password - I then soft-link the machine-specific versions (say "machine1-localconfig.py") to local/localconfig.py and then can "import localconfig" in settings.py
# I generally put middleware that's project-specific inside a project, and middleware that's not project-specific in common/middleware/ 