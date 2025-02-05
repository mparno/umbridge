import requests
import json

host = 'http://model:4242'

def test_Evaluate_default():
    url = f'{host}/Evaluate'

    payload = {'input': [[1,0,0,0]], 'config': {}}

    resp = requests.post(url, headers={}, data=json.dumps(payload,indent=4))
    print(resp.text)

    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['output'] == [[0.0671325634212171, 0.06713256342121707, 0.06713256342121707, 0.06713256342121704, 0.06713256342121704, 0.20832077985852093, 0.20832077985852088, 0.20832077985852096, 0.20832077985852082, 0.20832077985852082, 0.37308450540600907, 0.3730845054060091, 0.3730845054060091, 0.37308450540600907, 0.373084505406009, 0.5880037531004143, 0.5880037531004146, 0.5880037531004147, 0.5880037531004146, 0.5880037531004146, 0.8525808066508843, 0.8525808066508848, 0.8525808066508845, 0.8525808066508849, 0.8525808066508849], [0.012267346132887097]]

def test_Evaluate_lvl22():
    url = f'{host}/Evaluate'

    payload = {'input': [[1,0,0,0]], 'config': {'level': [2,2]}}

    resp = requests.post(url, headers={}, data=json.dumps(payload,indent=4))
    print(resp.text)

    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['output'] == [[0.06433223441704557, 0.06433223441704503, 0.06433223441704528, 0.06433223441704453, 0.06433223441704336, 0.20310060220674966, 0.20310060220674947, 0.20310060220674875, 0.20310060220674464, 0.20310060220673815, 0.37271533300822834, 0.3727153330082249, 0.3727153330082237, 0.3727153330082161, 0.37271533300820503, 0.5902115057250344, 0.5902115057250288, 0.590211505725026, 0.5902115057250128, 0.5902115057249947, 0.8562128072010176, 0.8562128072010163, 0.8562128072010167, 0.8562128072010126, 0.8562128072010003], [0.014807918127841541]]

def test_GetInputSizes():
    url = f'{host}/GetInputSizes'

    resp = requests.get(url)
    print(resp.text)

    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['inputSizes'] == [4]

def test_GetOutputSizes():
    url = f'{host}/GetOutputSizes'

    resp = requests.get(url)
    print(resp.text)

    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['outputSizes'] == [25,1]
