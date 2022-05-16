#%% 
import utilities as ut

list_of_subjects = []
subj_numbers = []
number_of_subjects = 0

folder_current = os.path.dirname(__file__) 
print(folder_current)
folder_input_data = os.path.join(folder_current, "input_data")
for file in os.listdir(folder_input_data):
    
    if file.endswith(".csv"):
        number_of_subjects += 1
        file_name = os.path.join(folder_input_data, file)
        print(file_name)
        list_of_subjects.append(ut.Subject(file_name))

#%%



for i in list_of_subjects:
    a=i.blood_flow.max()
    print(a)

    #print
    
  #  maxtemperature=i.temp.max()
   # maxtemperature+i
    #maxspO2=i.spO2.max()
    #maxspO2+i
   ## print(a)
   # print(b)
  #  print(c)


#%%
a=list_of_subjects[0]
maxbloodflow=a.blood_flow.max()
maxtemperature=a.temp.max()
maxspO2=a.spO2.max()
print(maxbloodflow)
print(maxtemperature)
print(maxspO2)



# %%
