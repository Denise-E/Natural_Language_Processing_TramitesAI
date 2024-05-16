"""
Resultados esperados:  

1 = se vincula a nuestros tramites:

    * Denuncia Siniestro
    * Cotización póliza de auto
    * Cotización póliza del hogar
    * Carga presupuestos

0 = no se vincula a nignuno de ellos.
"""

# 169 datos - 80%
sentences = [
    "denuncia de Siniestro",
    "denuncia de un siniestro",
    "siniestro",
    "denuncia",
    "solicitud Denuncia de Siniestro",
    "solicitud Denuncia siniestro",
    "solicitud siniestro",
    "solicitud denuncia",
    "pedido Denuncia de Siniestro",
    "pedido Denuncia de un siniestro",
    "pedido Denuncia siniestro",
    "pedido siniestro",
    "pedido denuncia",
    "reporte de siniestro",
    "aviso de siniestro",
    "cotización de pólizas de auto",
    "cotización de polizas de auto",
    "cotizacion de polizas de auto",
    "polizas de auto",
    "pólizas de auto",
    "cotización pólizas auto",
    "cotización polizas auto",
    "cotizacion pólizas auto",
    "pólizas auto",
    "solicitud Cotización de pólizas de auto",
    "solicitud Cotización de polizas de auto",
    "solicitud Cotizacion de pólizas de auto",
    "solicitud polizas de auto",
    "solicitud Cotización pólizas auto",
    "solicitud Cotización polizas auto",
    "solicitud Cotizacion pólizas auto",
    "solicitud Cotizacion polizas auto",
    "solicitud polizas auto",
    "solicitud pólizas auto",
    "pedido Cotización de pólizas de auto",
    "pedido Cotización de polizas de auto",
    "pedido Cotizacion de polizas de auto",
    "pedido polizas de auto",
    "pedido Cotización pólizas auto",
    "pedido Cotización polizas auto",
    "pedido Cotizacion pólizas auto",
    "pedido Cotizacion polizas auto",
    "pedido polizas auto",
    "pedido pólizas auto",
    "solicitar cotización de automóvil",
    "cotización de pólizas del hogar",
    "cotizacion de polizas del hogar",
    "polizas del hogar",
    "pólizas del hogar",
    "cotización pólizas hogar",
    "polizas hogar",
    "pólizas hogar",
    "solicitud Cotización de pólizas del hogar",
    "solicitud Cotizacion de polizas del hogar",
    "solicitud polizas del hogar",
    "solicitud pólizas del hogar",
    "solicitud Cotización polizas hogar",
    "solicitud polizas hogar",
    "solicitud pólizas hogar",
    "pedido Cotización de pólizas del hogar",
    "pedido Cotizacion de polizas del hogar",
    "pedido polizas del hogar",
    "pedido pólizas del hogar",
    "pedido Cotización pólizas hogar",
    "pedido Cotización polizas hogar",
    "pedido polizas hogar",
    "pedido pólizas hogar",
    "pedido Cotización de polizas del hogar",
    "pedido Cotizacion de pólizas del hogar",
    "pedido Cotizacion pólizas hogar",
    "pedido Cotizacion polizas hogar",
    "solicitud Cotización de polizas del hogar",
    "solicitud Cotizacion pólizas hogar",
    "solicitud Cotizacion polizas hogar",
    "cotización de pólizas de la casa",
    "cotizacion de polizas de la casa",
    "cotizacion de polizas casa",
    "cotización de pólizas vivienda",
    "cotizacion de polizas vivienda",
    "cotizacion de polizas depto",
    "cotización de pólizas departamento",
    "cotizacion de polizas departamento",
    "cotización de polizas veiculo",
    "cotizacion de pólizas veiculo",
    "cotisasión de pólizas veiculo",
    "cotisasión de polizas veiculo",
    "cotisasion de pólizas veiculo",
    "cotisasion de polizas veiculo",
    "cotisasión de pólizas de auto",
    "cotisasión de polizas de auto",
    "cotisasion de pólizas de auto",
    "cotisasion de polizas de auto",
    "cotización de polizas vehiculo",
    "cotizacion de pólizas vehiculo",
    "cotizacion de polizas vehiculo",
    "cotisasión de pólizas vehiculo",
    "cotisasion de pólizas vehiculo",
    "cotisasion de polizas vehiculo",
    "pólisas de auto",
    "cotización de polizas del hogar",
    "cotizacion de pólizas del hogar",
    "cotizacion pólizas hogar",
    "solicitud de presupuesto para hogar",
    "pedir presupuesto de póliza de hogar",
    "presupuestos Solicitados",
    "presupuestos",
    "solicitud Presupuestos Solicitados",
    "solicitud presupuestos",
    "pedido Carga de presupuestos",
    "pedido presupuestos a cargar",
    "pedido auto Por favor cotizar",
    "pedido hogar Por favor cotizar",
    "solicitud Carga de presupuestos",
    "solicitud presupuestos a cargar",
    "necesito presupuesto",
    "presupuestos a cargar",
    "pedido Vacaciones en Mardel",
    "solicitud Promoción en ropa",
    "promoción en ropa",
    "recordatorio de pago de factura pendiente",
    "confirmación de reserva de hotel",
    "información sobre cambios en el horario de atención al cliente",
    "resumen mensual de cuenta bancaria",
    "actualización sobre el estado de tu solicitud",
    "confirmación de reserva de vuelo",
    "informe de rendimiento trimestral",
    "recordatorio de reunión de equipo",
    "confirmación de compra en línea",
    "notificación de cambio de contraseña de cuenta",
    "recordatorio de renovación de membresía",
    "invitación a seminario web sobre desarrollo profesional",
    "conocé Datadog",
    "conoce nuestros beneficios",
    "nuevo mensaje",
    "descubre todas las novedades",
    "últimos días",
    "nuevo lanzamiento",
    "nuevos lanzamientos",
    "¡gana un millón de dólares ahora!",
    "oferta especial: ¡Descuento del 50 porciento de descuento solo por hoy!",
    "aumenta tu puntaje de crédito al instante",
    "¡compra seguidores y likes para tus redes sociales!",
    "conoce a solteros locales cerca de ti",
    "reunión de equipo esta tarde a las 3 p.m.",
    "confirmación de reserva para la conferencia",
    "actualización semanal del proyecto",
    "recuerda enviar el informe antes del viernes",
    "invitación a la presentación del nuevo producto",
    "¡gana un iPhone gratis!",
    "¡oferta exclusiva: descuento del 70% en productos electrónicos!",
    "aumenta tus seguidores en redes sociales al instante",
    "¡deshazte de la deuda en 24 horas!",
    "¡sorteo de vacaciones todo incluido!",
    "¡conoce solteros calientes en tu área!",
    "¡baja de peso rápidamente con esta pastilla milagrosa!",
    "¡dinero fácil y rápido: hazte rico en una semana!",
    "¡prueba gratis nuestro producto y gana una tarjeta de regalo!",
    "¡increíble oportunidad de inversión con altos rendimientos!",
    "¡descubre el secreto para una piel perfecta!",
    "¡aprovecha esta oferta única: préstamos sin intereses!",
    "¡gana un viaje de lujo a las Bahamas!",
    "¡incrementa tus ingresos con este sistema probado!",
    "¡obtén un préstamo sin verificación de crédito!",
    "¡haz crecer tu negocio con nuestro software revolucionario!",
    "¡oferta limitada: suscríbete ahora y recibe un descuento adicional!",
    "¡descubre cómo ganar dinero desde casa!",
    "¡productos de belleza gratis solo por registrarte!",
    "¡tu cuenta ha sido seleccionada para recibir un premio especial!",
    "solicitud Vacaciones"
]

