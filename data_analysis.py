#This assigment provide a data analysis about life expectancies over the years in all countries of the world
#To improve my project, I give the option to the user choose between Year or Country, instead of only Year.

max_life = -1
overall_max_life = -1
overall_min_life = float("inf")
min_life = float("inf")
sum = 0
number_of_countries = 0


print("Welcome to the program of life expectancy! ")

print("What type of data you wanna choose to see? ")
print("About 'Country' ")
print("About 'Year' ")
user_input = input("Enter your desired type of data: ").capitalize().strip()
   
if user_input == "Country":
  desired_country = input("What country do you wanna know about? ").capitalize()

elif user_input == "Year":
  desired_year = input ("What year do you wanna know about? ")

with open("life-expectancy.csv") as life_expec_file:
    next(life_expec_file)
    for line in life_expec_file:
        clean_line = line.strip()
        parts = clean_line.split(",")
        entity = parts[0]
        code = parts[1]
        year = parts[2]
        life_expec = float(parts[3])

        if life_expec > overall_max_life:
          overall_max_life = life_expec
          overall_max_country = entity
          overall_max_year = year

        if life_expec < overall_min_life:
          overall_min_life = life_expec
          overall_min_country = entity
          overall_min_year = year

        if user_input == "Country":
           if entity == desired_country:
             desired_country= entity

             if life_expec >= max_life:
              max_life = life_expec
            
             if life_expec < min_life:
              min_life = life_expec
              min_entity = entity

             sum += life_expec
             number_of_countries += 1
             average_expectancy = sum/number_of_countries
             

        elif user_input == "Year":
          
          if year == desired_year:

             if life_expec >= max_life:
              max_life = life_expec
              max_country = entity
            
             if life_expec < min_life:
              min_life = life_expec
              min_country = entity

             sum += life_expec
             number_of_countries += 1
             average_expectancy = sum/number_of_countries

        

print(f"The overall max life expectancy is: {overall_max_life} from {overall_max_country} in {overall_max_year}. ")
print(f"The overall min life expectancy is: {overall_min_life} from {overall_min_country} in {overall_min_year}. ")

if user_input == "Country":
  print(f"For {desired_country}: ")
  print(f"The average life expectancy across the years was {average_expectancy:.2f} ")
  print(f"The max life expectancy was {max_life}")
  print(f"The min life expectancy was {min_life}")

elif user_input == "Year":
  print(f"For the year {desired_year}: ")
  print(f"The average life expectancy across all countries was {average_expectancy:.2f}. ")
  print(f"The max life expectancy was in {max_country} with {max_life}. ")
  print(f"The min life expectancy was in {min_country} with {min_life}. ")

    

        
    
        