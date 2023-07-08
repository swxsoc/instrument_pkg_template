========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs| |readthedocs|
    * - build status
      - |testing| |codestyle|

{%- if cookiecutter.github_repo %}
.. |docs| image:: {{cookiecutter.github_repo}}/actions/workflows/docs.yml/badge.svg
    :target: {{cookiecutter.github_repo}}/actions/workflows/docs.yml
    :alt: Documentation Build Status

.. |testing| image:: {{cookiecutter.github_repo}}/actions/workflows/testing.yml/badge.svg
    :target: {{cookiecutter.github_repo }}/actions/workflows/testing.yml
    :alt: Build Status

.. |codestyle| image:: {{cookiecutter.github_repo}}/actions/workflows/codestyle.yml/badge.svg
    :target: {{cookiecutter.github_repo }}/actions/workflows/codestyle.yml
    :alt: Codestyle and linting using flake8
{%- endif %}

{%- if cookiecutter.readthedocs_url %}
.. |readthedocs| image:: {{cookiecutter.readthedocs_url}}/badge/?version=latest
    :target: {{cookiecutter.readthedocs_url}}/en/latest/?badge=latest
    :alt: Documentation Status
{%- endif %}

.. end-badges

A Python package to process and analyze data from {{cookiecutter.__short_string_name}}.

Contributing
------------
We'd love your contributions! Please see our `contribution guide <./CONTRIBUTING.md>`.

Code of Conduct
---------------
When you are interacting with this community you are asked to follow
the `Code of Conduct <./CODE_OF_CONDUCT.md>`_.

Acknowledgements
----------------
The package template used by this package is based on the one developed by the
`OpenAstronomy community <https://openastronomy.org>`_ and the `SunPy Project <https://sunpy.org/>`_.