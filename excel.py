import xlrd

fname = "Faculty Assignment.xlsx"#works for both xlsx and xls
book = xlrd.open_workbook(fname)
#print(book.nsheets)
sheet = book.sheet_by_index(0)
#print(sheet.name, sheet.nrows, sheet.ncols)
rows = sheet.nrows
cols = sheet.ncols
if sheet.cell_value(0,0) != "SUBJECT CODE" or sheet.cell_value(0,1) != "SUBJECT NAME" or sheet.cell_value(0,2) != "SUBJECT SHORT NAME" or sheet.cell_value(0,3) != "FACULTY" or sheet.cell_value(0,4) != "SEMESTER" or sheet.cell_value(0,5) != "SECTION" :
	print("fail")#show notification of file does not have required format
else:
	#print("pass")
	sub_code = []
	sub_name = []
	sub_short_name = []
	faculty = []
	sem = []
	sec = []
	for r in range(1, rows):# iterate rowss
		sub_code.append(sheet.cell_value(r,0))
		sub_name.append(sheet.cell_value(r,1))
		sub_short_name.append(sheet.cell_value(r,2))
		faculty.append(sheet.cell_value(r,3))
		sem.append(sheet.cell_value(r,4))
		sec.append(sheet.cell_value(r,5))
	print(sub_code)
	print(sub_name)
	print(sub_short_name)
	print(faculty)
	print(sem)
	print(sec)
	#print(len(sub_code))



#SUBJECTS ASSIGNED:  {'III': {}, 'V': {}, 'IV': {'A': ['Design & Analysis of Algorithms - DAA - Venugopala P S', 'Finite Automata & Formal languages - FAFL - Ravi B', 'Data Communications - DC - Radhakrishna Dodmane', 'Computer Organization & Architecture - CO - Pradeep Nazareth', 'Unix Programming - Unix - Sannidhan M S', 'Algorithms|Unix Lab - DAA|Unix Lab - Venugopala P S, Sannidhan M S', 'Enhancing Self Competence - ESC - ', 'Probability Theory and Numberical Methods - Maths - Anitha D Bayar'], 'B': ['Probability Theory and Numberical Methods - Maths - Shashirekha B Rai', 'Design & Analysis of Algorithms - DAA - Roshan Fernandes', 'Finite Automata & Formal languages - FAFL - Radhakrishna Dodmane', 'Data Communications - DC - Uday Kumar Shenoy', 'Computer Organization & Architecture - CO - Raghunandan K R', 'Unix Programming - Unix - Shabari Shedthi B', 'Algorithms|Unix Lab - DAA|Unix Lab - Shabari Shedthi B, Roshan Fernandes', 'Enhancing Self Competence - ESC - '], 'C': ['Probability Theory and Numberical Methods - Maths - Anitha D Bayar', 'Design & Analysis of Algorithms - DAA - Asmitha Poojari', 'Finite Automata & Formal languages - FAFL - K R Uday Kumar Reddy', 'Data Communications - DC - Sharada Uday Shenoy', 'Computer Organization & Architecture - CO - Raju K', 'Unix Programming - Unix - Ranjan Kumar H S', 'Algorithms|Unix Lab - DAA|Unix Lab - Asmitha Poojari, Ranjan Kumar H S', 'Enhancing Self Competence - ESC - '], 'D': ["Probability Theory and Numberical Methods - Maths - Apoorva D'Souza", 'Design & Analysis of Algorithms - DAA - Pallavi K N', 'Finite Automata & Formal languages - FAFL - Ramesha Shettigar', 'Data Communications - DC - Krishna Prasad Rao', 'Computer Organization & Architecture - CO - Sarika Hegde', 'Unix Programming - Unix - Savitha Shetty', 'Algorithms|Unix Lab - DAA|Unix Lab - Pallavi K N, Savitha Shetty', 'Enhancing Self Competence - ESC - ']}, 'VI': {'A': ['Computer Graphics - CG - Shilpa M K', 'Computer Networks - CN - Sudeepa K B', 'Java and Internet Technologies - JIT - Sandeep Hegde', 'Software Testing - ST - Pradeep Nazareth', ' - CCIM - Roshan Fernandes', ' - MC - Ravi B', 'Employability Skill Development - ESD - Krishna Prasad Rao', 'Computer Graphics|Networks Lab - CG|CN Lab - Shilpa M K, Sudeepa K B', 'Java Lab - JIT Lab - Sandeep Hegde'], 'B': ['Computer Graphics - CG - Sannidhan M S', 'Computer Networks - CN - Chandra Naik', 'Java and Internet Technologies - JIT - Ramesha Shettigar', 'Software Testing - ST - Rajalaxmi Hegde', ' - CCIM - Minu P Abraham', ' - MC - Uday Kumar Shenoy', 'Employability Skill Development - ESD - Sunil Kumar Aithal', 'Computer Graphics|Networks Lab - CG|CN Lab - Sannidhan M S, Chandra Naik', 'Java Lab - JIT Lab - Ramesha Shettigar'], 'C': ['Computer Graphics - CG - Pawan Hegde', 'Computer Networks - CN - Vijay Murari T', 'Java and Internet Technologies - JIT - Mahesh Kini', 'Software Testing - ST - Shabari Shedthi B', ' - CCIM - Venugopala P S', ' - MC - Sharada Uday Shenoy', 'Employability Skill Development - ESD - Sunil Kumar Aithal', 'Computer Graphics|Networks Lab - CG|CN Lab - Pawan Hegde, Vijay Murari T', 'Java Lab - JIT Lab - Mahesh Kini'], 'D': ['Computer Graphics - CG - Jyothi Shetty', 'Computer Networks - CN - Chandra Naik', 'Java and Internet Technologies - JIT - Sampath Kini', 'Software Testing - ST - D K Sreekantha', ' - CCIM - Pawan Hegde', ' - MC - Sharada Uday Shenoy', 'Employability Skill Development - ESD - Shilpa M K', 'Computer Graphics|Networks Lab - CG|CN Lab - Jyothi Shetty, Chandra Naik', 'Java Lab - JIT Lab - Sampath Kini']}, 'VII': {}, 'VIII': {'A': ['Engineering Management - EM - Rama Krishna', 'Big Data Analytics - BA - Mohammed Javed', 'BA for Industries - BAI - Naveen Chandavarkar', 'Open Elective - OE - '], 'B': ['Engineering Management - EM - Rama Krishna', 'Big Data Analytics - BA - Anisha P Rodrigues', 'BA for Industries - BAI - Sunil Kumar Aithal', 'Open Elective - OE - '], 'C': ['Engineering Management - EM - Rama Krishna', 'Internet of Things - IOT - Pallavi K N', "Security in Cloud - SIC - Divya Jennifer D'Souza", 'Open Elective - OE - '], 'D': ['Engineering Management - EM - Rama Krishna', 'Internet of Things - IOT - Asmitha Poojari', 'Security in Cloud - SIC - Vijay Murari T', 'Open Elective - OE - ']}}


