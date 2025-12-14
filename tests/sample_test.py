import pytest

import imgtoolkit.main

def test_sample():
    assert imgtoolkit.main.sample_function() == 'test_example'