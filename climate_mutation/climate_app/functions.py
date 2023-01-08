import matplotlib.pyplot as plt
import matplotlib
#import gmplot
from io import BytesIO
import io
import base64
matplotlib.use('Agg')

import plotly.express as px
import pandas as pd
import seaborn as sns
from PIL import Image,ImageDraw
import os
from django.conf import settings
from django.shortcuts import redirect

def top_ozone(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        year=int(request.POST.get('year'))
        top_values=int(request.POST.get('num'))
        print(year)
        print(top_values)
        fig=plt.figure(figsize=(6, 7), dpi=500,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/consumpozone.csv')
        year_wise=data[data["Year"]==year]
        sorted_year_desc=year_wise.sort_values(by=["ozoneconsumption"],ascending=False)
        print(sorted_year_desc)
        top=sorted_year_desc[:top_values]
#top
        sns.barplot(data=top,x="Entity",y="ozoneconsumption")
        buf = io.BytesIO()
        plt.xlabel('Countries')
        plt.ylabel('''Ozone Consumption 
 (million tonnes)''')
        plt.title(f'Top Consumption of Ozone in Year {year} for {top_values} Countries',pad=70)
        plt.xticks(rotation=90)
        plt.tight_layout()
    
    # Tweak spacing to prevent clipping of tick-labels
        
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.5)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic


def ozone_comparisons(request):  
     if not request.session.has_key('email'):
       raise http403          
     else:
        year1=int(request.POST.get('year1'))
        year2=int(request.POST.get('year2'))
        countries=request.POST.getlist('countries')

        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/consumpozone.csv')
       
        data3=data[data['Entity'].isin(countries)]
        deaths3=data3[(data3["Year"]>=year1) & (data3["Year"]<=year2)]
        sns.barplot(data=deaths3,x='Year',y='ozoneconsumption',hue="Entity")
        plt.xlabel('years')
        plt.ylabel('''Ozone Consumption 
 (million tonnes)''')
        plt.title(f'Ozone Consumption from {year1} to {year2}',pad=70)
        plt.legend(bbox_to_anchor=(1.3, 1.8), loc="upper right")
        plt.xticks(rotation=90)
        plt.tight_layout()
      
        buf = io.BytesIO()
       
     # Tweak spacing to prevent clipping of tick-labels
      
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic  
# def least_ozone(request):
#     if not request.session.has_key('email'):
#         raise http403
#     else:
#         year=int(request.POST.get('year'))
#         top_values=int(request.POST.get('num'))
#         print(year)
#         print(top_values)
#         fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
#         matplotlib.rcParams['axes.labelsize'] = 14
#         matplotlib.rcParams['xtick.labelsize'] = 8
#         matplotlib.rcParams['ytick.labelsize'] = 12
#         matplotlib.rcParams['text.color'] = 'k'
#         data = pd.read_csv('datasets/consumpozone.csv')
#         year_wise=data[data["Year"]==year]
#         sorted_year_asc=year_wise.sort_values(by=["ozoneconsumption"])
#         print(sorted_year_asc)
#         least=sorted_year_asc[:top_values]
#         sns.barplot(data=least,x="Entity",y="ozoneconsumption")
#         buf = io.BytesIO()
#         plt.margins(0.8)
#     # Tweak spacing to prevent clipping of tick-labels
#         plt.subplots_adjust(bottom=0.35)
#         plt.xticks(rotation=90)
#         plt.savefig(buf, format='png')
   
#         fig.savefig('abc.png')
    
#         plt.close(fig)
#         image = Image.open("abc.png")
#         draw = ImageDraw.Draw(image)
    
#         image.save(buf, 'PNG')
#         content_type="Image/png"
#         buffercontent=buf.getvalue()


#         graphic = base64.b64encode(buffercontent) 
#         return graphic

def ozone_yearly(request):
    if not request.session.has_key('email'):
       raise http403
    else:
        year1=int(request.POST.get('year1'))
        year2=int(request.POST.get('year2'))
        print(year1)
        print(year2)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/consumpozone.csv')
        yearly=data[(data["Year"]>=year1) & (data["Year"]<=year2)]
        print(yearly)
        sns.lineplot(data=yearly,x='Year',y='ozoneconsumption')
        buf = io.BytesIO()
        plt.xlim([year1,year2])
        plt.ylabel('''Ozone Consumption 
 (million tonnes)''')
        plt.title(f'Ozone Consumption from {year1} to {year2}',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
    # Tweak spacing to prevent clipping of tick-labels
        
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic

           

def least_ozone(request):
    if not request.session.has_key('email'):
        raise http403   #forbidden code
    else:
        year=int(request.POST.get('year'))
        top_values=int(request.POST.get('num'))
        print(year)
        print(top_values)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/consumpozone.csv')
        year_wise=data[data["Year"]==year]
        sorted_year_asc=year_wise.sort_values(by=["ozoneconsumption"])
        print(sorted_year_asc)
        
        greater_than_zero=sorted_year_asc[sorted_year_asc['ozoneconsumption']>0]
        least=greater_than_zero[:top_values]
        sns.barplot(data=least,x="Entity",y="ozoneconsumption")
        plt.xlabel('Countries')
        plt.ylabel('Ozone Consumption in million tonne')
        plt.title(f'Least Consumption of Ozone in Year {year} for {top_values} Countries',pad=50)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.ylim(0.0,0.2)
        buf = io.BytesIO()
        

       # plt.margins(0.3)
    # # Tweak spacing to prevent clipping of tick-labels
       #  plt.subplots_adjust(bottom=0.35)
    #     plt.gca().set_axis_off()
        #plt.subplots_adjust(top = 1, bottom = 1, right = 1, left = 1, 
         #   hspace = 1, wspace = 1)
    #     plt.margins(0,0)  
                                
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.5)
        plt.close(fig)
   
        fig.savefig('abc.png')
    
        
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        
        return graphic

def land_temp_yearly(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        year1=int(request.POST.get('year1'))
        year2=int(request.POST.get('year2'))
        radio_input=request.POST.get('temp')
        print(year1)
        print(year2)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/earth_global_temperature_incelsius.csv')
        data.drop(data.columns[[2,4,6,8]],axis=1,inplace=True)
        data['LandAverageTemperature'].fillna(data['LandAverageTemperature'].mean(),inplace=True)
        data.dropna(inplace=True)
        data.reset_index(drop=True,inplace=True)
        date=pd.to_datetime(data["dt"])
        data["year"]=date.dt.year
        data["month"]=date.dt.month
        dt_data=data[(data["year"]>=year1) & (data["year"]<=year2) ]
        if radio_input=="LandAverageTemperature":
           sns.lineplot(data=dt_data,x="year",y="LandAverageTemperature")
           #sns.barplot(data=dt_data,x="year",y="LandAverageTemperature")
        elif radio_input=="LandMaxTemperature":
           sns.lineplot(data=dt_data,x="year",y="LandMaxTemperature")
           #sns.barplot(data=dt_data,x="year",y="LandMaxTemperature")
        elif radio_input=="LandMinTemperature":   
           sns.lineplot(data=dt_data,x="year",y="LandMinTemperature")
           #sns.barplot(data=dt_data,x="year",y="LandMinTemperature")
        elif radio_input=="LandAndOceanAverageTemperature":
           sns.lineplot(data=dt_data,x="year",y="LandAndOceanAverageTemperature")
           #sns.barplot(data=dt_data,x="year",y="LandAndOceanAverageTemperature")
        else:
            return None
            

        buf = io.BytesIO()
        plt.xlabel('Years')
        plt.ylabel(f'{radio_input}')
        plt.title(f'{radio_input}  from Year {year1} to {year2}',pad=50)
        plt.xticks(rotation=90)
        plt.tight_layout()
        
       
    # Tweak spacing to prevent clipping of tick-labels
        
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic
        
           

def all_gases_cmp(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/air_pollution_deaths.csv')
        df1=data.set_index('Year')
        a=sns.lineplot(data=df1)
        a.set(ylabel="number of deaths")
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic

def country_year_deaths(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        year=int(request.POST.get('year'))
        country=request.POST.get('countries')
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/air_pollution_deaths.csv')
        df0=data[data['Year']==year]
        one_country=df0[df0["Entity"]==country]
        one_country=one_country.drop(['Year'],axis=1)
        p=sns.barplot(data=one_country)
        
        buf = io.BytesIO()
        plt.ylabel('''Number of deaths''')
        plt.xlabel('Causes')
        plt.title(f'Deaths in {country} in {year} year',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
        
      
    # Tweak spacing to prevent clipping of tick-labels
        
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic

def air_max_min_death_top_country(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        year=int(request.POST.get('year'))
        number=int(request.POST.get('num'))
        order=request.POST.get('order')
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data = pd.read_csv('datasets/air_pollution_deaths.csv')
        df1=data[data['Year']==year]
        if order=='maximum':
          country=df1.sort_values(by=['by_all_causes'],ascending=False)
        else:
          country=df1.sort_values(by=['by_all_causes'])

        top=country[:number]
        top_countries=sns.barplot(data=top,x="Entity",y="by_all_causes")
#top 
        top_countries.set_title(f'{order} {number} countries of death by harmful gases in {year}',pad=70)
        buf = io.BytesIO()
        plt.ylabel('Deaths')
        plt.xlabel('Countries')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
       
   
    
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic
def deaths_onecountry_year_cause(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        year1=int(request.POST.get('year1'))
        year2=int(request.POST.get('year2'))
        country=request.POST.get('countries')
        cause=request.POST.get('cause')
        
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        df= pd.read_csv('datasets/air_pollution_deaths.csv')
        
        df=df[df['Entity']==country]
        if not year1==year2:
            yearly=df[(df['Year']>=year1) & (df['Year']<=year2)]
        else:
            yearly=df[df['Year']==year1]    
        if not cause==None:
            yearly=yearly.loc[:,['Entity','Year',cause]]
        yearly=yearly.set_index('Year')
        if not year1==year2:
            p=sns.lineplot(data=yearly)
        else:
            p=sns.barplot(data=yearly)
        p.set_title('Deaths in '+ country + 'for year '+str(year1)+" to "+str(year2)+" by "+ cause,pad=70)
        p.set(ylabel='Deaths')

        buf = io.BytesIO()
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic        
def deaths_countries_year_cause(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        year1=int(request.POST.get('year1'))
        year2=int(request.POST.get('year2'))
        countries=request.POST.getlist('countries')
        cause=request.POST.get('cause')
        
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 20
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        df= pd.read_csv('datasets/air_pollution_deaths.csv')
        
        df=df[df['Entity'].isin(countries)]
        if not year1==year2:
            yearly=df[(df['Year']>=year1) & (df['Year']<=year2)]
        else:
            yearly=df[df['Year']==year1]    
        
        if not cause==None and not year1==year2:
            sns.lineplot(data=yearly,x='Year',y=cause,hue='Entity')
        elif year1==year2 and not cause==None:
            sns.barplot(data=yearly,x='Year',y=cause,hue='Entity')
        else:
            sns.barplot(data=yearly,x='Year',y='by_all_causes',hue='Entity')

        # if cause==None :    
        #      

        buf = io.BytesIO()
        plt.ylabel('Deaths')
        plt.xlabel('years')
        plt.title(f'Deaths in countries from {year1} to {year2} by {cause}',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic           
def air_max_deaths_cause_or_cn(request):
    if not request.session.has_key('email'):
       raise http403
    else:
        country=request.POST.get('countries')
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        df= pd.read_csv('datasets/air_pollution_deaths.csv')
        if country==None:
            df2=df.drop("by_all_causes",axis=1)
            df2=pd.DataFrame(df2.iloc[:,3:].mean()).reset_index()
            df2=df2.rename(columns=({'index':'causes',0:'values'}))
            p=sns.barplot(data=df2,x='causes',y='values')
            p.set_title('maximun deaths in all years due to different causes' ,pad=70)
            p.set(ylabel='deaths')
        if not country==None:
            df3=df[df['Entity']==country]
            df3=df3.drop("by_all_causes",axis=1)
            df3=pd.DataFrame(df3.iloc[:,3:].mean()).reset_index()
            df3=df3.rename(columns=({'index':'causes',0:'values'}))
            p=sns.barplot(data=df3,x='causes',y='values')
            p.set_title(f'maximun deaths in {country} due to different causes',pad=70)
            p.set(ylabel='deaths')
        buf = io.BytesIO()
     
      
        
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
    
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic                   

def water_deaths_all_years_range_country(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        if not request.method=='GET':
          year1=int(request.POST.get('year1'))
          year2=int(request.POST.get('year2'))
        country=request.POST.get('countries')
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 20
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data=pd.read_csv('datasets/deaths_unsafe_water.csv')
        if country==None:
            data1=data.set_index("Year")
            p1=sns.lineplot(data=data1)
            p1.set_title("Yearly % comparison of deaths from unsafe water")
        else:     
            by_country=data[data["Entity"]==country]
            deaths=by_country[(by_country["Year"]>=year1) & (by_country["Year"]<=year2)]
            p=sns.lineplot(data=deaths,x="Year",y="deaths")
           
        buf = io.BytesIO()
        plt.ylabel('Deaths')
        plt.xlabel('years')
        plt.title(f'Deaths from {year1} to {year2} in {country}',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
   
     
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic   

def water_deaths_cmp_countries_range(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        
        year1=int(request.POST.get('year1'))
        year2=int(request.POST.get('year2'))
        countries=request.POST.getlist('countries')
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 16
        matplotlib.rcParams['xtick.labelsize'] = 15
        matplotlib.rcParams['ytick.labelsize'] = 20
        matplotlib.rcParams['text.color'] = 'k'
        data=pd.read_csv('datasets/deaths_unsafe_water.csv')
        data3=data[data['Entity'].isin(countries)]
        deaths3=data3[(data3["Year"]>=year1) & (data3["Year"]<=year2)]
        sns.barplot(data=deaths3,x='Year',y='deaths',hue="Entity")
        buf = io.BytesIO()
        plt.ylabel('Deaths')
        plt.xlabel('years')
        plt.title(f'Deaths in countries from {year1} to {year2}',pad=70)
        
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.3)
  
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return graphic   

def co2_graph(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        buffer = io.StringIO()
        co2data=pd.read_csv('datasets/annualco2.csv')
        fig = px.choropleth(co2data, locations="Code",
                    color="Annual_CO2_emissions",
                    hover_name="Entity",
                    animation_frame="Year",
                    title = "co2 plotted using Plotly",color_continuous_scale=px.colors.sequential.Plasma)
        
        fig.write_html(settings.TEMPLATE_DIR+'/graph.html')
       
         

def methane_graph(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
       
        methane_data=pd.read_csv('datasets/methane_emissions_million_t.csv')
        fig = px.choropleth(methane_data, locations="Code",
                    color="Total including LUCF",
                    hover_name="Entity",
                    animation_frame="Year",
                    title = "methane analysis",color_continuous_scale=px.colors.sequential.Blackbody_r)
        
        fig.write_html(settings.TEMPLATE_DIR+'/graph.html')        


def no2_graph(request):
    if not request.session.has_key('email'):
        raise http403
    else:
        
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
       
        no2_data=pd.read_csv('datasets/nitrous_oxide_emissions_million_t.csv')
        fig = px.choropleth(no2_data, locations="Code",
                    color="Total including LUCF",
                    hover_name="Entity",
                    animation_frame="Year",
                    title = "nitrous oxide analysis",color_continuous_scale=px.colors.sequential.Sunsetdark_r)
        
        fig.write_html(settings.TEMPLATE_DIR+'/graph.html') 