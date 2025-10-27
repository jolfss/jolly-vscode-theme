NOTE: The (1: 1 (COLOR)) stands for how the parent was mixed with a different color

## References 
[1] https://code.visualstudio.com/docs/configure/themes
[2] https://code.visualstudio.com/api/references/theme-color
[3] https://code.visualstudio.com/api/extension-guides/color-theme
[4] https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide
[5] https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide#semantic-token-scope-map

# Colors
## Luminosity
- WHITE         #eef2f7
- SNOW          #dadfe6
- FIRN          #bbc4d2
- DARK          #002a5e
## Chromatic
- DUSK          #9a91ae
    - CLAY      #C4C2D3 (1:1 WHITE)
    - GUNMETAL  #676F93 (2:1 DARK)
- INDIGO        #4000f0
    - TARO      #9779F4 (1:1 WHITE)
    - ZAFFER    #1715AF (1:1 DARK)
- MAGENTA       #af00db
    - ORCHID    #CF79E9 (1:1 WHITE)
    - AMETHYST  #750eb1 (2:1 DARK)
- AMARANTH      #cd0030
    - GUM       #DE7994 (1:1 WHITE)
    - ROUGE     #a94d80ff (1:1 ~GUNMETAL)
    - RUBY      #890e3f (2:1 DARK)
- MARIGOLD      #b37a0d
    - WHEAT     #D1B682 (1:1 WHITE)
    - BRASS     #775F28 (2:1 DARK)
- MOSS          #768700
    - LICHEN    #B2BD7C (1:1 WHITE)
    - FERN      #4F681F (2:1 DARK)
- GLACIAL       #079672
    - OXIDIZED  #7BC4B5 (1:1 WHITE)
    - LAGOON    #05726b (2:1 DARK)
- SKY           #0081da
    - DENIM     #77bae9 (1:1 WHITE)
    - POLAR     #00569c (1:1 DARK)

# Tokens
    namespace/module/package -> INDIGO 
    class -> AMARANTH
    enum  -> AMARANTH
    interface -> AMARANTH
    struct -> AMARANTH
    typeParameter -> SKY
    type -> SKY
    parameter -> POLAR
    variable -> DARK
    property -> RUBY
    enumMember -> LAGOON
    decorator -> MAGENTA
    event -> AMARANTH
    function -> MARIGOLD
    method -> RUBY
    macro -> AMETHYST
    label -> AMETHYST
    comment -> DUSK
    string -> FERN
    keyword -> RUBY
    number -> MOSS
    regexp -> MARIGOLD
    operator -> GLACIAL