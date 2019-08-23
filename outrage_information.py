import uuid 
from outrage_details import OutrageDetails

class OutrageInformation:
    def __init__(self):
        self.latest_outrage_info = {}

    def add_outrage_information(self, start_time, outrage_status, end_time):
        outrage_id = str(uuid.uuid4())
        # outrage_details = OutrageDetails(outrage_id, outrage_status, start_time, end_time)
        # self.latest_outrage_info[outrage_id] = {outrage_details}

        self.latest_outrage_info[outrage_id] = {'start_time': start_time, 'outrage_status': outrage_status, 'end_time': end_time }


    def get_all_outrage_information(self):
        return self.latest_outrage_info

    def update_an_outrage_status(self, outrage_id, new_outrage_status):
        self.latest_outrage_info[outrage_id]['outrage_status'] = new_outrage_status

    def end_an_outrage(self, outrage_id, end_time):
        self.latest_outrage_info[outrage_id][end_time] = end_time




