# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:44:13 2021

@author: wangwy
"""

import pandas as pd
import pygal
import pycountry_convert as pc

def country_to_code(country):
    try:
        return pc.country_name_to_country_alpha2(country).lower()
    except:
        #print(str(country) + " is not a country.")
        return

def create_chart(year):
    df = pd.read_csv("export.csv")
    df = df.fillna(0)
    display(df)
    #df.rename( columns={'Unnamed: 0':'Country'}, inplace=True )
    #large = max(df[str(year)])
    #print(large)
    #df["Total"] = df["Total"].apply(lambda x: 100*x/large)
    df["COUNTRY NAME"] = df["COUNTRY NAME"].apply(country_to_code)
    df.dropna()
    #display(df)
    df = df[df["YEAR"] == year]
    #display(df)
    data = dict(zip(df["COUNTRY NAME"], df["VALUE"]))
    #print(data)
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Agriculture in ' + str(year)
    worldmap_chart.add("Total", data)
    #worldmap_chart.render_in_browser()
    worldmap_chart.render_to_file("static/maps/agriculture/" + str(year)+".svg")
    return worldmap_chart
 
for i in range(2001, 2017):
    create_chart(i)
