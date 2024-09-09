from enum import Enum

class FaseInnovacionEnum(str, Enum):
    identificacion = "1. Identificación de la necesidad o problema"
    generacion = "2. Generación de ideas"
    seleccion = "3. Selección de ideas"
    desarrollo = "4. Desarrollo del prototipo"
    pruebas = "5. Pruebas y validación"
    implementacion = "6. Implementación"

class PropositoIniciativaEnum(str, Enum):
    analisis = "Análisis de tendencias"
    comprender = "Comprender necesidades de usuarios"
    generacion = "Generación de ideas"
    identificacion = "Identificación de oportunidades de mercado"
    evaluacion = "Evaluación de competencia"
    innovacion = "Innovación tecnológica"
    conocimiento = "Conocimiento del usuario"
    segmentacion = "Segmentación de nichos de mercado"
    disruptiva = "Innovación disruptiva"

class UrgencyEnum(str, Enum):
    muy_bajo = "1 - Muy bajo: No hay presión para implementar la solución rápidamente."
    bajo = "2 - Bajo: La implementación puede esperar un poco más, no es una prioridad inmediata."
    moderado = "3 - Moderado: Existe cierta presión para implementar la solución en un plazo razonable."
    alto = "4 - Alto: Se necesita una implementación relativamente rápida para abordar el problema."
    muy_alto = "5 - Muy Alto: La situación es urgente y se necesita una solución inmediata."


class ComplexityEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: El problema es simple y bien definido.'
    bajo = '2 - Bajo: La complejidad en mínima y se entiende claramente.'
    moderado = '3 - Moderado: Hay algunas áreas de complejidad, pero en su mayoría está bien definido.'
    alto = '4 - Alto: El problema es complejo y requiere una comprensión detallada para abordarlo.'
    muy_alto = '5 - Muy Alto: La complejidad es extremadamente alta y el problema es difícil de definir.'
    
class UncertaintyEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: Hay una comprensión completa del problema y las soluciones posibles.'
    bajo = '2 - Bajo: Se tiene una idea general, pero hay cierta incertidumbre sobre las soluciones.'
    moderado = '3 - Moderado: Existen algunas áreas de incertidumbre, pero en su mayoría se tiene una comprensión razonable del problema.'
    alto = '4 - Alto: Hay una cantidad significativa de incertidumbre sobre el problema y las soluciones.'
    muy_alto = '5 - Muy Alto: La incertidumbre es extremadamente alta y no se comprende completamente el problema o las posibles soluciones.'


class CollaborationEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: No se requiere colaboración significativa, el proyecto es manejable por un solo equipo.'
    bajo = '2 - Bajo: Se necesitará alguna colaboración, pero los equipos pueden trabajar de forma independiente en su mayoría.'
    moderado = '3 - Moderado: La colaboración entre equipos es importante, pero no es crítica para el éxito.'
    alto = '4 - Alto: La colaboración es esencial y varios equipos deben trabajar estrechamente juntos.'
    muy_alto = '5 - Muy Alto: La colaboración entre múltiples equipos es absolutamente crucial para el éxito del proyecto.'
    
class ResourcesEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: Recursos muy limitados, es difícil obtener lo que se necesita.'
    bajo = '2 - Bajo: Los recursos son escasos, pero se pueden obtener con esfuerzo.'
    moderado = '3 - Moderado: Los recursos están disponibles, pero con algunas restricciones.'
    alto = '4 - Alto: Hay suficientes recursos disponibles para llevar a cabo el proyecto.'
    muy_alto = '5 - Muy Alto: Recursos abundantes y fácilmente accesibles para apoyar el proyecto.'
    
class FlexibilityEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: Se espera que el alcance del proyecto permanezca relativamente constante.'
    bajo = '2 - Bajo: Puede haber algunos cambios menores, pero el alcance general se mantendrá.'
    moderado = '3 - Moderado: Se esperan algunos cambios significativos, pero el alcance general permanecerá similar.'
    alto = '4 - Alto: Se anticipan cambios importantes en el alcance del proyecto.'
    muy_alto = '5 - Muy Alto: La flexibilidad es fundamental, se esperan cambios drásticos en el alcance del proyecto.'
    
class SpeedEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: La velocidad de implementación no es una prioridad.'
    bajo = '2 - Bajo: Se prefiere una implementación más rápida, pero no es crítica.'
    moderado = '3 - Moderado: La implementación oportuna es importante para el éxito del proyecto.'
    alto = '4 - Alto: Se necesita una implementación rápida para obtener beneficios rápidos.'
    muy_alto = '5 - Muy Alto: La velocidad de implementación es esencial y se espera que sea lo más rápido posible.'
    
class RiskEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: Riesgo mínimo, el fracaso no tendría un gran impacto.'
    bajo = '2 - Bajo: Algunos riesgos, pero manejables y el impacto de un fracaso sería moderado.'
    moderado = '3 - Moderado: Riesgos significativos, un fracaso tendría un impacto considerable.'
    alto = '4 - Alto: Riesgo alto, un fracaso tendría un impacto importante en el proyecto.'
    muy_alto = '5 - Muy Alto: Riesgo extremadamente alto, un fracaso tendría consecuencias catastróficas.'
    
class UserEnum(str, Enum):
    muy_bajo = '1 - Muy bajo: No se tiene información alguna sobre los usuarios.'
    bajo = '2 - Bajo: Hay una comprensión superficial de los usuarios, pero se requiere más investigación.'
    moderado = '3 - Moderado: Se dispone de alguna información sobre los usuarios, pero se necesitan más detalles para comprender completamente sus necesidades.'
    alto = '4 - Alto: Existe una comprensión significativa de los usuarios y sus necesidades, pero aún se pueden requerir ajustes adicionales.'
    muy_alto = '5 - Muy Alto: Se posee un conocimiento profundo y detallado de los usuarios, incluyendo sus necesidades, deseos y comportamientos.'
    