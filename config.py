# class for creating config files

import _pickle as pickle

class Config(object):
	def __init__(self, resolution, cap, lang_code):
		self.resolution = resolution
		self.cap = cap
		self.lang_code = lang_code

	def createConfig():
		resolution = input('Desired resolution of the videos you want to download (144p, 360p, 720p, 1080p, etc.): ')
		x = input('Do you want to download captions [Y,N]: ').lower()
		if x == 'y':
			cap = '1'
		else:
			cap = '2'
		lang_code = input('Enter languge code of the captions you wish to download (en for english): ').lower()

		output = open('config.pkl', 'wb')
		config = Config(resolution, cap, lang_code)
		pickle.dump(config, output, -1)
		output.close()