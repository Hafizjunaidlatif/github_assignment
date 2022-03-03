
#steps involved Data Visualiztion

# step-1 Import Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# step-2 set a theme
sns.set_theme(style="ticks", color_codes=True)

#step-3 import data set, you can also import your own data
kashti = sns.load_dataset("titanic")
#print(kashti)


# # #step-4 plot basis graph with 1 variable
# p = sns.countplot(x= "sex", data=kashti)
# plt.show()

# # #step-5 plot basis graph with 2 variable 
# p = sns.countplot(x= "sex", data=kashti, hue="class")
# plt.show()

# # #step-6 plot basis graph with 2 variable (count plot) with title
p = sns.countplot(x= "sex", data=kashti, hue="class") 
# ***p yahan imp ha, coz p sy hm ny plot banay ha an p p hm title bny gy.
p.set_title("count plot of titanic")
plt.show()
