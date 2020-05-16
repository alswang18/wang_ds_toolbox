import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def waterfall_plot(index_names,data,prefix='',suffix='',calc_total=True,total=None,
                   final_sum_name='net',is_money=True,title='',final_line=True,output=False,
                   output_path='waterfall.png'):
    #     examples for index_names
    #     index_names = ['sales','returns','credit fees','rebates','late charges','shipping']
    #     data = [350000,-30000,-7500,-25000,95000,-7000]
    def create_trans_blank(index_names,data):
        trans = pd.DataFrame(index=index_names,data=data)
        blank = trans.amount.cumsum().shift(1).fillna(0)
        return trans, blank
    def process_net(calc_total,total,trans,blank,final_sum_name):
        if(calc_total and total==None):
            total = trans.sum().amount
            trans.loc[final_sum_name]= total
            blank.loc[final_sum_name] = total
        elif(total!=None):
            if(type(total) is not int and type(total) is not float):
                raise TypeError("total is not a number")
            total = total
            trans.loc[final_sum_name]=total
            blank.loc[final_sum_name]=total
        else:
            print('No Totals Column')
    def process_step(final_line,blank):
        step = blank.reset_index(drop=True).repeat(3).shift(-1)
        step[1::3] = np.nan
        if(not final_line):
            step[-4:-3]=np.nan
        return step
    if(len(index_names)!=len(data)):
        raise Exception("index and data do not have the same index length")
    data = {'amount':data}
    if(is_money):
        def money(x, pos):
            'The two args are the value and tick position'
            return "{:,.0f}".format(x)

        formatter = FuncFormatter(money)


    #Store data and create a blank series to use for the waterfall
    trans, blank = create_trans_blank(index_names,data)

    #Get the net total number for the final element in the waterfall
    process_net(calc_total,total,trans,blank,final_sum_name)
    
    #The steps graphically show the levels as well as used for label placement   
    step = process_step(final_line,blank)
    
    #When plotting the last element, we want to show the full bar,
    #Set the blank to 0
    if(calc_total or total!=None):
        blank.loc["net"] = 0

    color = [np.where(trans["amount"]>=0, 'g', 'r')]
    color[0][-1]='b'
    #Plot and label
    my_plot = trans.plot(kind='bar', stacked=True, color=color, bottom=blank,legend=None, figsize=(10, 5), title=title)
    my_plot.plot(step.index, step.values,'k')
    my_plot.set_xlabel("Transactions")

    #Format the axis for the current format chosen
    my_plot.yaxis.set_major_formatter(formatter)

    #Get the y-axis position for the labels
    y_height = trans.amount.cumsum().shift(1).fillna(0)
    if(total!=None):
        y_height.loc[final_sum_name]=total

    #Get an offset so labels don't sit right on top of the bar
    maximum = trans.max()
    neg_offset = maximum / 25
    pos_offset = maximum / 50
    plot_offset = int(maximum / 15)

    #Start label loop
    loop = 0
    for index, row in trans.iterrows():
        # For the last item in the list, we don't want to double count
        if row['amount'] == total:
            y = y_height[loop]
        else:
            y = y_height[loop] + row['amount']
        # Determine if we want a neg or pos offset
        if row['amount'] > 0:
            y += pos_offset
        elif row['amount'] == total:
            y = total
        else:
            y -= neg_offset
        my_plot.annotate((prefix+"{:,.0f} "+suffix).format(row['amount']),(loop,y),ha="center")
        loop+=1
    
    red_patch = mpatches.Patch(color='red', label='Negative')
    green_patch = mpatches.Patch(color='green', label='Positive')
    if(not calc_total and total==None):
        my_plot.legend(handles=[red_patch,green_patch])
    else:
        blue_patch = mpatches.Patch(color='blue', label='Final')
        my_plot.legend(handles=[red_patch,green_patch,blue_patch])
    #Scale up the y axis so there is room for the labels
    my_plot.set_ylim(0,blank.max()+int(plot_offset))
    #Rotate the labels
    my_plot.set_xticklabels(trans.index,rotation=0)
    print(my_plot.get_figure())
    if(output):
        my_plot.get_figure().savefig("waterfall.png",dpi=400,bbox_inches='tight')
    #credits for initial code: https://pbpython.com/waterfall-chart.html