import argparse
from user_input import user_option_pick, user_input_add_outrage, user_input_update_outrage_status, user_input_view_outrage_history, user_input_end_outrage
from outrage_information import OutrageInformation


parser =argparse.ArgumentParser(prog='Outrage Tracker',
                                usage='''
                                Usage:
                                Keep record of outrages
                                ''',
                                description='''
                                -----------------------------------------------
                                Description:
                                This tool will display outrage information
                                -----------------------------------------------
                                ''',
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                add_help=True
                                )

arg = parser.parse_args()
outrage_information = OutrageInformation()
is_active = True

while is_active:
    user_choice = user_option_pick()
    
    if user_choice==1:
        all_outrage_information = outrage_information.get_all_outrage_information()
        print "{:<40} {:<15} {:<15} {:<15} {:<15}".format('ID', 'Status','Start Time', 'End Time', 'Time Modified')
        # import pdb;pdb.set_trace()
        for k, outrage in all_outrage_information.iteritems():
            outrage_id, outrage_status, start_time, end_time, date_modified = outrage.outrage_id, outrage.outrage_status, outrage.start_time, outrage.end_time, outrage.date_modified
            print "{:<40} {:<15} {:<15} {:<15} {:<15}".format(outrage_id, outrage_status, start_time, end_time, date_modified)

    
    elif user_choice==2:
        start_time, outrage_status = user_input_add_outrage()
        outrage_information.add_outrage_information(start_time, outrage_status)
        print '\nA new outrage has been added successfully.\n'

    elif user_choice==3:
        # import pdb;pdb.set_trace()
        outrage_id, outrage_status = user_input_update_outrage_status()
        outrage_information.update_an_outrage_status(outrage_id, outrage_status)
        print '\nThe outrage status has been updated.\n'

    elif user_choice==4:
        # import pdb;pdb.set_trace()
        outrage_id, end_time = user_input_end_outrage()
        outrage_information.end_an_outrage(outrage_id, end_time)
        print '\nThe outrage status has been ended.\n'

    elif user_choice==5:
        # import pdb;pdb.set_trace()
        outrage_id = user_input_view_outrage_history()
        print '\nFollowing is the outrage history for outrage with id:\n', outrage_id
        all_history = outrage_information.get_all_outrage_history(outrage_id)
        print "{:<15} {:<15} {:<15} {:<15}".format('Status', 'Start Time', 'End Time', 'Time Modified')
        for outrage in all_history:
            outrage_status, start_time, end_time, date_modified = outrage.outrage_status, outrage.start_time, outrage.end_time, outrage.date_modified
            print "{:<15} {:<15} {:<15} {:<15}".format(outrage_status, start_time, end_time, date_modified)

    elif user_choice==6:
        print '\nExiting as requested.\n'
        is_active = False

    else:
        print '\nPlease enter a valid choice.\n'



