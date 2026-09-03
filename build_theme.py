#!/usr/bin/env python3
import json
import json5
import sys
from pathlib import Path

def build_theme(input_file: str, output_file: str, overrides_file: str | None = None):
    print(f"Building theme from {input_file} -> {output_file}")
    template = json5.loads(Path(input_file).read_text())
    variables = template.pop("variables", {})

    if overrides_file:
        overrides = json5.loads(Path(overrides_file).read_text())
        variables.update(overrides.get("variables", {}))
        template.update(overrides.get("theme", {}))

    theme_str = json.dumps(template, indent="\t")
    
    for var_name, var_value in variables.items():
        if isinstance(var_value, dict):
            print(F"Look at you, fancy, {var_name}:{var_value} (we don't support that yet)")
            replacement = var_value.get("color", var_value)
        else:
            replacement = var_value
        theme_str = theme_str.replace(f"${{{var_name}}}", replacement)
    final_theme = json.loads(theme_str)

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(final_theme, indent="\t"))

    print(F"Rendered theme written to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "themes/jolly-light-color-theme.json"
        overrides_file = sys.argv[3] if len(sys.argv) > 3 else None
        build_theme(input_file, output_file, overrides_file)
    else:
        build_theme(
            "themes/jolly-light-template.json5",
            "themes/jolly-light-color-theme.json",
        )
        build_theme(
            "themes/jolly-light-template.json5",
            "themes/jolly-dark-color-theme.json",
            "themes/jolly-dark-palette.json5",
        )