#FACULTY ASSIGNED: {'': ['Open Elective - OE - VIII C', 'Open Elective - OE - VIII D', 'Open Elective - OE - VIII A', 'Open Elective - OE - VIII B'], 'Puneeth R P': [], 'Ranjan Kumar H S': ['Unix Programming - Unix - IV C', 'Algorithms|Unix Lab - DAA|Unix Lab - IV C'], 'Sudeepa K B': ['Computer Networks - CN - VI A', 'Computer Graphics|Networks Lab - CG|CN Lab - VI A'], 'Rama Krishna': ['Engineering Management - EM - VIII C', 'Engineering Management - EM - VIII D', 'Engineering Management - EM - VIII A', 'Engineering Management - EM - VIII B'], 'Uday Kumar Shenoy': ['Data Communications - DC - IV B', ' - MC - VI B'], 'Vijay Murari T': ['Security in Cloud - SIC - VIII D', 'Computer Networks - CN - VI C', 'Computer Graphics|Networks Lab - CG|CN Lab - VI C'], 'H R Manjunath Prasad': [], 'Shashirekha B Rai': ['Probability Theory and Numberical Methods - Maths - IV B'], 'Anisha P Rodrigues': ['Big Data Analytics - BA - VIII B'], 'Shabari Shedthi B': ['Unix Programming - Unix - IV B', 'Algorithms|Unix Lab - DAA|Unix Lab - IV B', 'Software Testing - ST - VI C'], 'Ankitha A Nayak': [], 'Sharada Uday Shenoy': ['Data Communications - DC - IV C', ' - MC - VI D', ' - MC - VI C'], 'Savitha Shetty': ['Unix Programming - Unix - IV D', 'Algorithms|Unix Lab - DAA|Unix Lab - IV D'], 'Sampath Kini': ['Java and Internet Technologies - JIT - VI D', 'Java Lab - JIT Lab - VI D'], 'Ramesha Shettigar': ['Finite Automata & Formal languages - FAFL - IV D', 'Java and Internet Technologies - JIT - VI B', 'Java Lab - JIT Lab - VI B'], 'Raju K': ['Computer Organization & Architecture - CO - IV C'], 'Krishna Prasad Rao': ['Data Communications - DC - IV D', 'Employability Skill Development - ESD - VI A'], 'Sandeep Hegde': ['Java and Internet Technologies - JIT - VI A', 'Java Lab - JIT Lab - VI A'], 'Rajalaxmi Hegde': ['Software Testing - ST - VI B'], 'Pallavi K N': ['Internet of Things - IOT - VIII C', 'Design & Analysis of Algorithms - DAA - IV D', 'Algorithms|Unix Lab - DAA|Unix Lab - IV D'], 'K R Uday Kumar Reddy': ['Finite Automata & Formal languages - FAFL - IV C'], 'Shilpa M K': ['Computer Graphics - CG - VI A', 'Computer Graphics|Networks Lab - CG|CN Lab - VI A', 'Employability Skill Development - ESD - VI D'], 'Sarika Hegde': ['Computer Organization & Architecture - CO - IV D'], 'Radhakrishna Dodmane': ['Finite Automata & Formal languages - FAFL - IV B', 'Data Communications - DC - IV A'], 'Keerthana B C': [], 'Sannidhan M S': ['Unix Programming - Unix - IV A', 'Computer Graphics - CG - VI B', 'Computer Graphics|Networks Lab - CG|CN Lab - VI B', 'Algorithms|Unix Lab - DAA|Unix Lab - IV A'], 'Asmitha Poojari': ['Design & Analysis of Algorithms - DAA - IV C', 'Algorithms|Unix Lab - DAA|Unix Lab - IV C', 'Internet of Things - IOT - VIII D'], 'Jyothi Shetty': ['Computer Graphics - CG - VI D', 'Computer Graphics|Networks Lab - CG|CN Lab - VI D'], 'Swathi Pai M': [], 'Roshan Fernandes': ['Design & Analysis of Algorithms - DAA - IV B', ' - CCIM - VI A', 'Algorithms|Unix Lab - DAA|Unix Lab - IV B'], 'Minu P Abraham': [' - CCIM - VI B'], 'Mahesh Kini': ['Java and Internet Technologies - JIT - VI C', 'Java Lab - JIT Lab - VI C'], 'Venugopala P S': ['Design & Analysis of Algorithms - DAA - IV A', 'Algorithms|Unix Lab - DAA|Unix Lab - IV A', ' - CCIM - VI C'], 'Pradeep Kanchan': [], 'Shashank Shetty': [], 'K R Raghunandan': [], 'Chandra Naik': ['Computer Networks - CN - VI D', 'Computer Networks - CN - VI B', 'Computer Graphics|Networks Lab - CG|CN Lab - VI B', 'Computer Graphics|Networks Lab - CG|CN Lab - VI D'], "Apoorva D'Souza": ['Probability Theory and Numberical Methods - Maths - IV D'], "Divya Jennifer D'Souza": ['Security in Cloud - SIC - VIII C'], 'Naveen Chandavarkar': ['BA for Industries - BAI - VIII A'], 'Humanities': [' - ESC - IV D', ' - ESC - IV C', ' - ESC - IV B', ' - ESC - IV A'], 'Anitha D Bayar': ['Probability Theory and Numberical Methods - Maths - IV C', 'Probability Theory and Numberical Methods - Maths - IV A'], 'D K Sreekantha': ['Software Testing - ST - VI D'], 'Ravi B': ['Finite Automata & Formal languages - FAFL - IV A', ' - MC - VI A'], 'Raghunandan K R': ['Computer Organization & Architecture - CO - IV B'], 'Pawan Hegde': [' - CCIM - VI D', 'Computer Graphics - CG - VI C', 'Computer Graphics|Networks Lab - CG|CN Lab - VI C'], 'Mohammed Javed': ['Big Data Analytics - BA - VIII A'], 'Pradeep Nazareth': ['Computer Organization & Architecture - CO - IV A', 'Software Testing - ST - VI A'], 'Smitha G V': [], 'Rajashree': [], 'Sunil Kumar Aithal': ['BA for Industries - BAI - VIII B', 'Employability Skill Development - ESD - VI B', 'Employability Skill Development - ESD - VI C']}