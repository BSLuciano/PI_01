use mercado;

select prod.nombre, suc.IdSucursal, round(avg(pr.precio),2) as prom
from precio as pr
join sucursal as suc on (pr.IdSucursal = suc.IdSucursal)
join producto as prod on (prod.IdProducto = pr.IdProducto)
where suc.IdSucursal = "9-1-688";