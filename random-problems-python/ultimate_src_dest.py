
#Given a list of tuples that make up an itinerary and its connections
#Find the ultimate source and destination
def find_src_dest(airport_list):
    airport_map = {}
    key_loc = None
    for (s, d) in airport_list:
        airport_map[s] = airport_map.get(s,0) + 1
        airport_map[d] = airport_map.get(d,0) + 1
    sd_list = []
    for key in iter(airport_map):
        if (airport_map[key] == 1):
            sd_list.append(key)
    for key in sd_list:
        key_loc = find_key_tuple(key, airport_list)
        if(key_loc == 0):
            print ('Source: ' + key)
        else:
            print ('Destination: ' + key)
    
def find_key_tuple(key, airport_list):
    key_loc = None
    for x,y in airport_list:
        if (x == key):
            key_loc = 0
        elif (y == key):
            key_loc = 1
    return key_loc    

#ap_list = [('SEA','SFO'), ('SFO','EWR')]
ap_list = [('DFW','LHR'), ('ATL','SFO'), ('SFO','CHI'), ('CDG','DFW'),('LHR','ATL'),('CHI','EWR'),('EWR','SEA')]
find_src_dest(ap_list)