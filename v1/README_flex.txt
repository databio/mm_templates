This is a generic template that can be used for any kind of sequential document; just create a varaible called `sections` with the names to include, in order. Like:

```
  target:
    data:
      md_files:
        specific_aims: src/specific_aims.md
        significance_innovation: src/significance_innovation.md
        aim1: src/aim1.md
        aim2: src/aim2.md
      variables:
        sections:
        - specific_aims
        - significance_innovation
        - aim1
        - aim2
```