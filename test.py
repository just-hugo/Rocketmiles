from RocketMilesClass import RocketMiles
import time

RM = RocketMiles()

#Sandbox Preconditions

#Sandbox


#Smoke test
#Preconditions
RM.open_rocketMiles()
RM.close_popUp_2()
RM.close_cookie_banner()

#TCID 1: Main Page - Can a user enter a destination?
RM.select_destination_field()
RM.type_destination()
print('TCID 1 has been executed.')

#TCID 2: Main Page - Can a user enter a rewards program?
RM.select_rewards()
RM.type_rewards()
print('TCID 2 has been executed.')

#TCID 3: Main Page - Can a user select the end date field?
RM.click_end_date()
print('TCID 3 has been executed.')

#TCID 4: Main Page - Can a user select a start date?
RM.click_start_date()
RM.click_November_21()
print('TCID 4 has been executed.')

#TCID 5: Main Page - Can a user select an end date from the end date calendar?
RM.click_November_25()
print('TCID 5 has been executed.')

#TCID 6: Main Page - Can a user select the number of guests?
RM.select_guest_field()
RM.click_1_guest()
print('TCID 6 has been executed.')

#TCID 7: Main Page - Can a user select the number of rooms?
RM.select_rooms_field()
RM.click_1_room()
print('TCID 7 has been executed.')

#TCID 8: Main Page - Can a user select the Search button?
RM.click_search_properties_button()
print('TCID 8 has been executed.')

#TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?
print('Beginning TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?')
RM.select_sort_by_field()
RM.click_miles()
print('TCID 9 has been executed.')

#TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?
print('Beginning TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?')
RM.select_hotel()
print('TCID 10 has been executed.')

#Precondition for proceeding with smoke test
RM.switch_tabs()

#TCID 11: Hotel Details - Can a user select the Select A Room button?
print('Beginning TCID 11: Hotel Details - Can a user select the Select A Room button?')
RM.click_select_room_button()
print('TCID 11 has been executed.')

#TCID 12: Hotel Details - Can a user select the View button?
print('Beginning TCID 12: Hotel Details - Can a user select the View button?')
RM.select_view_button()
print('TCID 12 has been executed.')

#TCID 13: Hotel Details - Can a user select the green Select button to choose a room?
print('Beginning TCID 13: Hotel Details - Can a user select the green Select button to choose a room?')
RM.select_button()
print('TCID 13 has been executed.')

#TCID 14: Checkout - Can a user enter a Guest First Name?
print('Beginning TCID 14: Checkout - Can a user enter a Guest First Name?')
RM.select_guest_first_name()
RM.type_first_name()
print('TCID 14 has been executed.')

#TCID 15: Checkout - Can a user enter a Guest Last Name?
print('Beginning TCID 15: Checkout - Can a user enter a Guest Last Name?')
RM.select_guest_last_name()
RM.type_last_name()
print('TCID 15 has been executed.')

#TCID 16: Checkout - Can a user enter Your First Name?
print('Beginning TCID 16: Checkout - Can a user enter Your First Name?')
RM.select_your_first_name()
RM.type_first_name()
print('TCID 16 has been executed.')

#TCID 17: Checkout - Can a user enter Your Last Name?
print('Beginning TCID 17: Checkout - Can a user enter Your Last Name?')
RM.select_your_last_name()
RM.type_last_name()
print('TCID 17 has been executed.')

#TCID 18: Checkout - Can a user enter an email address?
print('Beginning TCID 18: Checkout - Can a user enter an email address?')
RM.select_email_address()
RM.type_email_address()
print('TCID 18 has been completed.')

#TCID 19: Checkout - Can a user enter a new password?
print('Beginning TCID 19: Checkout - Can a user enter a new password?')
RM.select_new_password()
RM.type_password()
print('TCID 19 has been completed.')

#TCID 20: Checkout - Can a user confirm a new password?
print('Beginning TCID 20: Checkout - Can a user confirm a new password?')
RM.select_confirm_password()
RM.type_password()
print('TCID 20 has been executed.')

#TCID 21: Checkout - Can a user enter a United MileagePlus acount number?
print('Beginning TCID 21: Checkout - Can a user enter a United MileagePlus acount number?')
RM.select_reward_account()
RM.type_reward_account()
print('TCID 21 has been executed.')

#TCID 22: Checkout - Can a user enter a United MileagePlus first name?
print('Beginning TCID 22: Checkout - Can a user enter a United MileagePlus first name?')
RM.select_reward_first_name()
RM.type_first_name()
print('TCID 22 has been executed.')

#TCID 23: Checkout - Can a user enter a United MileagePlus last name?
print('Beginning TCID 23: Checkout - Can a user enter a United MileagePlus last name?')
RM.select_reward_last_name()
RM.type_last_name()
print('TCID 23 has been executed.')

#TCID 24 - 27: Checkout - Can a user enter a credit card number to the credit card number field?
print('Beginning Checkout - Payment test series (TCIDs 24-27)')
time.sleep(3)
RM.enter_cc_info()
print('Checkout - Payment test series (TCIDs 24-27) have been executed.')

#Precondition
RM.switch_to_default_frame()

#TCID 28: Checkout - Can a user enter a billing zip code?
print('Beginning TCID 28: Checkout - Can a user enter a billing zip code?')
RM.select_billing_zip()
RM.type_billing_zip()
print('TCID 28 has been executed.')

#TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?
print('Beginning TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?')
RM.click_terms_checkbox()
print('TCID 29 has been executed.')


