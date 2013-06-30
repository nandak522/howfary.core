from dica.core import query

def test_query():
    distance_attributes = query.compute_howfar(source='Delhi', destination='Bangalore')
    assert len(distance_attributes) == 2
    distance, duration = distance_attributes
    assert isinstance(distance, str)
    assert isinstance(duration, str)
