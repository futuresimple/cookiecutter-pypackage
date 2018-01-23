#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
from tests.conftest import *


@fixture
def sample_fixture():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 1


def test_something(sample_fixture):
    assert 1 == sample_fixture


{%- if cookiecutter.command_line_interface|lower == 'click' %}
def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{%- endif %}
