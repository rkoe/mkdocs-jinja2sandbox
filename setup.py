#!/usr/bin/env python3
from setuptools import setup

setup(
    name='mkdocs-jinja2sandbox-plugin',
    version='0.1',
    description='Enable Jinja2-Sandbox in MkDocs',
    keywords='mkdocs jinja2 sandbox',
    url='https://www.simple-is-better.org/TODO',
    author='Roland Koebler',
    author_email='rk@simple-is-better.org',
    license='MIT',
    install_requires=['mkdocs>=1.0.4'],
    packages=["jinja2sandbox"],
    entry_points={
        'mkdocs.plugins': [
            'jinja2sandbox = jinja2sandbox:Jinja2Sandbox'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
	'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
