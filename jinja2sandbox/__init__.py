"""
MkDocs-Plugin to enable the Jinja2-Sandbox.

Developed for and tested with MkDocs 1.0.4 on Linux.

:Author:    Roland Koebler <rk@simple-is-better.org>
:Version:   2019-03-20
:License:   MIT
"""
from mkdocs.plugins import BasePlugin
from jinja2.sandbox import SandboxedEnvironment

class Jinja2Sandbox(BasePlugin):
    """Use Jinja2-Sandbox in MkDocs.
    """
    def on_env(self, env, *args, **kwargs):
        env_sandbox = SandboxedEnvironment(loader=env.loader)
        env_sandbox.filters['tojson'] = env.filters['tojson']
        env_sandbox.filters['url'] = env.filters['url']
        return env_sandbox

