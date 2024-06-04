with open("hr_system.txt") as data_hr:
  
  for line in data_hr:
    clean_line = line.strip()
    parts = clean_line.split()
    name = parts[0]
    id_number = parts[1]
    job_title = parts[2]
    salary = float(parts[3])
    
    paycheck_amount = salary/24

    if job_title.lower()== "engineer":
      paycheck_amount += 1000
      
    print(f"{name} (ID: {id_number}), {job_title} - ${paycheck_amount:.2f} ")
    