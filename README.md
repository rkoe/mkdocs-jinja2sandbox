mkdocs-jinja2sandbox-plugin
===========================

Author:  Roland Koebler <rk@simple-is-better.org>  
Version: 2019-03-20  
License: MIT  

A MkDocs plugin that enables the Jinja2-sandbox.

Developed for and tested with MkDocs 1.0.4 on Linux.

Install: `python3 setup.py develop`
    
Test: `./test/test.sh`

Enable the plugin in `mkdocs.yml`:

    plugins:
	- jinja2sandbox

**Important:** Always check if the sandbox works.
To test if the sandbox works, you can use the following
in your MkDocs-Jinja2-template:

    <!--({{0 .__class__|string|length and "Jinja2-Sandbox disabled" or "Jinja2-Sandbox ENABLED"}})-->

