response=request.get(url)

data=response.json()

# {
#   "ip":"2600:1700:7ba0:3770:ed05:792f:f2b8:493b",
#   "type":"ipv6",
#   "continent_code":"NA",
#   "continent_name":"North America",
#   "country_code":"US",
#   "country_name":"United States",
#   "region_code":"TX",
#   "region_name":"Texas",
#   "city":"Midland",
#   "zip":"79707",
#   "latitude":32.024269104003906,
#   "longitude":-102.15827941894531,
#   "location":{
#     "geoname_id":5526337,
#     "capital":"Washington D.C.",
#     "languages":[
#       {
#         "code":"en",
#         "name":"English",
#         "native":"English"
#       }
#     ],
#     "country_flag":"http:\/\/assets.ipstack.com\/flags\/us.svg",
#     "country_flag_emoji":"\ud83c\uddfa\ud83c\uddf8",
#     "country_flag_emoji_unicode":"U+1F1FA U+1F1F8",
#     "calling_code":"1",
#     "is_eu":false
#   }
# }

coord=(data['latitude'], data['longitude'])
data['"latitude"']