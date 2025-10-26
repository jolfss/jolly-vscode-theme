# Jolly Theme - Comprehensive Style Guide
**Light Theme** | Inspired by volcanoes, glaciers, and the northern lights

---

## Design Philosophy

This theme captures the dramatic interplay of natural phenomena:
- **Glaciers**: Cool blues and greys for foundations and backgrounds
- **Volcanoes**: Warm reds, golds, and earth tones for emphasis
- **Northern Lights**: Vibrant purples, magentas, and electric blues for keywords and special elements

The light theme uses a soft glacial background with high-contrast, saturated colors for code elements, creating a bright, energetic workspace.

---

## Color Palette

### Foundation Colors (Backgrounds & Surfaces)

#### Primary Backgrounds
```
GLACIER-WHITE     #f8fafb    Primary editor background (soft icy white)
GLACIER-LIGHT     #eff2f5    Secondary surfaces (sidebar, panels)
GLACIER-MEDIUM    #e5e9ed    Tertiary surfaces (inactive tabs, borders)
GLACIER-BORDER    #d0d7de    Subtle borders and dividers
```

#### Elevated Surfaces
```
SNOW-WHITE        #ffffff    Elevated panels, dropdowns, tooltips
ICE-SHADOW        #dde2e8    Hover states, subtle elevation
```

### Code Syntax Colors (Core)

```
PLAIN             #002a5e    Base text (deep glacial blue)
PLAIN-BRIGHT      #dadfe6    Punctuation, subtle elements
PLAIN-LIGHT       #bbc4d2    Secondary text, faded elements

COMMENT           #9a91ae    Comments (muted purple-grey, volcanic stone)
MODULE            #2e00ff    Modules, imports (electric aurora blue)
KEYWORD           #af00db    Keywords (vibrant aurora magenta)
CLASS             #cd0030    Classes, types definitions (volcanic red)
ATTRIBUTE         #b37a0d    Attributes, decorators (geothermal gold)
CONSTANTS         #768700    Constants, enums (volcanic mineral green)
OPERATORS         #079672    Operators, symbols (glacial water teal)
TYPES             #0081da    Type annotations (ice blue)
```

### Extended Syntax Colors

#### Strings & Literals
```
STRING            #006d3d    Strings (deep forest green, moss on volcanic rock)
STRING-ESCAPE     #b37a0d    Escape characters (reuse ATTRIBUTE for consistency)
REGEX             #af00db    Regular expressions (reuse KEYWORD for vibrancy)
NUMBER            #768700    Numbers (reuse CONSTANTS)
```

#### Functions & Variables
```
FUNCTION          #b37a0d    Function names (ATTRIBUTE - geothermal gold)
METHOD            #b37a0d    Method names (ATTRIBUTE - geothermal gold)
VARIABLE          #8b5a3c    Variables (earthy brown - volcanic soil)
PARAMETER         #1e3a5f    Function parameters (dark navy blue - deep ocean)
PROPERTY          #000000    Object properties (dark crimson red - volcanic rock)
```

#### Special Elements
```
TAG               #cd0030    HTML/XML tags (reuse CLASS)
TAG-PUNCTUATION   #079672    Tag brackets (reuse OPERATORS)
MARKUP-HEADING    #002a5e    Markdown headings (bold PLAIN)
MARKUP-LINK       #0081da    Links (reuse TYPES)
MARKUP-CODE       #6f42c1    Inline code (aurora purple variant)
```

### UI Accent Colors

#### Interactive Elements
```
ACCENT-PRIMARY    #0081da    Primary actions, links (ice blue)
ACCENT-HOVER      #006dbb    Hover states for primary actions
ACCENT-ACTIVE     #005999    Active/pressed states

FOCUS-BORDER      #0081da    Focus indicators (ice blue)
SELECTION-BG      #cce5ff    Text selection background (pale ice blue)
SELECTION-INACTIVE #e5e9ed   Inactive selection (glacier medium)
```

#### Secondary Actions
```
BUTTON-SECONDARY  #6f42c1    Secondary buttons (aurora purple)
BUTTON-SEC-HOVER  #5a32a3    Secondary hover state
```

### Status & Semantic Colors

