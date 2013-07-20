from howfary.core.query import compute_howfar

def test_query():
    distance_attributes = compute_howfar(source='Delhi', destination='Bangalore')
    assert isinstance(distance_attributes, dict)
    assert len(distance_attributes) == 3
    assert distance_attributes['status'] == 'OK'

    assert distance_attributes['distance']
    assert distance_attributes['distance']['text']
    distance_in_text = distance_attributes['distance']['text']
    assert isinstance(distance_in_text, unicode)
    assert distance_attributes['distance']['value']
    distance_in_value = distance_attributes['distance']['value']
    assert isinstance(distance_in_value, int)

    assert distance_attributes['duration']
    assert distance_attributes['duration']['text']
    duration_in_text = distance_attributes['duration']['text']
    assert isinstance(duration_in_text, unicode)
    assert distance_attributes['duration']['value']
    duration_in_value = distance_attributes['duration']['value']
    assert isinstance(duration_in_value, int)
