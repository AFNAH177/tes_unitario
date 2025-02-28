import pytest 

def calcular_impuesto(monto, tasa):
    """
    Calcula el impuesto de un monto dado una tasa.
    """
    if monto < 0 or tasa < 0:
        raise ValueError("El monto y la tasa deben ser valores positivos")
    return monto * (tasa / 100)

def generar_reporte_ingresos(ingresos):
    """
    Genera un resumen financiero con total de ingresos y promedio.
    """
    if not ingresos:
        raise ValueError("La lista de ingresos no puede estar vacía")
    total = sum(ingresos)
    promedio = total / len(ingresos)
    return {"total": total, "promedio": promedio}

# Tests Unitarios

def test_calcular_impuesto():
    assert calcular_impuesto(1000, 10) == 100.0  # 10% de 1000 es 100
    assert calcular_impuesto(500, 5) == 25.0  # 5% de 500 es 25
    
    with pytest.raises(ValueError):
        calcular_impuesto(-100, 10)  # No permite valores negativos
    with pytest.raises(ValueError):
        calcular_impuesto(100, -5)  # No permite tasas negativas

def test_generar_reporte_ingresos():
    datos = [100, 200, 300, 400]
    reporte = generar_reporte_ingresos(datos)
    assert reporte["total"] == 1000
    assert reporte["promedio"] == 250.0
    
    with pytest.raises(ValueError):
        generar_reporte_ingresos([])  # No permite lista vacía
