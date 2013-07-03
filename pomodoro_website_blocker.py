import shutil, time, os

#use Windows Task Scheduler to run this script at startup whenever a user logs on (search start menu for task scheduler)
#need to set it to run as administrator - this script needs to be able to write to system folders
#Instrutions for using Task scheduler found here: http://windows.microsoft.com/en-US/windows7/schedule-a-task

hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\'
#need to have full control over the 'hosts' file in this folder. Do this by going to the file properties, giving user these priviledges.

black_list = ('www.reddit.com',
 'static.reddit.com',
 'news.ycombinator.com',
 'www.twitter.com',
 'www.facebook.com',
 'www.lesswrong.com',
 'www.youtube.com'
 )
blocking_time = 25 #in minutes
break_time = 5

do_pomodoro = True
p = 0
while(do_pomodoro==True):
	f = open(hosts_path+'hosts', 'w')
	for site in black_list:
		f.write('127.0.0.1\t'+site+'\n')
	f.close()

	#after changing the dns cache, need to close all open browsers
	#In firefox, or any other browser with a built-in dns cache, need to ensure that it updates the built-in cache from the hosts file very regularly
	#Firefox: go to about:config, add new variable 'network.dnscacheexpiration' to be an integer equal to 0 (its in seconds)

	time.sleep(blocking_time*60)

	# os.remove(hosts_path+'hosts')
	f = open(hosts_path+'hosts', 'w')
	f.write('')
	f.close()

	print("\n"+blocking_time.__str__()+" minutes elapsed! Pomodoro finished!\n")
	print("Take a "+break_time.__str__()+" minute break. You can access any website in this period.\n")

	time.sleep(break_time*6)
	
	answer = raw_input("Break finished! Do another pomodoro (y/n)?")
	p = p+1
	if (answer=='y' or answer=='yes'):
		continue
	else:
		do_pomodoro = False

print("You did a total of " + p.__str__() + " pomodoros in this session.")
time.sleep(5)