input_file = "xptv.sgmodule"
output_file = "XPTV.list"

rules = set()

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        # 跳过空行和注释
        if not line or line.startswith("#"):
            continue

        # 只处理规则
        if line.startswith(("DOMAIN,", "DOMAIN-SUFFIX,", "DOMAIN-KEYWORD,", "IP-CIDR,")):

            parts = [x.strip() for x in line.split(",")]

            rule_type = parts[0]

            # DOMAIN 系列
            if rule_type in ["DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"]:
                if len(parts) >= 2:
                    rule = f"{rule_type},{parts[1]}"
                    rules.add(rule)

            # IP-CIDR
            elif rule_type == "IP-CIDR":
                if len(parts) >= 2:
                    rule = f"{rule_type},{parts[1]}"
                    rules.add(rule)

# 排序（避免无意义 commit）
rules = sorted(rules)

# 输出
with open(output_file, "w", encoding="utf-8") as f:
    for rule in rules:
        f.write(rule + "\n")

print(f"Generated {len(rules)} rules")
