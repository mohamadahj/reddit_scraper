##############################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from horizontal_barchart_distribution import survey_hbd


##############################################################################
def my_survey(data):
	survey = pd.DataFrame([], columns = ['Param', 'Type', 'uCount', 'nanCount', 'Detail'])
	survey['Param']= data.columns
	temp= data.dtypes.values
	for i,name in enumerate(data.columns):
		survey['Type'][i]= temp[i].name
		survey['uCount'][i]= len(pd.unique(data[name]))
		try:
			survey['nanCount'][i]= np.sum(np.isnan(data[name]))
		except:
			survey['nanCount'][i]= np.sum(data[name].isnull())
# 		survey['Detail'][i]= data[name].value_counts()
	return survey


##############################################################################
emacs= pd.read_csv('emacs_scrape_result.csv')
vim= pd.read_csv('vim_scrape_result.csv')

temp= [pd.to_datetime(emacs['datetime'][i]).date() for i in range(len(emacs))]
emacs['just_date'] = pd.DataFrame(temp)
temp= [pd.to_datetime(vim['datetime'][i]).date() for i in range(len(vim))]
vim['just_date'] = pd.DataFrame(temp)

temp= [emacs['just_date'][i].strftime('%Y-%m') for i in range(len(emacs))]
emacs['year_month']= pd.DataFrame(temp)
temp= [vim['just_date'][i].strftime('%Y-%m') for i in range(len(vim))]
vim['year_month']= pd.DataFrame(temp)

##############################################################################
emacs_survey= my_survey(emacs)
vim_survey= my_survey(vim)


##############################################################################
# e0= sum(emacs['num_crossposts']==0)/len(emacs)*100
# e1= sum(emacs['num_crossposts']==1)/len(emacs)*100
# v0= sum(vim['num_crossposts']==0)/len(vim)*100
# v1= sum(vim['num_crossposts']==1)/len(vim)*100

# category_names = ['0', '1']
# results = {
# 	'emacs': [e0, e1],
# 	'vim': [v0, v1]
# }

# survey_hbd(results, category_names)


##############################################################################
plt.figure()

t1= emacs.groupby(['just_date']).count()
t2= vim.groupby(['just_date']).count()

group1= emacs.groupby(['just_date']).count()[['id']]
group1= group1.rename(columns={"id": "emacs"})
group2= vim.groupby(['just_date']).count()[['id']]
group2= group2.rename(columns={"id": "vim"})
result = pd.concat([group1, group2], axis=1)

plt.plot(result.index, result['emacs'], label = 'emacs')
plt.plot(result.index, result['vim'], label = 'vim')
plt.title('compare number of ID per date')
plt.legend()


##############################################################################
plt.figure()

group1= emacs.groupby(['year_month']).count()[['id']]
group1= group1.rename(columns={"id": "emacs"})
group2= vim.groupby(['year_month']).count()[['id']]
group2= group2.rename(columns={"id": "vim"})
result = pd.concat([group1, group2], axis=1)

plt.plot(result.index, result['emacs'], label = 'emacs')
plt.plot(result.index, result['vim'], label = 'vim')
plt.title('compare number of ID per month')
plt.legend()

##############################################################################
plt.figure()

group11= emacs.groupby(['year_month']).groups
group22= vim.groupby(['year_month']).groups
result['emacs_author']= 0
result['vim_author']= 0
for ind in result.index:
	result['emacs_author'][ind]= len(emacs['author'][group11[ind]].unique())
	result['vim_author'][ind]= len(vim['author'][group22[ind]].unique())

plt.plot(result.index, result['emacs_author'], label = 'emacs')
plt.plot(result.index, result['vim_author'], label = 'vim')
plt.title('compare number of ID per month')
plt.legend()


##############################################################################
# plt.figure()

category_names = result.index.to_list()
results = {
	'emacs_id': [result['emacs'][i]/sum(result['emacs'])*100 for i in result.index],
	'vim_id': [result['vim'][i]/sum(result['vim'])*100 for i in result.index],
	'emacs_author': [result['emacs_author'][i]/sum(result['emacs_author'])*100 for i in result.index],
	'vim_author': [result['vim_author'][i]/sum(result['vim_author'])*100 for i in result.index]
}

survey_hbd(results, category_names)


##############################################################################
plt.figure()

all_data = [np.array(emacs['score']),np.array(vim['score'])]
labels = ['emacs_score','vim_score']

bplot = plt.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
colors = ['lightblue', 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
	patch.set_facecolor(color)
plt.show()


##############################################################################
plt.figure()

all_data = [np.array(emacs['num_comments']),np.array(vim['num_comments'])]
labels = ['emacs_comments','vim_comments']

bplot = plt.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
colors = ['lightblue', 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
	patch.set_facecolor(color)
plt.show()


##############################################################################
plt.figure()

group1= emacs.groupby(['just_date']).count()[['id']]
group1= group1.rename(columns={"id": "emacs"})
group2= vim.groupby(['just_date']).count()[['id']]
group2= group2.rename(columns={"id": "vim"})
result = pd.concat([group1, group2], axis=1)

group11= emacs.groupby(['just_date']).groups
group22= vim.groupby(['just_date']).groups
result['emacs_comment']= 0
result['vim_comment']= 0
for ind in result.index:
	result['emacs_comment'][ind]= sum(emacs['num_comments'][group11[ind]])
	result['vim_comment'][ind]= sum(vim['num_comments'][group22[ind]])

plt.plot(result.index, result['emacs_comment'], label = 'emacs')
plt.plot(result.index, result['vim_comment'], label = 'vim')
plt.title('compare number of comments per date')
plt.legend()
plt.show()

##############################################################################
plt.figure()

all_data = [np.array(result['emacs']),np.array(result['vim'])]
labels = ['emacs_date','vim_date']

bplot = plt.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
colors = ['lightblue', 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
	patch.set_facecolor(color)
plt.show()


##############################################################################
plt.figure()

all_data = [np.array(result['emacs_comment']),np.array(result['vim_comment'])]
labels = ['emacs_comment','vim_comment']

bplot = plt.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks
colors = ['lightblue', 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
	patch.set_facecolor(color)
plt.show()

##############################################################################
plt.figure()

temp1= emacs.groupby(['domain']).count()[['id']]
temp2= vim.groupby(['domain']).count()[['id']]
t1= np.sort(np.array(temp1['id']))[::-1]
t2= np.sort(np.array(temp2['id']))[::-1]

result_new= np.zeros([np.max([len(temp1),len(temp2)]),2])
result_new[:len(t1),0]= t1
result_new[:len(t2),1]= t2
result_new= pd.DataFrame(result_new, columns=['emacs','vim'])

plt.plot(result_new.index, result_new['emacs'], label = 'emacs')
plt.plot(result_new.index, result_new['vim'], label = 'vim')
plt.title('compare number of domain (log scale)')
plt.yscale('log')
plt.legend()
plt.show()