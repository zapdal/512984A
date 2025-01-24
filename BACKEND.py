import tensorflow as tf
import numpy as numpy
from keras.utils import img_to_array,load_img,get_file
import numpy as np

class IMG_PRED:

    def __init__(self) -> None:
        self.IMG_HEIGHT = 180
        self.IMG_WIDTH = 180
        self.MODEL_PATH = './model.tflite'
        self.LABELS = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
        self.MODEL = tf.lite.Interpreter(
            model_path=self.MODEL_PATH
        )
        self.CLASSIFIER = self.MODEL.get_signature_runner('serving_default')

    def predict(self,url:str)->str:

        test_file=get_file(
            origin=url
        )

        img=load_img(
            test_file,
            target_size=(
                self.IMG_HEIGHT,
                self.IMG_WIDTH
            )
        )

        img_array=img_to_array(
            img=img
        )

        img_array=tf.expand_dims(
            input=img_array,
            axis=0
        )

        predictions = self.CLASSIFIER(resnet50_input=img_array)['dense_5']

        score = tf.nn.softmax(predictions[0])

        result="This image most likely belongs to {} with a {:.2f} percent confidence.".format(self.LABELS[np.argmax(score)], 100 * np.max(score))

        return result


