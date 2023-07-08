import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "QeIdK0mOpYBlv1Abb2mW4p9xz6GdfDe0"

while True:
    orig = input("Ingrese ciudad de origen: ")
    if orig == "quit" or orig == "S":
        break

    dest = input("Ingrese ciudad destino: ")
    if dest == "quit" or dest == "S":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")

    print("Direccion desde {} to {}".format(orig, dest))
    print("Duracion del viaje:   " + json_data["route"]["formattedTime"])
    print("Kilometros:           {:.1f}".format(json_data["route"]["distance"] * 1.61))
    print("=============================================")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print("{} ({:.1f} km)".format(each["narrative"], each["distance"] * 1.61))

    print("=============================================\n")
