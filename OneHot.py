import random
import pandas as pd 
#никак не удается импортировать panda - перепробовал все (уставливал "через" pip)
#Но по идее если импорт panda будет корректный, все должно работать.
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

data['temp'] = 1
data.set_index([data.index, 'whoAmI'], inplace = True)
data = data.unstack(level = -1, fill_value = 0).astype (int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)