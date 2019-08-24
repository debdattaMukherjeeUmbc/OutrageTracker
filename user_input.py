from datetime import datetime

def user_option_pick():
	
	options = ["View all outrages.", "Add a new outrage.", "Update status of an outrage.", "End outrage.", "View history of an outrage.", "Exit program."]
	print("Please choose one of the following:")  
	for idx, element in enumerate(options):
		print("{}) {}".format(idx+1,element))

	try:
		user_entered_number = input("Enter number: ")
		if 0 < int(user_entered_number) <= len(options):
			return int(user_entered_number)
	except:
		pass
	return None


def user_input_add_outrage():
	start_time = _user_date_input()
	isValid=False
	while not isValid:
		try:
			outrage_status = input('Enter the status of the outrage:')
			isValid=True
		except:
			print "Try again!\n"

	return (start_time, outrage_status)

def user_input_update_outrage_status():

	isValid=False
	while not isValid:
		try:
			outrage_id = input('Enter the id of the outrage that you want to update:')
			outrage_status = input('Enter the status of the outrage:')
			isValid=True
		except:
			print "Try again!\n"
	return (outrage_id, outrage_status)
	

def user_input_view_outrage_history():
	
	isValid=False
	while not isValid:
		try:
			outrage_id = input('Enter the id of the outrage that you want to view history:')
			isValid=True
		except:
			print "Try again!\n"
	return outrage_id


def user_input_end_outrage():
	
	isValid=False
	while not isValid:
		try:
			outrage_id = input('Enter the id of the outrage that you want to end:')
			isValid=True
		except:
			print "Try again!\n"
	end_time = _user_date_input()
	return (outrage_id, end_time)

def _user_date_input():
	
	isValid=False
	while not isValid:
		try:
			userIn = input("Enter a date as the following example- 'Jun 1 2005 1:33PM':")
			d = datetime.strptime(userIn, '%b %d %Y %I:%M%p')
			isValid=True
		except:
			print "Try again!\n"
	return userIn

