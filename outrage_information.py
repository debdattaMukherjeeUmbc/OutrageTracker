from datetime import datetime
import uuid 

from outrage_details import OutrageDetails


class OutrageInformation(object):
    """
    This class records outrage information. The latest outrage denotes all outrages that have been reported till now.
    The outrage history stores all information related to updates made on an outrage.
    """
    
    def __init__(self):
        
        self.latest_outrage_info = {}
        self.outrage_history = {}

    def add_outrage_information(self, start_time, outrage_status):
        """
        Adds a new outrage.
        """
        
        end_time = 'CURRENT'
        outrage_id = str(uuid.uuid4())
        current_time = self._get_current_time()
        outrage_details = OutrageDetails(outrage_id, outrage_status, start_time, end_time, current_time)
        self.latest_outrage_info[outrage_id] = outrage_details
        outrage_details_history = OutrageDetails(outrage_id, outrage_status, start_time, end_time, current_time)
        self.outrage_history[outrage_id] = [outrage_details_history]


    def get_all_outrage_information(self):
        """
        Returns all outrages recorded till now.
        """
        
        return self.latest_outrage_info

   
    def get_all_outrage_history(self, outrage_id):
        """
        Returns all history related to the outrage_id supplied.
        """
        
        return self.outrage_history[outrage_id]


    def update_an_outrage_status(self, outrage_id, new_outrage_status):
        """
        Updates the status of an outrage.
        """
        
        self.latest_outrage_info[outrage_id].outrage_status = new_outrage_status
        self.latest_outrage_info[outrage_id].date_modified = self._get_current_time()
        self._create_history(outrage_id)


    def end_an_outrage(self, outrage_id, end_time):
        """
        Ends an outrage by flipping the status to ENDED.
        """
        self.latest_outrage_info[outrage_id].outrage_status = 'ENDED'
        self.latest_outrage_info[outrage_id].end_time = end_time
        self._create_history(outrage_id)

    
    def _create_history(self, outrage_id):
        
        outrage_status = self.latest_outrage_info[outrage_id].outrage_status
        start_time = self.latest_outrage_info[outrage_id].start_time
        end_time = self.latest_outrage_info[outrage_id].end_time
        current_time = self._get_current_time()
        outrage_new_details = OutrageDetails(outrage_id, outrage_status, start_time, end_time, current_time)

        self.outrage_history[outrage_id].append(outrage_new_details)


    def _get_current_time(self):
        
        return datetime.now().strftime('%b %d %Y %I:%M%p')


