from dica.core.query import compute_howfar

def test_query():
    distance_attributes = compute_howfar(source='Delhi', destination='Bangalore')
    assert len(distance_attributes) == 2
    distance, duration = distance_attributes
    assert isinstance(distance, unicode)
    assert isinstance(duration, unicode)
