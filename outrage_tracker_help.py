import argparse

def outrage_tracker_help():
    parser =argparse.ArgumentParser(prog='Outrage Tracker',
                                    usage='''
                                    Usage:
                                    ------------------------------------------------------------
                                    1. To view all outrages recorded till now, enter 1.
                                    2. To enter a new outrage, enter 2 and type the
                                        status and start time. The end time would be CURRENT
                                        as it is an active outrage.
                                    3. To update an outrage status, enter 3 and type in
                                       the status you want to update along with the 
                                       id of the outrage you are trying to update.
                                    4. To end an outrage, enter 4 and type in the end time
                                       and id of the outrage, the status of the outrage 
                                       would be automatically set to ENDED.
                                    5. To view history of a particular outrage, press 5 at 
                                       any point and enter the valid outrage id you would
                                       like to view the history of.
                                    6. If you want to exit the application at any point,
                                       press 6.

                                    Examples of input:
                                    Start time : Jun 1 2005 1:33PM
                                    Status: Active and being monitored
                                    ------------------------------------------------------------
                                    ''',
                                    description='''
                                    -----------------------------------------------
                                    Description:
                                    This tool will display outrage information.

                                    -----------------------------------------------
                                    ''',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    add_help=True
                                    )

    arg = parser.parse_args()
