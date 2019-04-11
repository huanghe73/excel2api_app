# excel2api_app

## run

```shell
conda activate excel2api_app
fabmanager run
```

## JS files

Under directory `/app/static/js`, there are below JS projects:

- swagger-ui

Generally, use `npm run build` to build the JS files from these projects. The built bundle JS files would be referenced from template files.

## dev notes

`utils` js a junction linking to the same directory of project `schemaconverter`.
