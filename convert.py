import re

input_file = "xptv.sgmodule"
output_file = "XPTV.list"

rules = set()

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        # 只保留规则行
        if line.startswith("DOMAIN,"):
            rules.add(line)
        elif line.startswith("DOMAIN-SUFFIX,"):
            rules.add(line)
        elif line.startswith("DOMAIN-KEYWORD,"):
            rules.add(line)
        elif line.startswith("IP-CIDR,"):
            rules.add(line)

# 排序（稳定输出，避免无意义 diff）
rules = sorted(rules)

with open(output_file, "w", encoding="utf-8") as f:
    for r in rules:
        f.write(r + "\n")

print(f"Generated {len(rules)} rules")
