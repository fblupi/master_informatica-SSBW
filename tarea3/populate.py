from mongoengine import *
from lxml import etree
import datetime

db = connect('test')
db.drop_database('test')

# Esquema para la BD de pruebas de mongoDB
class addr(EmbeddedDocument):
    building = StringField()
    street   = StringField()
    city     = StringField()
    zipcode  = IntField()
    coord    = GeoPointField()

class likes(EmbeddedDocument):
    grade = StringField(max_length=1)
    score = IntField()
    date  = DateTimeField()

class restaurants(Document):
    name             = StringField(required=True, max_length=80)
    restaurant_id    = IntField()
    cuisine          = StringField()
    address          = EmbeddedDocumentField(addr)
    grades           = ListField(EmbeddedDocumentField(likes))

def downloadAndInsert(bar, city, cuisine):
    api_base_url = 'http://maps.googleapis.com/maps/api/geocode/xml?address='

    req = api_base_url + bar + city
    tree = etree.parse(req)

    addressXML = tree.xpath('//address_component')
    locationXML = tree.xpath('//location')

    buildingXML = addressXML[0].xpath('//long_name/text()')[0]
    streetXML = addressXML[1].xpath('//long_name/text()')[1]
    cityXML = addressXML[2].xpath('//long_name/text()')[2]
    zipcodeXML = int(addressXML[6].xpath('//long_name/text()')[6])
    coordXML = [float(locationXML[0].xpath('//lat/text()')[0]), float(locationXML[0].xpath('//lng/text()')[0])]

    a = addr(building=buildingXML, street=streetXML, city=cityXML, zipcode=zipcodeXML, coord=coordXML)
    r = restaurants(name=bar, cuisine=cuisine, address=a)
    r.save()

# Rellenar BD
downloadAndInsert("Casa Julio", "Granada", "Granaina")
downloadAndInsert("Pizzería Romana", "La Chana", "Italiana")
downloadAndInsert("El Nido del Búho", "Granada", "Tapas")
downloadAndInsert("Pizzametro", "Granada", "Italiana")
downloadAndInsert("La Bodeguica de Miguel del Rei", "Almería", "Tapas")

# Consulta, los tres primeros
print ("\nConsultar los tres primeros:")
for r in restaurants.objects[:3]:
    print (r.id, r.name, r.address.street, r.address.building, r.address.zipcode, r.address.city, r.address.coord)

# Hacer más consultas, probar las de geolocalización
print ("\nConsultar por nombre:")
rr = restaurants.objects(name="Pizzametro")
print (rr[0].name)

print ("\nConsultar por tipo de cocina (no tapas):")
for r in restaurants.objects(cuisine__ne="Tapas"):
    print (r.name)

# print ("\nConsultar por geolocalización:")
# for r in restaurants.objects(address__coord__geo_within_box=[(37.17, -3.61), (37.19, -3.59)]):
#     print (r.name, r.address.coord)