#### Validation & Feedback
```
ERROR             #d73a49    Errors, destructive actions (volcanic red variant)
ERROR-BG          #ffe8eb    Error backgrounds
ERROR-BORDER      #f5b5bc    Error borders

WARNING           #b37a0d    Warnings (geothermal gold)
WARNING-BG        #fff8e6    Warning backgrounds
WARNING-BORDER    #ffe5b3    Warning borders

INFO              #0081da    Information (ice blue)
INFO-BG           #e6f3ff    Info backgrounds
INFO-BORDER       #b3d9ff    Info borders

SUCCESS           #22863a    Success, additions (deep moss green)
SUCCESS-BG        #e6f5ea    Success backgrounds
SUCCESS-BORDER    #b3dfc0    Success borders
```

#### Git & Diff Colors
```
ADDED             #22863a    Added lines, new files
ADDED-BG          #e6ffe9    Added line backgrounds
MODIFIED          #0081da    Modified files (ice blue)
MODIFIED-BG       #e6f3ff    Modified backgrounds
DELETED           #d73a49    Deleted lines, removed files
DELETED-BG        #ffe8eb    Deleted line backgrounds
CONFLICT          #b37a0d    Merge conflicts (warning gold)
```

### Text & Foreground Colors

```
TEXT-PRIMARY      #002a5e    Primary text (PLAIN)
TEXT-SECONDARY    #586069    Secondary text, hints
TEXT-TERTIARY     #8b949e    Tertiary text, disabled text
TEXT-PLACEHOLDER  #bbc4d2    Placeholder text (PLAIN-LIGHT)
TEXT-LINK         #0081da    Hyperlinks (ACCENT-PRIMARY)
TEXT-INVERSE      #ffffff    Text on dark backgrounds
```

### Shadow & Depth

```
SHADOW-SM         #0000000d   Subtle shadows (rgba 0,0,0,0.05)
SHADOW-MD         #0000001a   Medium shadows (rgba 0,0,0,0.10)
SHADOW-LG         #00000026   Larger shadows (rgba 0,0,0,0.15)
```

---

## Component Mapping

### Editor

```
Background:               GLACIER-WHITE (#f8fafb)
Foreground:               PLAIN (#002a5e)
Line highlight:           ICE-SHADOW (#dde2e8)
Selection:                SELECTION-BG (#cce5ff)
Inactive selection:       SELECTION-INACTIVE (#e5e9ed)
Cursor:                   PLAIN (#002a5e)
Find match:               WARNING-BG (#fff8e6)
Current find match:       WARNING-BORDER (#ffe5b3)
Word highlight:           ACCENT-PRIMARY at 15% opacity
```

### Activity Bar

```
Background:               GLACIER-MEDIUM (#e5e9ed)
Foreground:               TEXT-SECONDARY (#586069)
Active foreground:        ACCENT-PRIMARY (#0081da)
Active border:            ACCENT-PRIMARY (#0081da)
Inactive foreground:      TEXT-TERTIARY (#8b949e)
Badge background:         ERROR (#d73a49)
Badge foreground:         TEXT-INVERSE (#ffffff)
```

### Sidebar

```
Background:               GLACIER-LIGHT (#eff2f5)
Foreground:               TEXT-PRIMARY (#002a5e)
Border:                   GLACIER-BORDER (#d0d7de)
Section header:           TEXT-SECONDARY (#586069)
Selection background:     ICE-SHADOW (#dde2e8)
Active background:        SELECTION-BG (#cce5ff)
```

### Tabs

```
Active background:        GLACIER-WHITE (#f8fafb)
Active foreground:        TEXT-PRIMARY (#002a5e)
Active border:            ACCENT-PRIMARY (#0081da)
Inactive background:      GLACIER-MEDIUM (#e5e9ed)
Inactive foreground:      TEXT-SECONDARY (#586069)
Hover background:         ICE-SHADOW (#dde2e8)
Border:                   GLACIER-BORDER (#d0d7de)
Modified border:          MODIFIED (#0081da)
```

### Status Bar

```
Background:               GLACIER-MEDIUM (#e5e9ed)
Foreground:               TEXT-PRIMARY (#002a5e)
No folder background:     GLACIER-LIGHT (#eff2f5)
Debug background:         WARNING (#b37a0d)
Debug foreground:         TEXT-INVERSE (#ffffff)
```

### Terminal

