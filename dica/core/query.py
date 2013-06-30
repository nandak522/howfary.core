import argparse
import requests

URL = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins={source}&destinations={destination}&sensor=false'

def main():
    parser = argparse.ArgumentParser(description='Core Library for Distance Calculator')
    parser.add_argument('source', type=str, help='Source Place')
    parser.add_argument('destination', type=str, help='Destination Place')
    args = parser.parse_args()
    url = URL.format(**(args.__dict__))
    response = requests.get(url)
    assert response.status_code == 200, 'Not able to retrieve distance between source and destination'
    response = response.json()
    distance_attributes = response['rows'][0]['elements'][0]
    distance = distance_attributes['distance']['text']
    duration = distance_attributes['duration']['text']
    return (distance, duration)

if __name__ == '__main__':
    print main()
