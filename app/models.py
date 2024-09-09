from sqlalchemy import Column, Integer, String, Text, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
import enum
import datetime

Base = declarative_base()

class FaseInnovacionEnum(str, enum.Enum):
    identificacion = "1. Identificación de la necesidad o problema"
    generacion = "2. Generación de ideas"
    seleccion = "3. Selección de ideas"
    desarrollo = "4. Desarrollo del prototipo"
    pruebas = "5. Pruebas y validación"
    implementacion = "6. Implementación"

class PropositoIniciativaEnum(str, enum.Enum):
    analisis = "Análisis de tendencias"
    comprender = "Comprender necesidades de usuarios"
    generacion = "Generación de ideas"
    identificacion = "Identificación de oportunidades de mercado"
    evaluacion = "Evaluación de competencia"
    innovacion = "Innovación tecnológica"
    conocimiento = "Conocimiento del usuario"
    segmentacion = "Segmentación de nichos de mercado"
    disruptiva = "Innovación disruptiva"

class UrgencyEnum(str, enum.Enum):
    muy_bajo = "1 - Muy bajo: No hay presión para implementar la solución rápidamente."
    bajo = "2 - Bajo: La implementación puede esperar un poco más, no es una prioridad inmediata."
    moderado = "3 - Moderado: Existe cierta presión para implementar la solución en un plazo razonable."
    alto = "4 - Alto: Se necesita una implementación relativamente rápida para abordar el problema."
    muy_alto = "5 - Muy Alto: La situación es urgente y se necesita una solución inmediata."

class InnovacionFormulario(Base):
    __tablename__ = 'innovacion_formulario'
    
    id = Column(Integer, primary_key=True, index=True)
    descripcion_iniciativa = Column(Text, nullable=False)
    objetivos_clave = Column(Text, nullable=False)
    fase_innovacion = Column(Text, nullable=False)  # Store as comma-separated string
    proposito_iniciativa = Column(Text, nullable=False)  # Store as comma-separated string

    urgencia = Column(Enum(UrgencyEnum), nullable=False)
    complejidad = Column(Enum(UrgencyEnum), nullable=False)
    incertidumbre = Column(Enum(UrgencyEnum), nullable=False)
    colaboracion = Column(Enum(UrgencyEnum), nullable=False)
    recursos = Column(Enum(UrgencyEnum), nullable=False)
    flexibilidad = Column(Enum(UrgencyEnum), nullable=False)
    velocidad = Column(Enum(UrgencyEnum), nullable=False)
    riesgo = Column(Enum(UrgencyEnum), nullable=False)
    usuario = Column(Enum(UrgencyEnum), nullable=False)

class ResultadosInnovacion(Base):
    __tablename__ = 'resultados_innovacion'
    
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
