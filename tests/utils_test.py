
# this is the "test/utils_test.py" file...


from app.utils import to_usd

#def test_answer(): 
#    assert inc(3) == 5

def test_to_usd():
    assert to_usd(123456789.98) == "$123,456,789.98"
