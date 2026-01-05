# instrument_pkg_template
A Python package template for instruments compatible with the SWxSOC processing pipeline

This template also uses the `jinja2_time` package to automatically insert the current year into the license file. If you do not have this package installed, you can install it via pip:

    pip install jinja2_time

To use this template, first install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html) then run

    cookiecutter gh:swxsoc/instrument_pkg_template.git

To use a specific fork or branch, add the fork name and the `--checkout <branch-name>` option:

    cookiecutter gh:swxsoc/instrument_pkg_template.git --checkout <branch-name>

Answer the prompts. If provided a mission name "helios" and instrument 'boo', then cookiecutter will create a new directory called `helios_boo`. 

Go into this directory and run

    git init

This is required by `setuptools_scm` to be able to derive the version number automatically. 
You can then install for the package for development with

    pip install -e .

This template depends on [sunpy](https://sunpy.org) as well as [astropy](https://www.astropy.org) so you'll have to install them as well.

For other dependencies such as developer dependencies see the `pyproject.toml` file.