from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Tramites AI"
    }
)

swagger_data = {
    "swagger": "2.0",
    "info": {
        "version": "1.0.0",
        "title": "Documentación Tramites AI",
        "description": "Detalle de las rutas definidas en el proyecto para BDT Global",
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
                "summary": "Ruta ping pong para verificar que está levantada la API",
                "responses": {
                    "200": {
                        "description": "Petición procesada exitosamente",
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
                        "description": "Petición incorrecta",
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
                        "description": "Petición procesada exitosamente",
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
                        "description": "Petición incorrecta",
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
                                        "example": "busco información para asegurar un peugeot 2008 del 2016, mi código postal es 1420"
                                    }
                                }
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Petición procesada exitosamente",
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
                        "description": "Petición incorrecta",
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
                        "description": "Petición incorrecta",
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
                        "description": "Ruta no implementada",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Ruta no implementada"
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
                        "description": "Petición incorrecta",
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
                        "description": "Ruta no implementada",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Ruta no implementada"
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
                        "description": "Petición incorrecta",
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
                        "description": "Ruta no implementada",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Ruta no implementada"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/entrenar/poliza_auto": {
            "get": {
                "tags": ["Pólizas de auto"],
                "summary": "Entrena el modelo para pólizas de auto",
                "responses": {
                   "200": {
                        "description": "Petición procesada exitosamente",
                        "examples": {
                            "application/json": [
                                { "msg": True },
                                { "msg": False }
                            ]
                        },
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "boolean",
                                    "example": True
                                }
                            }
                        }
                    },
                    "200":   {
                            "description": "Entrenamiento exitoso",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "msg": {
                                        "type": "boolean",
                                        "example": True
                                    }
                                }
                            }
                        },
                    "400": {
                        "description": "Petición incorrecta",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error al entrenar el modelo de pólizas de auto"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/entrenar/evaluar_asunto": {
            "post": {
                "tags": ["Asuntos"],
                "summary": "Entrena el modelo para asuntos",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": False,
                        "description": "Todos los campos son opcionales. Puede enviarse un JSON vacío. Los valores mostrados son los definidos por defecto en el código.",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "max_tokens": {
                                    "type": "integer",
                                    "example": 10000,
                                    "description": "Tamaño del vocabulario (por defecto: 10000)"
                                },
                                "dim_vector": {
                                    "type": "integer",
                                    "example": 16,
                                    "description": "Tamaño del vector (por defecto: 16)"
                                },
                                "long_sentencias": {
                                    "type": "integer",
                                    "example": 10000,
                                    "description": "Longitud máxima de las secuencias de entrada (por defecto: 10000)"
                                },
                                "iteraciones": {
                                    "type": "integer",
                                    "example": 4000,
                                    "description": "Cantidad de iteraciones para el entrenamiento (por defecto: 4000)"
                                }
                            },
                            "additionalProperties": False
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Entrenamiento exitoso",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "boolean",
                                    "example": True
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Petición incorrecta",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "msg": {
                                    "type": "string",
                                    "example": "Error al entrenar modelo asuntos"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
