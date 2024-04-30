import yaml


def fstab_generator(yaml_data):
    fstab_content = ""
    for device, info in yaml_data['fstab'].items():
        if "options" not in info:
            fstab_content += (
                f"{device.ljust(15)}"
                f"{info['mount'].ljust(20)}"
                f"{info['type'].ljust(7)}"
                f"defaults {''.ljust(30)}"
                f"{info.get('dump', '0')}"
                f"{info.get('pass', '1')}\n"
            )
            continue

        padding = len(','.join(info['options']))
        fstab_content += (
            f"{device.ljust(15)}"
            f"{info['mount'].ljust(20)}"
            f"{info['type'].ljust(7)}"
            f"defaults,{','.join(info['options'])}{''.ljust(30-padding if 30-padding >0 else 0)}"
            f"{info.get('dump', '0')}"
            f"{info.get('pass', '1')}\n"
        )
    return fstab_content.strip()


def main():
    with open("fstab.yaml") as fstab_yaml:
        try:
            loaded_yaml = yaml.safe_load(fstab_yaml)
            fstab_format = fstab_generator(loaded_yaml)
        except yaml.YAMLError as exc:
            print(exc)
    with open("/etc/fstab", "a") as to_fstab:
        try:
            to_fstab.write(fstab_format)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
