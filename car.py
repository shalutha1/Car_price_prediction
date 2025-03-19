import string
import pickle
import numpy as np
from flask import Flask, render_template, request,url_for

car = Flask(__name__)

# Load the trained model
#model_filename = "D:/Data Science/ML/sample pro/Regression/car price/car_price_prediction.pickle"
#with open(model_filename, 'rb') as file:
  #  model = pickle.load(file)

# Load the saved scaler
#scaler_filename = "D:/Data Science/ML/sample pro/Regression/car price/StandardScaler_car.pkl"
#with open(scaler_filename, 'rb') as file:
    #scaler = pickle.load(file)

#def prediction(lst):
   # """Transform user input and make prediction."""
   # lst = np.array(lst).reshape(1, -1)  # Convert list to numpy array and reshape
   # scaled_input = scaler.transform(lst)  # Scale the input
   # pred_value = model.predict(scaled_input)  # Make prediction
   # return pred_value[0]

def prediction(lst):
    filename = "D:/Data Science/ML/sample pro/Regression/car price/car_price_prediction.pickle"
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([lst])
        return pred_value

@car.route("/",methods=["Post","Get"])

def index():

    pred_value = 0

    if request.method == 'POST':

        form_data = request.form

        manufacturer = form_data['manufacturer']
        model = form_data['model']
        Prod_year = form_data['prod_year']
        category = form_data['category']
        leather_interior = form_data['leather_interior']
        fuel_type = form_data['fuel_type']
        engine_volume = form_data['engine_volume']
        mileage = form_data['mileage']
        cylinders = form_data['cylinders']
        gear_box_type = form_data['gear_box_type']
        drive_wheels = form_data['drive_wheels']
        doors = form_data['doors']
        wheel = form_data['wheel']
        color = form_data['color']
        airbags = form_data['airbags']


        input_list = []

        input_list.append(int(manufacturer))
        input_list.append(int(model))
        input_list.append(int(Prod_year))
        input_list.append(int(category))
        input_list.append(int(leather_interior))
        input_list.append(int(fuel_type))
        input_list.append(int(engine_volume))
        input_list.append(int(mileage))
        input_list.append(int(cylinders))
        input_list.append(int(gear_box_type))
        input_list.append(int(drive_wheels))
        input_list.append(int(doors))
        input_list.append(int(wheel))
        input_list.append(int(color))
        input_list.append(int(airbags))
        

        pred_value = prediction(input_list)


       
    return render_template("car.html",pred_value= pred_value )

if __name__ =='__main__':
    car.run(debug = True)