from mongoengine import *
import datetime

db = connect('test')
db.drop_database('test')

# Esquema para la BD de pruebas de mongoDB
class addr(EmbeddedDocument):
    building = StringField()
    street   = StringField()
    city     = StringField()   # añadido
    zipcode  = IntField()
    coord    = GeoPointField() # OJO, al BD de test estan a revés
                               # [long, lat] en vez de [lat, long]

class likes(EmbeddedDocument):
    grade = StringField(max_length=1)
    score = IntField()
    date  = DateTimeField()

class restaurants(Document):
    name             = StringField(required=True, max_length=80)
    restaurant_id    = IntField()
    cuisine          = StringField()
    borough          = StringField()
    address          = EmbeddedDocumentField(addr)              # en la misma collección
    grades           = ListField(EmbeddedDocumentField(likes))

# Rellenar BD
a1 = addr(building="5", street="Hermosa", city="Granada", zipcode=18010, coord=[37.1766872, -3.5965171])
r1 = restaurants(name="Casa Julio", cuisine="Granaina", borough="Centro", address=a1)
r1.save()

a2 = addr(building="10", street="Periodista Eugenio Selles", city="Granada", zipcode=18014, coord=[37.1964443, -3.6235739])
r2 = restaurants(name="La Posada", cuisine="Tapas", borough="Cerrillo de Maracena", address=a2)
r2.save()

a3 = addr(building="83", street="Concha Piquer", city="Granada", zipcode=18015, coord=[37.19007, -3.630659])
r3 = restaurants(name="Pizzería Romana", cuisine="Italiana", borough="La Chana", address=a3)
r3.save()

a4 = addr(building="10", street="Dr. Pareja Yébenes", city="Granada", zipcode=18012, coord=[37.1899028, -3.609669])
r4 = restaurants(name="El Nido del Búho", cuisine="Tapas", borough="Plaza de Toros", address=a4)
r4.save()

a5 = addr(street="Panamá", city="Peligros", zipcode=18210, coord=[37.2304073, -3.6272395])
r5 = restaurants(name="El Rey de Tapas", cuisine="Tapas", borough="Peligros", address=a5)
r5.save()

a6 = addr(building="21", street="Gran Capitán", city="Granada", zipcode=18002, coord=[37.1778754, -3.6046391])
r6 = restaurants(name="Pizzametro", cuisine="Italiana", borough="Centro", address=a6)
r6.save()

a7 = addr(building="7", street="La Piralica", city="Almería", zipcode=4009, coord=[36.8515198, -2.4509926])
r7 = restaurants(name="La Bodeguica de Miguel del Rei", cuisine="Tapas", borough="San Luís", address=a7)
r7.save()

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
