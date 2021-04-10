from utils import *
from keras.models import load_model
import time
# import tensorflow as tf
# from tf.keras.models import load_model

# Load model
model = load_model('models/model_THT_1000.h5')

# Doc input

i = 1
while (1):
    # delay 5s
    time.sleep(3)
    print('Query lan thu ', i)

    Input = load_input_from_SQL()

    print('Input:', Input)

    # Reshape
    Input = Input.reshape(1, Input.shape[0], 1)

    # Du doan
    output = model.predict(Input)

    print('Output', output[0])

    # Save

    predict = [1] + list(output[0])
    predict = np.array(predict)

    save_output_to_SQL(predict)

    i = i + 1