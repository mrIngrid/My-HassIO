#!/usr/bin/env python

import os
import errno

def path_hierarchy(path):
    hierarchy = {
        'type': 'folder',
        'name': os.path.basename(path),
        'path': path,
    }

    try:
        hierarchy = [
            path_hierarchy(os.path.join(path, contents))
            for contents in os.listdir(path)
        ]
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        hierarchy['type'] = 'file'

    return hierarchy

if __name__ == '__main__':
    import json
    import sys

    try:
        directory = sys.argv[1]
    except IndexError:
        directory = "."

    ##############################################################
    #METTI QUI IL TUO ACCESS TOKEN A LUNGA VITA E IL TUO DOMINIO DI Home Assistant
    Access_Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlYmVmZWNlMjBlZjY0NTRjODQ3YWE0NDliZDZlY2MwMiIsImlhdCI6MTU4NDY0MzQ5NSwiZXhwIjoxOTAwMDAzNDk1fQ.vsIkyykJi_XK2cFMOjN93yHBVgYZSjeLfinvc4DrFkw"
    ip_ha = "ajdinihome.duckdns.org:8123"
    entity_slider = "input_select.music"
    ##############################################################

    var = 'curl -X POST -H "Authorization: Bearer ' + Access_Token + '" -H "Content-Type: application/json" -d '
    var = var +  "'" + '{"entity_id": "' + entity_slider +'","options": ['
    data = path_hierarchy(directory)
    d = 0
    for i in data:
        if d == 0:
           var = var + '"' + i['name'] + '"'
        else:
           var = var + ',"' + i['name']  + '"'
        d = d + 1
    var = var + "]}' https://" + ip_ha + "/api/services/input_select/set_options"
    print(var)
    print(os.system(var))