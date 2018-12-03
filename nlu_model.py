from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


def run_nlu():
	interpreter = Interpreter.load('./models/current/nlu')
	print(interpreter.parse(u"quero treinar um esporte"))
	print("\n")
	print(interpreter.parse(u"to meio mal"))
	print("\n")
	print(interpreter.parse(u"to com fome"))

if __name__ == '__main__':
	run_nlu()
