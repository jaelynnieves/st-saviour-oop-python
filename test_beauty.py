from beauty import Beauty 
from hair import Hair 

def test_beauty():
    beauty = beauty('tarte','clean girl')
    assert beauty.apply("apply") == 'the makeup artist applys tarte makeup to creat the clean girl style'

def test_hair():
    hair = hair('ponytail')
    assert isinstance(hair, style)
def test_makeup():
    makeup = makeup(True, 'blush')

def test_brush():
    brush = brush('fluffy')


def test_spray():
    spray = spray(True, 'hairspray')