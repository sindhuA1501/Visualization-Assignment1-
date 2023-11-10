#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 20:54:07 2023
@author: Sindhu Kavya Alahari

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_and_show_line_plot(x_data,y_data,graphLabel,label_x,label_y,ticks_x,graphTitle,ticks_y):
    """
        Create and display a line or scatter plot.

        Parameters:
        - plotName (str): Specifies the type of plot ('line' or 'scatter').
        - x_data (list): X-axis data (e.g., month numbers).
        - y_data (list): Y-axis data (e.g., profit or sales data).
        - graphLabel (str): Label for the plot.
        - label_x (str): Label for the X-axis.
        - label_y (str): Label for the Y-axis.
        - ticks_x (list): List of tick locations for the X-axis.
        - graphTitle (str): Title of the graph.
        - ticks_y (list): List of tick locations for the Y-axis (can be None for automatic).

        Returns:
        - None"""
    for i,j in zip(y_data,graphLabel):
        plt.plot(x_data,i,label=j,marker='o', linewidth=3)
    plt.legend(loc='upper left')
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.xticks(ticks_x)
    plt.title(graphTitle)
    plt.yticks(ticks_y)
    plt.show()
    return

def create_and_show_scatter_plot(x_data,y_data,graphLabel,label_x,label_y,ticks_x,graphTitle,ticks_y):
    """
        Create and display a scatter plot.

        Parameters:
        - x_data: Data for the x-axis.
        - y_data: Data for the y-axis.
        - graph_label: Label for the data in the legend.
        - label_x: Label for the x-axis.
        - label_y: Label for the y-axis.
        - ticks_x: Tick positions for the x-axis.
        - graph_title: Title for the graph.
        - ticks_y: Tick positions for the y-axis.

        Returns:
        None
        """
    plt.scatter(x_data, y_data, label=graphLabel)
    plt.legend(loc='upper left')
    plt.grid(True, linewidth= 1, linestyle="--")
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.xticks(ticks_x)
    plt.title(graphTitle)
    plt.yticks(ticks_y)
    plt.show()
    return

def create_and_show_pie_chart(data,labels,title):
    """
        Create and display a pie chart.

        Parameters:
        - data (list): Data for creating the pie chart (e.g., sales data for different products).
        - labels (list): Labels for the pie chart segments.
        - title (str): Title of the pie chart.

        Returns:
        - None
        """
    plt.axis("equal")
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.legend(loc='lower right')
    plt.title(title)
    plt.show()
    return


#loading dataset using pandas
dataFrame = pd.read_csv('Sales_data.csv')

#Data Preparation
profitList = dataFrame['total_profit'].tolist()
monthList = dataFrame['month_number'].tolist()
health = dataFrame['health'].tolist()
beauty = dataFrame['beauty'].tolist()
electronicAccessories = dataFrame['electronicAccessories'].tolist()
home = dataFrame['home'].tolist()
lifestyle = dataFrame['lifestyle'].tolist()
sports = dataFrame['sports'].tolist()

linePlotY_data = [health,beauty,electronicAccessories,home,lifestyle,sports]
lineGraphLabels = ['health items sales','beauty sales', 'electronic accessories sales',
                   'home items sales', 'lifestyle sales', 'sports sales']

Y = [1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000]
ChartLabels = ['health', 'beauty', 'electronicAccessories', 'home', 'lifestyle', 'sports']

salesData = [dataFrame[label].sum() for label in ChartLabels]

#Line plot
create_and_show_line_plot(monthList,linePlotY_data,lineGraphLabels,'Month','sales units in number',monthList,
     'salesData',Y)

#Scatter plot
create_and_show_scatter_plot(monthList,electronicAccessories,'Sales data of Electronic Accessories','Month','No.of units sold',
     monthList,'Sales Data Of Electronic Accessories',None)

#pie plot
create_and_show_pie_chart(salesData,labels=ChartLabels,title='Sales Data')





