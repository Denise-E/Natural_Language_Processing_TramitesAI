swagger_data = {
    "swagger": "2.0",
    "info": {
        "version": "1.0.0",
        "title": "Documentación Tramites AI",
        "description": "Detalle de las rutas definidas en el proyecto",
    },
    "host": "localhost:5000",
    "basePath": "",
    "schemes": [
        "http"
    ],
    "paths": {
        "/ping": {
            "get": {
                "tags": ["Ping"],
                "summary": "Ruta ping pong para verificar que está levantada",
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "pong"
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Error response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/evaluar_asunto": {
            "post": {
                "tags": ["Asuntos"],
                "summary": "Predice el tema del asunto recibido",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "textos": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "example": "siniestro a denunciar"
                                    }
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "resultados": {
                                    "type": "object",
                                    "properties": {
                                        "textos": {
                                            "type": "array",
                                            "items": {
                                                "type": "string",
                                                "example": "siniestro a denunciar"
                                            }
                                        },
                                        "predicciones": {
                                            "type": "array",
                                            "items": {
                                                "type": "integer",
                                                "example": 1
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Error response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error al evaluar el asunto"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/poliza_auto": {
            "post": {
                "tags": ["Pólizas de auto"],
                "summary": "Obtiene los datos recibidos para una póliza de auto",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "textos": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "example": "siniestro a denunciar"
                                    }
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "resultados": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "campos": {
                                                "type": "object",
                                                "properties": {
                                                    "anio": {
                                                        "type": "string",
                                                        "example": "2016"
                                                    },
                                                    "cod_postal": {
                                                        "type": "string",
                                                        "example": "1420"
                                                    },
                                                    "marca": {
                                                        "type": "string",
                                                        "example": "peugeot"
                                                    },
                                                    "modelo": {
                                                        "type": "string",
                                                        "example": "2008"
                                                    }
                                                }
                                            },
                                            "texto": {
                                                "type": "string",
                                                "example": "busco información para asegurar un peugeot 2008 del 2016, mi código postal es 1420"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Error response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error al evaluar póliza de auto"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/poliza_hogar": {
            "post": {
                "tags": ["Pólizas del hogar"],
                "summary": "Obtiene los datos recibidos para una póliza de Hogar",
                "responses": {
                    "400": {
                        "description": "Error response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error al evaluar póliza del hogar"
                                }
                            }
                        }
                    },
                    "501": {
                        "description": "Not implemented",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "ruta no implementada"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/denuncia_siniestro": {
            "post": {
                "tags": ["Denuncias de siniestros"],
                "summary": "Obtiene los datos recibidos para la denuncia de un siniestro",
                "responses": {
                    "400": {
                        "description": "Error response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error al evaluar la denuncia de siniestro"
                                }
                            }
                        }
                    },
                    "501": {
                        "description": "Not implemented",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "ruta no implementada"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/carga_presupuesto": {
            "post": {
                "tags": ["Carga de presupuestos"],
                "summary": "Obtiene los datos recibidos para la carga de presupuestos",
                "responses": {
                    "400": {
                        "description": "Error response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error al evaluar el presupuesto"
                                }
                            }
                        }
                    },
                    "501": {
                        "description": "Not implemented",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "ruta no implementada"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
