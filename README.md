# A collection of markmeld templates.

This repository contains a bunch of useful templates for use with [markmeld](http://github.com/databio/markmeld) markdown melder. The templates are published to web using GitHub Pages. To view the list of templates, see: [index.json](index.json).

## How to use

Point your `_markmeld.yaml` config to this URL:


```yaml
mm_templates: http://databio.org/mm_templates/
```

Then you can use a template like this:

```yaml
targets:
  letter:
    md_template: generic.jinja
```

## Submitting a new template

You can propose a new template to this repo by PR.
