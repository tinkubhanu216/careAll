Elders={}
Youngers={}
Requests={}
Responce={}
Rating={}
Hired={}
panel="home"
user_id=""
while(1):
	print("\n**************CareAll**************\n")
	if(panel=="home"):
		op=str(input("1. Login\n2. Register\n3.Exit\nChoose your Option:"))
		if(op=='1'):
			user_type=input("Choose User Type( Elder(e) or Younger(y)):")
			if(user_type=="e"):
				user_id=input("Enter User ID:")
				try:
					d=Elders[user_id]
					panel="elder"
					print("Successfully Logged On")
				except KeyError:
					print("User not exist. Please Register")
			elif(user_type=="y"):
				user_id=input("Enter User ID:")
				try:
					d=Youngers[user_id]
					panel="younger"
					print("Successfully Logged On")
				except KeyError:
					print("User not exist. Please Register")
			else:
				print("Invalid Input\n")
		elif(op=='2'):
			user_type=input("Choose User Type( Elder(e) or Younger(y)):")
			if(user_type=="e"):
				user_id=input("Enter User ID:")
				user_name=input("Enter your Name:")
				age=int(input("Enter your Age"))
				fund=input("Enter fund")
				contact=input("Enter contact details:")
				Elders[user_id]=[user_name,age,fund,contact]
				Requests[user_id]=[]
				Rating[user_id]=[]
			elif(user_type=="y"):
				user_id=input("Enter User ID:")
				user_name=input("Enter your Name:")
				age=int(input("Enter your Age:"))
				contact=input("Enter contact details:")
				Youngers[user_id]=[user_name,age,contact]
				Hired[user_id]=[]
				Rating[user_id]=[]
			else:
				print("Invalid Input\n")
		elif(op=='3'):
			break
		else:
			print("Invalid Input\n")
	elif(panel=="elder"):
		op=str(input("1. careRequests\n2. Approve careRequests\n3. addRating\n4. myRating\n5. remove Young folk\n6. logout\nChoose your Option:"))
		if(op=='1'):
			data=Requests[user_id]
			if(len(data)>0):
				num=1
				for request in data:
					print("------------ S. No ",num,"----------")
					num+=1
					print("Younger ID:",request)
					print("Name:",Youngers[request][0])
					print("Age:",Youngers[request][1])
					print("Contact Info:",Youngers[request][2])
			else:
				print("No Requests Found")
		elif(op=='2'):
			hire=False
			yid=""
			for young_id in Hired:
				if(user_id in Hired[young_id]):
					hire=True
					yid=young_id
					break
			if(not(hire)):
				young_id=input("Enter young_id:")
				try:
					if(len(Hired[young_id])<=4):
						Hired[young_id].append(user_id)
						print("Successfully Hired Young folk")
					else:
						print("Young folk limit is Reached")
				except KeyError:
					print("young_id not found")
			else:
				print("You are already hired a younger: id is:",yid)
		elif(op=='3'):
			young_id=input("Enter younger ID:")
			try:
				rate=int(input("Enter Rating on Scale 5:"))
			except ValueError:
				print("Invalid input: Rating should be number")
			review=input("Enter review:")
			try:
				Rating[young_id].append((rate,review))
				print("Thank you for feedback\n")
			except KeyError:
				print("young_id not found")
		elif(op=='4'):
			data=Rating[user_id]
			r=0
			print("Reviews:")
			for rating in data:
				r+=rating[0]
				print(rating[1])
			try:
				print("Overall Rating on Scale 5 is: ",r/len(data))
			except ZeroDivisionError:
				print("No rating exist")
		elif(op=='5'):
			for young_id in Hired:
				if(user_id in Hired[young_id]):
					Hired[young_id].remove(user_id)
					print("Successfully Removed Younge folk\n")
					break
		elif(op=='6'):
			panel="home"
			user_id=""
		else:
			print("Invalid Input\n")

	elif(panel=="younger"):
		op=str(input("1. searchElder\n2. RequestElder\n3. my_Elders\n4. addRating\n5. myRating\n6. logout\nChoose your Option:"))
		if(op=='1'):
			eld=[]
			num=1
			for elder in Elders:
				found=False
				for young in Hired:
					if(elder in Hired[young]):
						found=True
						break
				if(not(found)):
					print("---------------S.No ",num,"--------------")
					print("Elder ID:",elder)
					print("Name:",Elders[elder][0])
					print("Age:",Elders[elder][1])
					print("Funding:",Elders[elder][2])
					print("Contact:",Elders[elder][3])
					num+=1
		elif(op=='2'):
			try:
				if(len(Hired[user_id])<=4):
					elder_id=input("Enter ElderId:")
					Requests[elder_id].append(user_id)
				else:
					print("Your Limit is Reached")
			except KeyError:
				print("elder_id not found")
		elif(op=='3'):
			if(len(Hired[user_id])>0):
				for data in Hired[user_id]:
					print(data)
			else:
				print("Data not found")
		elif(op=='4'):
			elder_id=input("Enter younger ID")
			try:
				rate=int(input("Enter Rating on Scale 5:"))
			except ValueError:
				print("Invalid input: Rating should be number")
			review=input("Enter review")
			try:
				Rating[elder_id].append((rate,review))
				print("Thank you for feedback\n")
			except KeyError:
				print("young_id not found")
		elif(op=='5'):
			data=Rating[user_id]
			r=0
			print("Reviews:")
			for rating in data:
				r+=rating[0]
				print(rating[1])
			try:
				print("Overall Rating on Scale 5 is: ",r/len(data))
			except ZeroDivisionError:
				print("No rating exist")
		elif(op=='6'):
			panel="home"
			user_id=""
		else:
			print("Invalid Input\n")
print("Thank You")
