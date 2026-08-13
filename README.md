# tejaspandya

Personal site — quantitative research portfolio.

Single self-contained `index.html`. No build step, no dependencies, no external requests.
Charts are drawn on canvas from measured results in the linked repositories.

Served by GitHub Pages from the default branch root.

## Build

`index.html` is generated — edit `src/index.template.html`, then:

```
python3 build.py
```

That inlines the subset JetBrains Mono woff2 files from `src/` as base64 `@font-face`
data URIs. The page stays a single file with zero external requests.

Font: JetBrains Mono © 2020 The JetBrains Mono Project Authors, SIL OFL 1.1.
Subset to Latin + the symbols used here with `pyftsubset --flavor=woff2`.
