# A collection of markmeld templates

This repository contains a bunch of useful templates for use with [markmeld](http://github.com/databio/markmeld) markdown melder. The templates are published to web using GitHub Pages. To view the list of templates, see: [index.json](index.json).

## How to use

### Remotely

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

### Locally

Clone the repository and then point to it with a local path:

```yaml
mm_templates: local/path/to/mm_templates/
```

Then use in the same way as above.

## Submitting a new template

You can propose a new template to this repo by PR.

## Make your own

It's super easy to make your own template repository for re-use, just use this repository as an example. You can even host it on github pages to share with the world.