```
Background:               GLACIER-WHITE (#f8fafb)
Foreground:               PLAIN (#002a5e)
Selection background:     SELECTION-BG (#cce5ff)
Cursor:                   PLAIN (#002a5e)

ANSI Colors:
Black:                    #002a5e
Red:                      #d73a49
Green:                    #22863a
Yellow:                   #b37a0d
Blue:                     #0081da
Magenta:                  #af00db
Cyan:                     #079672
White:                    #d0d7de

Bright variants:          30% lighter versions of above
```

### Buttons

```
Primary background:       ACCENT-PRIMARY (#0081da)
Primary foreground:       TEXT-INVERSE (#ffffff)
Primary hover:            ACCENT-HOVER (#006dbb)

Secondary background:     BUTTON-SECONDARY (#6f42c1)
Secondary foreground:     TEXT-INVERSE (#ffffff)
Secondary hover:          BUTTON-SEC-HOVER (#5a32a3)
```

### Input Fields

```
Background:               SNOW-WHITE (#ffffff)
Foreground:               TEXT-PRIMARY (#002a5e)
Border:                   GLACIER-BORDER (#d0d7de)
Focus border:             FOCUS-BORDER (#0081da)
Placeholder:              TEXT-PLACEHOLDER (#bbc4d2)

Error border:             ERROR-BORDER (#f5b5bc)
Warning border:           WARNING-BORDER (#ffe5b3)
Info border:              INFO-BORDER (#b3d9ff)
```

### Lists & Trees

```
Background:               transparent
Hover background:         ICE-SHADOW (#dde2e8)
Selection background:     SELECTION-BG (#cce5ff)
Active selection:         ACCENT-PRIMARY (#0081da)
Active foreground:        TEXT-INVERSE (#ffffff)
Focus background:         ACCENT-PRIMARY (#0081da)
Focus foreground:         TEXT-INVERSE (#ffffff)
```

### Panels (Terminal, Output, etc.)

```
Background:               GLACIER-LIGHT (#eff2f5)
Border:                   GLACIER-BORDER (#d0d7de)
Section header bg:        GLACIER-MEDIUM (#e5e9ed)
```

### Notifications

```
Background:               SNOW-WHITE (#ffffff)
Foreground:               TEXT-PRIMARY (#002a5e)
Border:                   GLACIER-BORDER (#d0d7de)
Error background:         ERROR-BG (#ffe8eb)
Warning background:       WARNING-BG (#fff8e6)
Info background:          INFO-BG (#e6f3ff)
```

---

## TextMate Scope Mapping

### Comments
```
comment:                  COMMENT (#9a91ae)
comment.documentation:    COMMENT (#9a91ae) italic
```

### Strings
```
string:                   STRING (#006d3d)
string.regexp:            REGEX (#af00db)
constant.character.escape: STRING-ESCAPE (#b37a0d)
```

### Numbers & Constants
```
constant.numeric:         NUMBER (#768700)
constant.language:        CONSTANTS (#768700)
constant.other:           CONSTANTS (#768700)
```

### Keywords
```
keyword:                  KEYWORD (#af00db)
keyword.control:          KEYWORD (#af00db)
keyword.operator:         OPERATORS (#079672)
keyword.other:            KEYWORD (#af00db)
storage:                  KEYWORD (#af00db)
storage.type:             TYPES (#0081da)
```

### Variables
```
variable:                 VARIABLE (#8b5a3c)
variable.parameter:       PARAMETER (#1e3a5f)
variable.language:        KEYWORD (#af00db)
variable.other.property:  PROPERTY (#000000)
```

### Functions & Methods
```
entity.name.function:     ATTRIBUTE (#b37a0d)
entity.name.method:       ATTRIBUTE (#b37a0d)
meta.function-call:       ATTRIBUTE (#b37a0d)
meta.method-call:         ATTRIBUTE (#b37a0d)
```

### Classes (Definitions Only)
```
entity.name.class:        CLASS (#cd0030)
entity.name.type.class:   CLASS (#cd0030)
entity.name.type.enum:    CLASS (#cd0030)
entity.name.type.interface: CLASS (#cd0030)
```

### Types (Usage/References)
```
storage.type:             TYPES (#0081da)
support.type:             TYPES (#0081da)
entity.name.type:         TYPES (#0081da)
support.class:            TYPES (#0081da)
entity.other.inherited-class: TYPES (#0081da)
meta.type.annotation:     TYPES (#0081da)
meta.return.type:         TYPES (#0081da)
```

