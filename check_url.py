import urllib.request
try:
    code = urllib.request.urlopen("https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/ToyCar/glTF/ToyCar.gltf").getcode()
    print(code)
except Exception as e:
    print(e)
