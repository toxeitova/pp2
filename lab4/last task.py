import json

with open("data.json") as f:
    data = json.load(f)
    
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU'}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu}")
