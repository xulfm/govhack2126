import geocoder
import pandas as pd

 

data = pd.read_csv('ADDRESS CSV', delimiter=',')
df = pd.read_csv(' *STORAGE CSV*')


address_list = data.values.tolist()

counter = 0
for address in address_list:
    
    if counter == len(address_list):
        break

    else:
        location = geocoder.google(str(address), key="*API KEY*")
        df = pd.DataFrame([location.latlng])
        df.to_csv('STORAGE CSV', mode='a',index=False, header=False)

        counter +=1
        print(counter)

