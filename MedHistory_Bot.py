# Pseudocode formatting MedHistory writing (SP cases)

class 入院病历(basic_info, summary, 
			current_report, past_history, 
			personal_history, 
			marriage_history, menstrual_history, child_bearing_history, family_history):

	def create_report():
		report = '\n'.join(
			basic_info, summary, 
			current_report, past_history, 
			personal_history, 
			marriage_history, menstrual_history, child_bearing_history, family_history
			)
	
	#---------------
	def add_basic_info(name='WW', sex='F', age=52, 
					   birth_place:'Beijing', 民族:'汉', 
					   marriage=True, occupation':'retired worker',working_site:None,
					   reception_date:'2020-09-24', recording_time:'2020-09-24',
					   病史陈述人:'本人',reliability:'high') 

		txt = '\n'.join()
		return txt

	basic_info = add_basic_info()

	#---------------
	def add_summary(symp_old='Dyspnea', time_old='10 years',
					symp_current='Cough, Dyspnea', time_new='2 days'):
		txt = f'{symp_old} {time_old},  {symp_current} {time_new}' # no name added!
		return txt
	summary = add_summary()

	#---------------
	def add_current_report(progressive=True): # including all past history relevant to current
		
		def main_symp(x):
			if x in pain_list:
				desc = {'loci':'behind chest', 'size':'fist', 
				'VAS score':4, 'Type':'blunt',
				'radiation':'left scapular'
				}
				time = {'start':-2, 'freq':'interval', 'progression':True}

			txt = ','.join([desc.values])
			return txt


		def co_symp(): # a list of associated symp for Differential Dx

		def neg_symp():
			desc = {'spirit':'low', 
					'appetite':'low', 'sleep':'good',
					'urine_feces':'normal', 'body_weight':'unchanged'}

		def treatment(x):
			desc = {'operation_name':None, 'drug_name':None,
					'dose':3, 'freq': 3, 'period':2}

		def timely_symp(x):
			sp = main_symp(x) + co_symp(x) 
				+ diagnosis(x) + labs(x)
				+ treatment(x) + afterTx_cond(x)
			return sp

		txt = name
		if progressive:

			times = range(3) # most distant to most recent

			for time in times: 
				txt += '\t'.join(time, timely_symp(x))

			txt += neg_symp(x)

		return = txt

	current_report = add_current_report()
	
	#---------------
	def add_past_history(current_report, progressive=True, desc=None): 

		txt = add_current_report(xx, progressive=progressive) # all past history less relevant to current

		cardioVas = {'HTN':True, 'High_Glc':True, 'High_Lipid':True, 'CAD':True} # coronary artery disease
		allergy = {'food':None, 'drug':'penicillin'}
		vaccine = {'MMP':True}

		if age>45:
			txt += cardioVas
			
		txt += allergy, txt+= vaccine

		return txt	

	past_history = add_past_history()

	#---------------
	def add_personal_history(cardioVas=True, smoking=True, drink=True,
							year_smoke=20, n_pack=1.5, 
							year_drink=15, wine='whiskey', n_cup=2.5,
							travel_spots=None):

		desc = {'occupation':'worker', ''}
		smoking = f'{year_smoke} years, {n_pack} packs per day'
		drinking = f'{year_drink} years, {n_cup} cups of {wine} per day'

		if age>45:
			desc += smoking, desc += drinking

		for spot in travel_spots:
			start_time, end_time, co_travelers, transporter_No= None, None, ['ZS','LS'], ['CZ123','CA231']
			desc += f'{spot} {start_time} {end_time} {co_travelers} {transporter_No}'

		return desc

	personal_history = add_personal_history()

	#---------------		
	def add_sexual_history(female=True,
				 year_marriage=30, partner_health='good',
				 start_age=13, end_age=50, days_bleeding=4, days_cycle=30,
				 num_child=1, sex_child='son', health_child='good',
				 num_gravidy=3, num_parity=2
				 ):


		marriage_history = f'{year_marriage} years, {partner_health}'
		menstrual_history = f'{start_age} \frac{days_bleeding}{days_cycle} {end_age}'
		child_bearing_history = f'{num_child} {sex_child} {health_child}'

		if female:
			OB_history = '{num_gravidy}G{num_parity}P' # number of conception and pregancy
			child_bearing += OB_history
				
		return marriage_history, menstrual_history, child_bearing_history

	marriage_history, menstrual_history, child_bearing_history = add_sexual_history()

	#---------------	
	def add_family_history(parents=None, siblings=None, health='good',
						  'disease_hereditary':None, 'disease_contagious':None):
		desc = ''
		for person in parents+siblings:
			desc += f'{person} {health}'

		return desc

	family_history = add_family_history()

#---------------
if __name__ == "__main__":
	create_report()

