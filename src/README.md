# Beautiful_Geonode

## Modificaciones

* Nuevo tema de Geonode

* Campo is_tabular en el modelo de Dataset
* Formulario para Dataset con campo is_tabular
* Señal para guardar ResourceBase como subtype = tabular si is_tabular = True

* Override de genode mapstore client si el estado del dataset es de subtipo tabular

* Django app para iconos en el home de geonode

## Hay que hacer migraciones!!