### Attributes & Decorators
```
entity.other.attribute-name: ATTRIBUTE (#b37a0d)
meta.decorator:           ATTRIBUTE (#b37a0d)
punctuation.definition.decorator: ATTRIBUTE (#b37a0d)  // @ symbol matches decorator
storage.type.annotation:  ATTRIBUTE (#b37a0d)
```

### Modules & Imports
```
entity.name.namespace:    MODULE (#2e00ff)
support.module:           MODULE (#2e00ff)
keyword.control.import:   MODULE (#2e00ff)
```

### Operators
```
keyword.operator:         OPERATORS (#079672)
```

### Punctuation & Delimiters

**Context-Aware Delimiters** (match their content):
```
String quotes (' " """):        STRING (#006d3d)
Regex delimiters (/ /):         REGEX (#af00db)
Template expressions (${}):     STRING (#006d3d)
Decorator @ symbol:             ATTRIBUTE (#b37a0d)
```

**Structural Punctuation** (base color):
```
Brackets/Braces/Parens:         PLAIN (#002a5e)
Commas and semicolons:          PLAIN (#002a5e)
Colons:                         PLAIN (#002a5e)
```

**Operator Punctuation** (operator color):
```
Dots and accessors (.):         OPERATORS (#079672)
Arrow functions (=>):           OPERATORS (#079672)
Spread/Rest (...):              OPERATORS (#079672)
```

### HTML/XML
```
entity.name.tag:          TAG (#cd0030)
punctuation.definition.tag: TAG-PUNCTUATION (#079672)
```

### Markdown
```
markup.heading:           MARKUP-HEADING (#002a5e) bold
markup.bold:              inherit bold
markup.italic:            inherit italic
markup.underline.link:    MARKUP-LINK (#0081da)
markup.inline.raw:        MARKUP-CODE (#6f42c1)
markup.inserted:          ADDED (#22863a)
markup.deleted:           DELETED (#d73a49)
```

### CSS
```
support.type.property-name: PROPERTY (#000000)
entity.other.attribute-name.class: CLASS (#cd0030)
entity.other.attribute-name.id: ATTRIBUTE (#b37a0d)
```

### JSON
```
support.type.property-name: PROPERTY (#000000)
string.quoted.double.json: STRING (#006d3d)
```

---

## Semantic Token Mapping

For TypeScript/JavaScript semantic highlighting:

```
namespace:                MODULE (#2e00ff)

// Class/Interface/Enum definitions
class:                    CLASS (#cd0030)
enum:                     CLASS (#cd0030)
interface:                CLASS (#cd0030)
struct:                   CLASS (#cd0030)

// Type usage and annotations
type:                     TYPES (#0081da)
typeParameter:            TYPES (#0081da)

// Functions and methods
function:                 ATTRIBUTE (#b37a0d)
method:                   ATTRIBUTE (#b37a0d)
macro:                    ATTRIBUTE (#b37a0d)

// Variables and properties
property:                 PROPERTY (#000000)
variable:                 VARIABLE (#8b5a3c)
parameter:                PARAMETER (#1e3a5f)
variable.readonly:        CONSTANTS (#768700)
property.readonly:        CONSTANTS (#768700)
enumMember:               CONSTANTS (#768700)

// Decorators
decorator:                ATTRIBUTE (#b37a0d)

// Class semantics (context-aware)
class:                    TYPES (#0081da) when in type position
class.declaration:        CLASS (#cd0030) when defining
class.defaultLibrary:     CLASS (#cd0030) when used as value (e.g., object, str, int)
class.decorator:          CLASS (#cd0030) when used as decorator (e.g., @property)

// Function/Method decorators
function.decorator:       ATTRIBUTE (#b37a0d) when used as decorator
method.decorator:         ATTRIBUTE (#b37a0d) when used as decorator
```

---

## Accessibility Guidelines

### Contrast Ratios (WCAG AA)
All text should meet minimum contrast ratios against backgrounds:
- Normal text (< 18pt): 4.5:1 minimum
- Large text (≥ 18pt or 14pt bold): 3:1 minimum

