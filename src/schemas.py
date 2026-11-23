from pydantic import BaseModel, Field


class Cliente(BaseModel):
    tenure: int = Field(ge=0, le=100, description="Meses como cliente", examples=[2])
    MonthlyCharges: float = Field(ge=0, le=500, description="Mensalidade", examples=[95.5])
    TotalCharges: float = Field(ge=0, le=50000, description="Total já pago", examples=[191.0])
    SeniorCitizen: int = Field(ge=0, le=1, description="1 = idoso, 0 = não", examples=[1])
    Contract: str = Field(description="Month-to-month, One year ou Two year", examples=["Month-to-month"])
    InternetService: str = Field(description="DSL, Fiber optic ou No", examples=["Fiber optic"])
    PaymentMethod: str = Field(description="Forma de pagamento", examples=["Electronic check"])
    TechSupport: str = Field(description="Yes, No ou No internet service", examples=["No"])


class Resposta(BaseModel):
    classe_predita: str
    probabilidade: float
