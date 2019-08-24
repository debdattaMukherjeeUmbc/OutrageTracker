import argparse
from user_input import user_option_pick, user_input_add_outrage, user_input_update_outrage_status, \
                        user_input_view_outrage_history, user_input_end_outrage
from outrage_information import OutrageInformation
from outrage_tracker_help import outrage_tracker_help
from validator import OutrageInformationValidator

def main():
    outrage_tracker_help()
    outrage_information = OutrageInformation()
    outrage_validator = OutrageInformationValidator(outrage_information)
    is_active = True

    while is_active:
        user_choice = user_option_pick()
        
        if user_choice==1:

            all_outrage_information = outrage_information.get_all_outrage_information()
            print "{:<40} {:<30} {:<20} {:<20} {:<20}".format('ID', 'Status','Start Time', 'End Time', 'Time Modified')
            for k, outrage in all_outrage_information.iteritems():
                outrage_id, outrage_status, start_time, end_time, date_modified = outrage.outrage_id, outrage.outrage_status, \
                                                                                    outrage.start_time, outrage.end_time, outrage.date_modified
                print "{:<40} {:<30} {:<20} {:<20} {:<20}".format(outrage_id, outrage_status, start_time, end_time, date_modified)

        
        elif user_choice==2:

            start_time, outrage_status = user_input_add_outrage()
            outrage_information.add_outrage_information(start_time, outrage_status)
            print '\nA new outrage has been added successfully.\n'

        elif user_choice==3:

            outrage_id, outrage_status = user_input_update_outrage_status()
            is_valid = outrage_validator.validate_outrage_id(outrage_id)
            if is_valid:
                outrage_information.update_an_outrage_status(outrage_id, outrage_status)
                print '\nThe outrage status has been updated.\n'
            else:
                print '\nEnter valid outrage id.\n'

        elif user_choice==4:

            outrage_id, end_time = user_input_end_outrage()
            is_valid = outrage_validator.validate_outrage_id(outrage_id)
            if is_valid:
                outrage_information.end_an_outrage(outrage_id, end_time)
                print '\nThe outrage status has been ended.\n'
            else:
                print '\nEnter valid outrage id.\n'

        elif user_choice==5:

            outrage_id = user_input_view_outrage_history()
            print '\nFollowing is the outrage history for outrage with id:\n', outrage_id
            is_valid = outrage_validator.validate_outrage_id(outrage_id)
            if is_valid:
                all_history = outrage_information.get_all_outrage_history(outrage_id)
                print "{:<30} {:<20} {:<20} {:<20}".format('Status', 'Start Time', 'End Time', 'Time Modified')
                for outrage in all_history:
                    outrage_status, start_time, end_time, date_modified = outrage.outrage_status, outrage.start_time, \
                                                                          outrage.end_time, outrage.date_modified
                    print "{:<30} {:<20} {:<20} {:<20}".format(outrage_status, start_time, end_time, date_modified)
            else:
                print '\nEnter valid outrage id.\n'

        elif user_choice==6:

            print '\nExiting as requested.\n'
            is_active = False

        else:

            print '\nPlease enter a valid choice.\n'


if __name__ == '__main__':
    main()


