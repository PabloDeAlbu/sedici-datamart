# Data Warehouse

## Installation

### Extractor de ejemplo

Crear imagen para extractor de ejemplo

```bash
make -C app/extract/.base/ -s build
```


Ejecutar container con extractor de ejemplo

```bash
make -C app/extract/.base/ -s up
```


### Agregar un extractor para una fuente **foo**

Crear directorio para el extractor **foo**

```bash
cp -R app/extract/.base app/extract/foo
sed -i "s/REPLACE_NAME/foo/" app/extract/foo/Makefile
sed -i "s/REPLACE_WORKDIR/foo/" app/extract/foo/Makefile
```

Agregar dependencias en app/extract/foo/requirements.txt

```bash
echo -e dependency\ >> app/extract/foo/requirements.txt 
```

Creo imagen para extractor **foo**

```bash
make -C app/extract/foo/ -s build
```

Ejecutar container con extractor **foo**

```bash
make -C app/extract/foo/ -s up
```