# config = {
#     # feeder
#     "FEEDER_URL": "http://feeder.untad.ac.id:8100/ws/live2.php",
#     "FEEDER_USERNAME": "001028e1",
#     "FEEDER_PASSWORD": "az18^^",
# }
config = {
    # feeder
    # "FEEDER_URL": "http://103.245.72.114:8100/ws/live2.php",
    "FEEDER_URL": "http://feeder.untad.ac.id:8100/ws/live2.php",
    "FEEDER_USERNAME": "001028p1",
    "FEEDER_PASSWORD": "tikuntad2023&*",
}

def load(param):
    return config[param]

