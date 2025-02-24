#Simple trend graph with 2 lines
#Data hardcoded in lists
#Ms G Hennessy - CUS

import matplotlib.pyplot as plt

# Creation of Data 
headings = ['8am', '9am', '10am', '11am', '12am', '1pm', '2pm', '3pm'] 
perfect = [100, 95, 100, 95, 100, 95,100, 95] 
you = [100, 90, 80, 90, 80, 70, 60, 70] 
  
# Plotting the Data 
plt.plot(headings, perfect, label='Perfect Hydration') 
plt.plot(headings, you, label='You') 
  
plt.xlabel('time') 
plt.ylabel('hydration level') 
plt.title("Hydration record") 
  
plt.plot(perfect, linestyle='--', linewidth='4') 
plt.plot(you, linestyle=':', linewidth='4')

plt.legend()
plt.show()