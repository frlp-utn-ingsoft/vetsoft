client_template="""
{
    "model": "app.client",
    "pk": $id,
    "fields": {
        "name": "Cliente $id",
        "phone": "1123456789",
        "email": "cliente$id@example.com",
        "address" : "calle $id"
    }
}"""
product_template="""
{
    "model": "app.product",
    "pk": $id,
    "fields": {
        "name": "Producto $id",
        "type": "Tipo $id",
        "price": $id.99
    }
}"""

medicine_template="""
{
    "model": "app.medicine",
    "pk": $id,
    "fields": {
        "name": "Medicina $id",
        "description": "Descripción de la medicina $id",
        "dose": $id
    }
}"""

vet_template="""
{
    "model": "app.vet",
    "pk": $id,
    "fields": {
        "name": "Veterinario $id",
        "phone": "111222333",
        "email": "vet$id@example.com"
    }
}"""

provider_template="""
{
    "model": "app.provider",
    "pk": $id,
    "fields": {
        "name": "Proveedor $id",
        "phone": "777888999",
        "email": "prov$id@example.com",
        "address": "Dirección $id"
    }
}"""

pet_template="""
{
    "model": "app.pet",
    "pk": $id,
    "fields": {
        "name": "Mascota $id",
        "breed": "Raza $id",
        "birthday": "2000-01-01"
    }
}"""

templates = [client_template, product_template, medicine_template, vet_template, provider_template, pet_template]
data = []
DATA_COUNT = 10
# genero el data json para cargar datos.
t = "["
for template in templates:
    # datos por plantilla
    data.append(','.join([template.replace("$id", str(i)) for i in range(1,DATA_COUNT + 1)]))
t += ','.join(data)
t += "]"

print(t, file=open("fixtures/data.json", 'w'))

