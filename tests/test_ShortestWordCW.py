import pytest
from applications import ShortestWordCW

def test_find_short():
    shortest = ShortestWordCW.find_short("How about no")
    assert shortest == 2