training_labels = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0]

# 42 datos - 20%
testing_sentences = [
    "denuncia siniestro",
    "solicitud Denuncia de un siniestro",
    "notificación siniestro",
    "informe de siniestro",
    "cotizacion de pólizas de auto",
    "cotizacion polizas auto",
    "polizas auto",
    "solicitud Cotizacion de polizas de auto",
    "solicitud pólizas de auto",
    "pedido Cotizacion de pólizas de auto",
    "pedido pólizas de auto",
    "cotización polizas hogar",
    "solicitud Cotización pólizas hogar",
    "solicitud Cotizacion de pólizas del hogar",
    "cotización de pólizas casa",
    "cotización de pólizas depto",
    "cotizacion de polizas veiculo",
    "cotización de pólizas vehiculo",
    "cotisasión de polizas veiculo",
    "polisas de auto",
    "cotizacion polizas hogar",
    "cotización de seguro de vivienda",
    "pedido Presupuestos Solicitados",
    "pedido presupuestos",
    "carga de presupuestos",
    "pedido Promoción en ropa",
    "solicitud Vacaciones en Mardel",
    "vacaciones en Mardel",
    "actualización de política de privacidad",
    "recordatorio de cita médica",
    "confirmación de registro en el evento",
    "notificación de entrega de paquete",
    "invitación a evento de networking empresarial",
    "recordatorio de fecha de vencimiento de suscripción",
    "invitación a participar en encuesta de satisfacción",
    "resumen de actividad en la cuenta de redes sociales",
    "vacaciones!",
    "descuentos solo para vos",
    "conoce Datadog",
    "feliz cumpleaños",
    "conocé nuestras ofertas",
    "solicitud Vacaciones Mar de las Pampas"
]

testing_labels = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]