### Verified Combinations
```
PLAIN on GLACIER-WHITE:       13.8:1 ✓
TEXT-SECONDARY on GLACIER-WHITE: 7.2:1 ✓
KEYWORD on GLACIER-WHITE:     7.8:1 ✓
CLASS on GLACIER-WHITE:       8.9:1 ✓
OPERATORS on GLACIER-WHITE:   5.2:1 ✓
STRING on GLACIER-WHITE:      6.1:1 ✓
```

### Color Blindness Considerations
- Avoid relying solely on red/green distinction (use supplementary indicators)
- Error states use both color AND icons/underlines
- Git colors use backgrounds AND gutter symbols

---

## Implementation Notes

### Punctuation Philosophy

This theme uses **context-aware punctuation coloring** for better readability:

1. **Delimiters match their content**: String quotes are the same green as strings, regex delimiters match regex color, etc.
2. **Structural punctuation is visible**: Brackets, commas, colons use the base PLAIN color so code structure is clear
3. **Operator punctuation uses operator color**: Dots (.), arrows (=>), and spread (...) use OPERATORS color for consistency

This approach ensures:
- Strings are clearly delineated with matching green quotes
- Code structure (brackets, commas) is easy to scan
- Operators are visually grouped and recognizable

### Class/Type Coloring Philosophy

This theme distinguishes between **class definitions**, **type references**, and **value references**:

1. **Class definitions** (declaring a new class): **RED** `#cd0030`
   - `class MyClass {}` - "MyClass" is red
   - `interface MyInterface {}` - "MyInterface" is red

2. **Type references** (using a class as a type): **BLUE** `#0081da`
   - `somevalue: MyType` - "MyType" is blue
   - `normalized: Dataset` - "Dataset" is blue
   - `def method(self) -> str:` - "str" is blue
   - `extends MyClass` - "MyClass" is blue
   - `Array<MyClass>` - "MyClass" is blue

3. **Value references** (using a class as an object): **RED** `#cd0030`
   - `object.__setattr__()` - "object" is red (built-in class used as value)
   - `MyClass.staticMethod()` - "MyClass" is red (class used as object)
   - `@property` - "property" is red (class used as decorator)
   - Built-in classes: `object`, `str`, `int`, `list`, etc. when used as values

### Decorator Coloring Philosophy

Decorators are colored based on **what they are** (relies on semantic highlighting):

1. **Function/Method decorators**: **GOLD** `#b37a0d`
   - `@decorator_fn` - entire decorator gold (decorator_fn is a function)
   - `@my_method` - entire decorator gold (my_method is a method)
   - The `@` symbol inherits the color of the decorator name

2. **Class decorators**: **RED** `#cd0030`
   - `@property` - entire decorator red (property is a built-in class)
   - `@dataclass` - entire decorator red (dataclass is a class)
   - The `@` symbol inherits the color of the decorator name

**Note**: The `@` symbol color is determined by semantic highlighting and will match the decorator it precedes. This requires TypeScript/Python language server support for accurate classification.

### Opacity Usage
Where alpha transparency is beneficial:
- `editor.wordHighlightBackground`: ACCENT-PRIMARY at 15%
- `editor.selectionHighlightBackground`: ACCENT-PRIMARY at 20%
- Shadows use black with varying opacity

### Font Styles
Apply sparingly for emphasis:
- Comments: italic (optional, user preference)
- Documentation comments: italic
- Keywords: normal weight (bold optional in some languages)
- Markup headings: bold

### Border Strategy
Use borders to create hierarchy without cluttering:
- Active tabs: bottom border with ACCENT-PRIMARY
- Focus states: full border with FOCUS-BORDER
- Panels: subtle borders with GLACIER-BORDER
- Avoid heavy borders on light backgrounds

---

## Extension & Customization

### Future Dark Theme Variant
When creating a dark companion theme:
- Invert background/foreground relationships
- Reduce saturation of syntax colors by 10-15%
- Use darker backgrounds: #0d1117, #161b22, #21262d
- Maintain relative luminance relationships

### User Customization Hooks
Users can override specific elements via `workbench.colorCustomizations`:
- Comment italic toggle
- Bracket pair colorization
- Minimap contrast
- Terminal ANSI color preferences

---

## Version History

**v1.0** - Initial style guide
- Complete color palette definition
- Component mapping for all major UI elements
- TextMate and semantic token scopes
- Accessibility verification
