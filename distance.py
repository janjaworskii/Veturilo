



# Pakiet i API do dystansu 
import googlemaps
gmaps = googlemaps.Client(key="AIzaSyDNvRhZKdSYX5O1btoSVn3pcZDdDboKhL4")


#funkcja to liczenia dystansu
def dystans1(poczatek, koniec): 
    result = gmaps.distance_matrix(poczatek, koniec, mode="bicycling")
    #return bool(result['destination_addresses']!="" and result['origin_addresses']!="")
    #return result
    return result['origin_addresses']


a = dystans1("origin","destination")
print(a)



#funkcja to liczenia dystansu
def dystans(poczatek, koniec): 
    result = gmaps.distance_matrix(poczatek, koniec, mode="bicycling")
    if result["rows"][0]["elements"][0]["status"][0] == "O":
        distance = result["rows"][0]["elements"][0]["distance"]["text"]
        return distance
    else:
        return "Brak"
    
    


origin = "aha "
destination = "berlin"  


dystans("berlin", "katowice")


dystans(origin,destination)





