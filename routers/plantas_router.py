from fastapi import APIRouter

from schemas.plantas_schemas import PlanData
from services.plantas_service import plantas_prediction


router = APIRouter()

@router.post("/predict")
async def plan_predict(data: PlanData):
    print("patient data ", data.N)

    prediction = plantas_prediction(data)


    return{"prediction": prediction}