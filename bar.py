import matplotlib.pyplot as plt
import pandas as pd
x=['grocery','rent','education of childern','meicine','fuel','entertainment','miscelloneous']
y=[4,5,5,2,2,1,1]
plt.bar(x,y,color='green',edgecolor='blue',linewidth=3)
plt.title("familymonthly plan")
plt.xlabel('heads')
plt.ylabel('expenditure(in thousand rupees)')
plt.xticks(x,rotation=45)
plt.show()
