import yaml

with open("fs.yaml") as inyaml:
    try:
        yo = yaml.safe_load(inyaml)
    except yaml.YAMLError as exc:
        print(exc)

a = yo["fstab"]
for k,v in a.items():
  with open("/etc/fstab", "a") as file:
    if "options" not in v:
        file.write("{} {} {} defaults 0 1\n".format(k,v['mount'],v['type']))
        continue
    file.write("{} {} {} {} 0 1\n".format(k,v['mount'],v['type'],",".join(v['options'])))
