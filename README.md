# py-dashboards
---
[![Demo CountPages alpha](https://i.imgur.com/ICsrMgj.gif)](https://i.imgur.com/zqFdv3J.mp4)

[Proof of concept]()

Py Stub repo for creating and exporting native py, parametrized interactive html visuals.

This flask server/REST server, lambda endpoint, creates REST visual resources, which can return interactive dashboard visuals,
with the option HTTP GET parameters as filters.

## Install:
---
specific py and node env are needed

1. `conda create --name pydash python==3.8`
2. `pip install -r requirements.txt`
3. `npm i -g serverless && npm i`

## Example Usage:
---

4. `sls wsgi serve`
5. `sls package`
6. `sls deploy --stage dev`

## Extensibility:
---

The most basic way to extend this repo is to utilize more mature, more built out drawing libraries like (besides **mpl3d**)

- bokeh
- plotly (dash)
- seaborn styles
- ...

## Todo:
---

1. Make the api take parameters that interactively change the visual display.
2. ....


