def convert_to_sf(number, dp):
    return round(number, -abs(len(list(str(number).split(".")[0]))-abs(sf)))
