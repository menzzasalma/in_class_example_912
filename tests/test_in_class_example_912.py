#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `in_class_example_912` package."""

import pytest


from in_class_example_912 import in_class_example_912


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_LargeIfFactual(result):
    response = in_class_example_912.LargeIfFactual("any string that contains the word true")
    assert result == "big"
    assert in_class_example_912.x == "big"
    assert in_class_example_912.y == "small"
    assert in_class_example_912.z == "small"