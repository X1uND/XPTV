import requests

URL = "https://raw.githubusercontent.com/fangkuia/XPTV/main/X/xptv.sgmodule"

text = requests.get(URL).text

rules = []
in_rule = False

for line in text.splitlines():
    line = line.strip()

    if line == "[Rule]":
        in_rule = True
        continue

    if line.startswith("[") and line != "[Rule]":
        in_rule = False

    if in_rule and line and not line.startswith("#"):
        # Surge rule format: DOMAIN,xxx,PROXY
        parts = line.split(",")

        if len(parts) >= 2:
            rules.append(parts[0].strip() + "," + parts[1].strip())

# 去重
rules = sorted(set(rules))

with open("XPTV.list", "w") as f:
    f.write("\n".join(rules))

print("done:", len(rules))
