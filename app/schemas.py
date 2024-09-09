from pydantic import BaseModel
from typing import List, Optional
from app.enums import *

class InnovacionFormularioCreate(BaseModel):
    nombre_proyecto: str
    proposito_iniciativa: Optional[List[PropositoIniciativaEnum]]
    fase_innovacion: Optional[List[FaseInnovacionEnum]]
    urgencia: UrgencyEnum
    complejidad: ComplexityEnum
    incertidumbre: UncertaintyEnum
    colaboracion: CollaborationEnum
    recursos: ResourcesEnum
    flexibilidad: FlexibilityEnum
    velocidad: SpeedEnum
    riesgo: RiskEnum
    usuario: UserEnum
