import argparse
from user_input import user_option_pick, user_input_add_outrage, user_input_update_outrage_status, user_input_end_outrage
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
        print outrage_information.get_all_outrage_information()
    
    elif user_choice==2:
        start_time, outrage_status, end_time = user_input_add_outrage()
        outrage_information.add_outrage_information(start_time, outrage_status, end_time)
        print 'A new outrage has been added successfully.'

    elif user_choice==3:
        outrage_id, outrage_status = user_input_update_outrage_status()
        outrage_information.update_an_outrage_status(outrage_id, outrage_status)
        print 'The outrage status has been updated.'

    
    elif user_choice==5:
        print 'Exiting as requested...'
        is_active = False










# start_time, outrage_status, end_time = user_input()
# # import pdb;pdb.set_trace()
# outrage_information = OutrageInformation()
# outrage_information.add_outrage_information(start_time, outrage_status, end_time)
# outrage_information.print_infor()

# start_time, outrage_status, end_time = user_input()
# outrage_information.add_outrage_information(start_time, outrage_status, end_time)
# outrage_information.print_infor()