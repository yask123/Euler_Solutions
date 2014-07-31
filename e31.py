#200 * a1 + 100*a2+50*a3+20*a4+10*a5+5*a6+2*a7+a8
count=0
for a1 in range(2):
	if 200*a1<200:
		for a2 in range(3):
			if 200*a1+100*a2<200:
				for a3 in range(5):
					if 200*a1+100*a2+50*a3<200:
						for a4 in range(6):
							if 200*a1+100*a2+50*a3+20*a4<200:
								for a5 in range(21):
									if 200*a1+100*a2+50*a3+20*a4+10*a5<200:
										for a6 in range (41):
											if 200*a1+100*a2+50*a3+20*a4+10*a5+5*a6<200:
												for a7 in range(101):
													if 200*a1+100*a2+50*a3+20*a4+10*a5+5*a6+2*a7<200:
														for a8 in range(201):
															if 200*a1+100*a2+50*a3+20*a4+10*a5+5*a6+2*a7+a8 == 200:
																count+=1
print (count)																

