# jolly-light

A vibrant light theme for VSCode inspired by volcanoes, glaciers, and the northern lights.

![](JOLLY-LIGHT.png)

## Building the Theme

This theme uses a simple build system to manage color variables in a template.

The source theme is in [themes/jolly-light-template.json5](themes/jolly-light-template.json5), which supports:
- Color variables (defined in the `variables` section, referenced later using `${variableName}` syntax in the main body)
- Comments are elided (using `//` syntax for json5)

To build the final theme:

```bash
uv run build_theme.py
```

This generates [themes/jolly-light-color-theme.json](themes/jolly-light-color-theme.json) from the template.

### Watch Mode

To automatically rebuild when you edit the template:

```bash
npm run watch
```

### Color Preprocess Example

```json5
{
  "variables": {
    "primaryBlue": "#0081da",
    "navyBlue": "#002a5e"
  },
  "colors": {
    "editor.background": "${backgroundWhite}",
    "editor.foreground": "${navyBlue}"
  }
}
```

## Files

- [themes/jolly-light-template.json5](themes/jolly-light-template.json5) - **Edit this file** (source with variables)
- [themes/jolly-light-color-theme.json](themes/jolly-light-color-theme.json) - Generated theme (do not edit)
- [build_theme.py](build_theme.py) - Build script
- [pyproject.toml](pyproject.toml) - Python dependencies (json5)


## License

Creative Commons - enjoy :)