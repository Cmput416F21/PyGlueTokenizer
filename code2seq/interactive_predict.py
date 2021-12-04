from common import Common
from extractor import Extractor

SHOW_TOP_CONTEXTS = 10
MAX_PATH_LENGTH = 8
MAX_PATH_WIDTH = 2
EXTRACTION_API = 'https://po3g2dx2qa.execute-api.us-east-1.amazonaws.com/production/extractmethods'


class InteractivePredictor:
    exit_keywords = ['exit', 'quit', 'q']

    def __init__(self, config, model):
        model.predict([])
        self.model = model
        self.config = config
        self.path_extractor = Extractor(config, EXTRACTION_API, self.config.MAX_PATH_LENGTH, max_path_width=2)

    @staticmethod
    def read_file(input_filename):
        with open(input_filename, 'r') as file:
            return file.readlines()

    def predict(self):
        input_filename = 'Input.java'

        user_input = ' '.join(self.read_file(input_filename))
        try:
            predict_lines, pc_info_dict = self.path_extractor.extract_paths(user_input)
        except ValueError:
            print("Error: please verify that your .py file has no syntax errors!")
            return
        model_results = self.model.predict(predict_lines)

        prediction_results = Common.parse_results(model_results, pc_info_dict, topk=SHOW_TOP_CONTEXTS)
        for index, method_prediction in prediction_results.items():
            if self.config.BEAM_WIDTH == 0:
                print('Predicted:\t%s' % [step.prediction for step in method_prediction.predictions])
                myfile = open('Predictions.txt', 'w')
                for step in method_prediction.predictions:
                    myfile.write(step.prediction + ' ')
                myfile.close()
            else:
                print('Predicted:')
                for predicted_seq in method_prediction.predictions:
                    print('\t%s' % predicted_seq.prediction)
                myfile = open('Predictions.txt', 'w')
                for step in method_prediction.predictions:
                    myfile.write(step.prediction + ' ')
                myfile.close()
        return method_prediction.predictions
