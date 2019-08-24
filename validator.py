

class OutrageInformationValidator:

	def __init__(self, outrage_info):
		self.outrage_info = outrage_info

	def validate_outrage_id(self, outrage_id):
		return outrage_id in self.outrage_info.get_all_outrage_information()



        

   




