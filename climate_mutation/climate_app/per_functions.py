import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
import io
from PIL import Image,ImageDraw
import base64


def ozone_per(request):
       if not request.session.has_key('email'):
          return redirect('login')
       else:
        country=request.POST.get('countries')
        years=int(request.POST.get('num'))
       
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
 
        data=pd.read_csv('datasets/consumpozone.csv',parse_dates=['Year'])
        data_by_country=data[data['Entity']== country]
        cols=data_by_country.iloc[:,2:]
        if cols['ozoneconsumption'].isnull().sum() != 0:
          cols['ozoneconsumption']=cols['ozoneconsumption'].fillna(value=cols['ozoneconsumption'].mean())
        year_as_index=cols.set_index('Year')
        year_as_index.index = pd.DatetimeIndex(year_as_index.index).to_period('y')

        mod = sm.tsa.statespace.SARIMAX(year_as_index,
                                 order=(10, 1, 1),
                                 seasonal_order=(0, 0, 0, 0),
                                 enforce_stationarity=True,
                                 enforce_invertibility=False)
        results = mod.fit() 
        
        pred_uc = results.get_forecast(steps=years)
        pred_ci = pred_uc.conf_int()
        ax = year_as_index['1990':].plot()
        pred_uc.predicted_mean.plot(ax=ax)
        ax.fill_between(pred_ci.index,
                         pred_ci.iloc[:, 0],
                         pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.legend(['observed','forecast'])                 
         
        
        buf = io.BytesIO()
        plt.ylabel('''Ozone Consumption 
 (million tonnes)''')
        plt.xlabel('years')
        plt.title(f'Ozone Consumption for next {years} years',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
    # Tweak spa
    # Tweak spacing to prevent clipping of tick-labels
       
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        #draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic


def air_pol_per(request):
       if not request.session.has_key('email'):
          return redirect('login')
       else:
        country=request.POST.get('countries')
        cause=request.POST.get('cause')
        years=int(request.POST.get('num'))
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
 
        data=pd.read_csv('datasets/air_pollution_deaths_per.csv',parse_dates=['Year'])
        data_by_country=data[data['Entity']== country]
        air_pollution=data_by_country.loc[:,['Year',cause]]
        if air_pollution[cause].isnull().sum() != 0:
             air_pollution[cause]=air_pollution[cause].fillna(value=air_pollution[cause].mean())
        year_as_index=air_pollution.set_index('Year')
        year_as_index.index = pd.DatetimeIndex(year_as_index.index).to_period('y')
      
        mod = sm.tsa.statespace.SARIMAX(year_as_index,
                                 order=(5, 1, 1),
                                 seasonal_order=(0, 0, 0, 0),
                                 enforce_stationarity=True,
                                 enforce_invertibility=False)
        results = mod.fit() 
        
        pred_uc = results.get_forecast(steps=years)
        pred_ci = pred_uc.conf_int()
        ax = year_as_index['1950':].plot()
        pred_uc.predicted_mean.plot(ax=ax)
        ax.fill_between(pred_ci.index,
                         pred_ci.iloc[:, 0],
                         pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.legend(['observed','forecast'])                 
   
  
        buf = io.BytesIO()
        plt.ylabel(f'''Deaths
        {cause}''')
        plt.xlabel('years')
        plt.title(f'Deaths in {country} next {years} years',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
    # Tweak spa
    # Tweak spacing to prevent clipping of tick-labels
       
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        #draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic


def nt_em_per(request):
       if not request.session.has_key('email'):
          return redirect('login')
       else:
        country=request.POST.get('countries')
        years=int(request.POST.get('num'))
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
 
        data=pd.read_csv('datasets/nitrous_oxide_emissions_million_t.csv',parse_dates=['Year'])
        data_by_country=data[data['Entity']== country]
        cols=data_by_country.iloc[:,2:]
        if cols['Total including LUCF'].isnull().sum() != 0:
            cols['Total including LUCF']=cols['Total including LUCF'].fillna(value=cols['Total including LUCF'].mean())
    
        year_as_index=cols.set_index('Year')

        year_as_index.index = pd.DatetimeIndex(year_as_index.index).to_period('y')
      
        mod = sm.tsa.statespace.SARIMAX(year_as_index,
                                 order=(10, 1, 1),
                                 seasonal_order=(0, 0, 0, 0),
                                 enforce_stationarity=True,
                                 enforce_invertibility=False)
        results = mod.fit() 
        
        pred_uc = results.get_forecast(steps=years)
        pred_ci = pred_uc.conf_int()
        ax = year_as_index['1950':].plot()
        pred_uc.predicted_mean.plot(ax=ax)
        ax.fill_between(pred_ci.index,
                         pred_ci.iloc[:, 0],
                         pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.legend(['observed','forecast'])                 
        plt.ylabel('''Nitrous dioxide emissions''')
        plt.xlabel('years')
        plt.title(f'Nitrous Dioxide Emissions of {country} for next {years} years',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
    # Tweak spacing to prevent clipping of tick-labels
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
  
        
       
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        #draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic
def mth_em_per(request):
       if not request.session.has_key('email'):
          return redirect('login')
       else:
        country=request.POST.get('countries')
        years=int(request.POST.get('num'))
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
 
        data=pd.read_csv('datasets/methane_emissions_million_t.csv',parse_dates=['Year'])
        data_by_country=data[data['Entity']== country]
        cols=data_by_country.iloc[:,2:]
        if cols['Total including LUCF'].isnull().sum() != 0:
            cols['Total including LUCF']=cols['Total including LUCF'].fillna(value=cols['Total including LUCF'].mean())
    
        year_as_index=cols.set_index('Year')

        year_as_index.index = pd.DatetimeIndex(year_as_index.index).to_period('y')
      
        mod = sm.tsa.statespace.SARIMAX(year_as_index,
                                 order=(10, 1, 1),
                                 seasonal_order=(0, 0, 0, 0),
                                 enforce_stationarity=True,
                                 enforce_invertibility=False)
        results = mod.fit() 
        
        pred_uc = results.get_forecast(steps=years)
        pred_ci = pred_uc.conf_int()
        ax = year_as_index['1950':].plot()
        pred_uc.predicted_mean.plot(ax=ax)
        ax.fill_between(pred_ci.index,
                         pred_ci.iloc[:, 0],
                         pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.legend(['observed','forecast'])                 
           
  
        buf = io.BytesIO()
        plt.ylabel('''Methane emissions''')
        plt.xlabel('years')
        plt.title(f'Methane Emissions of {country} for next {years} years',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
    # Tweak spacing to prevent clipping of tick-labels
        
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        #draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic

def co2_em_per(request):
       if not request.session.has_key('email'):
          return redirect('login')
       else:
        country=request.POST.get('countries')
        years=int(request.POST.get('num'))
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
 
        data=pd.read_csv('datasets/annualco2.csv',parse_dates=['Year'])
        data_by_country=data[data['Entity']== country]
        cols=data_by_country.iloc[:,2:]
        if cols['Annual_CO2_emissions'].isnull().sum() != 0:
            cols['Annual_CO2_emissions']=cols['Annual_CO2_emissions'].fillna(value=cols['Annual_CO2_emissions'].mean())
    
        year_as_index=cols.set_index('Year')

        year_as_index.index = pd.DatetimeIndex(year_as_index.index).to_period('y')
      
        mod = sm.tsa.statespace.SARIMAX(year_as_index,
                                 order=(10, 1, 1),
                                 seasonal_order=(0, 0, 0, 0),
                                 enforce_stationarity=True,
                                 enforce_invertibility=False)
        results = mod.fit() 
        
        pred_uc = results.get_forecast(steps=years)
        pred_ci = pred_uc.conf_int()
        ax = year_as_index['1950':].plot()
        pred_uc.predicted_mean.plot(ax=ax)
        ax.fill_between(pred_ci.index,
                         pred_ci.iloc[:, 0],
                         pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.legend(['observed','forecast'])                 
   
  
        buf = io.BytesIO()
        plt.ylabel('''Carbon dioxide emissions''')
        plt.xlabel('years')
        plt.title(f'Carbon Dioxide Emissions of {country} for next {years} years',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
    # Tweak spacing to prevent clipping of tick-labels
        
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        #draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic

def gb_eth_per(request):
       if not request.session.has_key('email'):
          return redirect('login')
       else:
        temp=request.POST.get('temp')
        years=int(request.POST.get('num'))
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
 
        data=pd.read_csv('datasets/earth_global_temperature_incelsius.csv',parse_dates=['dt'])
        data1=data.loc[:,['dt',temp]]
        data1=data1.fillna(value=data1[temp].mean())
        data1.isnull().sum()
        data1=data1.set_index('dt')
        # data1.index = pd.DatetimeIndex(data1.index).to_period('y')
      
        mod = sm.tsa.statespace.SARIMAX(data1,
                                 order=(10, 1, 1),
                                 seasonal_order=(0, 0, 0, 0),
                                 enforce_stationarity=True,
                                 enforce_invertibility=False)
        results = mod.fit() 
        
        pred_uc = results.get_forecast(steps=years)
        pred_ci = pred_uc.conf_int()
        ax = data1['2000':].plot()
        pred_uc.predicted_mean.plot(ax=ax)
        ax.fill_between(pred_ci.index,
                         pred_ci.iloc[:, 0],
                         pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.legend(['observed','forecast'])                 
        plt.xlabel('years')
        plt.ylabel(f'{temp}')
        plt.title(f'{temp} perdiction for next {years} years',pad=50)
        plt.xticks(rotation=90)
        plt.tight_layout() 
  
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        #draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic
def un_wt_per(request):
       if not request.session.has_key('email'):
          return redirect('login')
       else:
        country=request.POST.get('countries')
        years=int(request.POST.get('num'))
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
 
        data=pd.read_csv('datasets/deaths_unsafe_water.csv',parse_dates=['Year'])
        data_by_country=data[data['Entity']== country]
        cols=data_by_country.iloc[:,2:]
        if cols['deaths'].isnull().sum() != 0:
            cols['deaths']=cols['deaths'].fillna(value=cols['deaths'].mean())
        
        year_as_index=cols.set_index('Year')
        year_as_index.index = pd.DatetimeIndex(year_as_index.index).to_period('y')
      
        mod = sm.tsa.statespace.SARIMAX(year_as_index,
                                 order=(10, 1, 1),
                                 seasonal_order=(0, 0, 0, 0),
                                 enforce_stationarity=True,
                                 enforce_invertibility=False)
        results = mod.fit() 
        
        pred_uc = results.get_forecast(steps=years)
        pred_ci = pred_uc.conf_int()
        ax = year_as_index['2000':].plot()
        pred_uc.predicted_mean.plot(ax=ax)
        ax.fill_between(pred_ci.index,
                         pred_ci.iloc[:, 0],
                         pred_ci.iloc[:, 1], color='k', alpha=.25)
        ax.legend(['observed','forecast'])  
        plt.xlabel('years')
        plt.ylabel('Deaths')
        plt.title(f'Deaths perdiction in {country} for next {years} years',pad=50)
        plt.xticks(rotation=90)
        plt.tight_layout()                
       
  
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
       
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        #draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic

       