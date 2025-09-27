import pickle

import numpy as np
from schemas.plantas_schemas import PlanData

with open('RFPlantas.pkl','rb') as file:
    model = pickle.load(file)

labels = ['Arroz','Maize','Garbanzo','Frijoles','Guandul','Frijoles de Polilla',
          'Frijol Mungo','Frijol Negro','Lenteja','Granada','Banano','Mango',
          'Uvas','Sandia','Melon','Manzana','Naranja','Papaya','Coco',
          'Algodon','Yute','Cafe']

def plantas_prediction(data: PlanData):

    xin = np.array([
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]).reshape(1, 7 )


    prediction = model.predict(xin)

    print("prediccion ", prediction)

    return prediction[0]