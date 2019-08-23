
def user_option_pick():
	options = ["View all outrages.", "Add a new outrage.", "Update status of an outrage.", "End outrage.", "Exit program."]
	print("Please choose one of the following:")  
	for idx, element in enumerate(options):
		print("{}) {}".format(idx+1,element))
    
	user_entered_number = input("Enter number: ")
	try:
		if 0 < int(user_entered_number) <= len(options):
			return int(user_entered_number)
	except:
		pass
	return None


def user_input_add_outrage():
	start_time = input('Enter a date in YYYY-MM-DD format:')
	outrage_status = input('Enter the status of the outrage:')
	end_time = input('Enter endtime: ') 
	return (start_time, outrage_status, end_time)

def user_input_update_outrage_status():
	outrage_id = input('Enter the id of the outrage that you want to update:')
	outrage_status = input('Enter the status of the outrage:')
	return (outrage_id, outrage_status)
	
def user_input_end_outrage():
	outrage_id = input('Enter the id of the outrage that you want to end:')
	end_time = input('Enter endtime:') 
	return (outrage_id, end_time)