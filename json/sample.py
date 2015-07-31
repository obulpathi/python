import jsonschema

schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : 1},
     },
}

jsonschema.validate({u'name' : "Eggs", "price" : 34.99}, schema)
