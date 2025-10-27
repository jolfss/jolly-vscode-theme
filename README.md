# Jolly Light Theme

A vibrant light theme for VSCode inspired by volcanoes, glaciers, and the northern lights.

## Development

This theme uses a build system to manage color variables and make editing easier.

### Setup

Make sure you have [uv](https://docs.astral.sh/uv/) installed:

```bash
brew install uv
```

### Building the Theme

The source theme is in [themes/jolly-light-template.json5](themes/jolly-light-template.json5), which supports:
- **Comments** (using `//` syntax)
- **Color variables** (defined in the `variables` section)

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

### Editing Colors

1. Edit [themes/jolly-light-template.json5](themes/jolly-light-template.json5)
2. Modify colors in the `variables` section at the top
3. Reference variables using `${variableName}` syntax
4. Run `uv run build_theme.py` to generate the final theme
5. Reload VSCode to see changes

### Example

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

MIT
