import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

data=pd.read_csv('immo_data.csv')
df=pd.DataFrame(data)
df=df.drop([
    'baseRentRange','telekomUploadSpeed','pricetrend','street','livingSpaceRange',
    'houseNumber','petsAllowed','facilities','condition','noRoomsRange','interiorQual',
    'streetPlain','geo_bln','scoutId','picturecount','description','electricityBasePrice',
    'electricityKwhPrice','energyEfficiencyClass','lastRefurbish','telekomTvOffer',
    'telekomHybridUploadSpeed'
], axis=1)

df_cleand=df.dropna(subset=['totalRent']) #Leere Zeilen für die Gesamtmiete wurden gelöscht, um eine genauere Analyse zu erhalten.
df_cleand=df_cleand[(df_cleand['totalRent']<5000) & (df_cleand['livingSpace']<500) & (df_cleand['totalRent']!=0) &(df_cleand['livingSpace']!=0)]
df_hochmiet=df_cleand[(df_cleand['totalRent']>=5000) | (df_cleand['livingSpace']>=500)]
durchschnitt=(df_hochmiet['date'].count()/df_cleand['date'].count())*100 
df_cleand['regio1'] = df_cleand['regio1'].str.replace('_', ' ')
#der Durchschnitt ist 0.134.deswegen filtere ich die Daten, bei denen die Miete unter 5000 Euro liegt.







def gesamtzahlnachBundesland():

    result=df_cleand[['regio1','date']].groupby(['regio1']).count().sort_values(by='date', ascending=False)
    
    plt.bar(np.arange(0.25, (len(result)/2), 0.5), result['date'], width=0.20, color='r')
    plt.xticks(np.arange(0.25, (len(result)/2), 0.5), result.index, rotation=90)

    plt.xlabel('Bundesländer')
    plt.ylabel('Gesamtzahl der Mietwohnungen')
    plt.title('Gesamtzahl der Mietwohnungen nach Bundesland')
    plt.tight_layout()
    plt.show()


def durchschinitlichMietnachBundesland():

    durchschinitlich_miet_list=df_cleand[['regio1','totalRent']].groupby('regio1')['totalRent'].mean()
    result=pd.DataFrame(durchschinitlich_miet_list)

    plt.figure(figsize=(12, 8)) 
    plt.plot(result.index, result['totalRent'], color='r')
    plt.xticks(result.index, rotation=90)
    plt.xlabel('Bundesländer')
    plt.ylabel('Durchschnittliche Miete (€)')
    plt.title('Durchschnittliche Miete nach Bundesland')
    plt.tight_layout()
    plt.show()
    

def durchschinttlichMietenachMerkmale():

    neudata=df_cleand[['regio1','cellar','garden','balcony','lift','totalRent','newlyConst']]
    neudata['feature_count'] = neudata[['cellar', 'garden', 'balcony', 'lift','newlyConst']].sum(axis=1)
    neudata=neudata.groupby(['regio1', 'feature_count'])['totalRent'].mean().reset_index()

    pivot_tbl=neudata.pivot_table(index='regio1', columns='feature_count', values='totalRent') 

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_tbl, annot=True, fmt=".0f", cmap='YlOrRd')
    plt.title('Durchschnittliche Miete nach Bundesland und Anzahl der Merkmale')
    plt.xlabel('Anzahl der Merkmale (Keller, Garten, Balkon, Aufzug, Neubau)')
    plt.ylabel('Bundesländer')
    plt.tight_layout()
    plt.show()

def zahlderMietwohnung():
    group_bundesland=df_cleand[['regio1','totalRent']].groupby('regio1')

    with PdfPages('Histogramm-Diagramm.pdf') as pdf:
        for name, veri in group_bundesland:

            plt.figure(figsize=(10, 6)) 

            plt.hist(veri['totalRent'], bins=150, color='skyblue', edgecolor='black')

            max_miete = veri['totalRent'].max()
            plt.xticks(np.arange(0, max_miete + 250, 250))


            plt.xlabel(name)
            plt.title('Der Zahl der Mietwohnungen nach Bundesland')
            plt.tight_layout()

            pdf.savefig() 
            plt.close() 

        plt.figure(figsize=(12, 8))  
        df_cleand['regio1'] = df_cleand['regio1'].str.replace('_', ' ')
        sns.boxplot(x='regio1', y='totalRent', data=df_cleand, order=df_cleand['regio1'])
        
        plt.xticks(rotation=90,fontsize=9)
        plt.yticks(np.arange(0, 5500, 500),fontsize=10)
        plt.xlabel('Bundesländer')
        plt.ylabel('Gesamtmiete (€)')
        plt.title('Verteilung der Mieten (Boxplot) nach Bundesland')

        plt.tight_layout()
        pdf.savefig() 
        

    import webbrowser
    webbrowser.open("Histogramm-Diagramm.pdf")



def mietenachLivingspace():
    df_cleand['price_per_m2'] = df_cleand['totalRent'] / df_cleand['livingSpace']
    group_bundesland=df_cleand.groupby('regio1')

    with PdfPages('Scatterplot-Diagramm.pdf') as pdf:
        for name, veri in group_bundesland:

            plt.figure(figsize=(8, 6)) 
            sns.scatterplot(x='livingSpace', y='totalRent', data=veri, alpha=0.3)

            plt.ylabel('Gesamtmiete (€)')
            
            max_miete = veri['totalRent'].max()
            plt.yticks(np.arange(0, max_miete + 250, 250))

            max_livingspace=veri['livingSpace'].max()
            plt.xlabel(name)
            plt.xticks(np.arange(0, max_livingspace+50, 50))

            plt.title('Zusammenhang zwischen Wohnfläche und Gesamtmiete')
            plt.tight_layout()

            pdf.savefig() 
            plt.close() 

        
        avrg_m2price=group_bundesland['price_per_m2'].mean().sort_values(ascending=False)

        plt.figure(figsize=(8, 6))
        avrg_m2price.plot(kind='bar', color='orange')
        plt.xticks(rotation=90, fontsize=8)
        plt.ylabel('Durchschnittlicher Preis pro m² (€)')
        plt.xlabel('Bundesländer')
        plt.title('Durchschnittlicher m²-Preis nach Bundesland')
        plt.tight_layout()
        pdf.savefig()
    import webbrowser
    webbrowser.open("Scatterplot-Diagramm.pdf")

def heatingtypePieplot():
    plt.figure(figsize=(12, 8)) 
    df_grouped = df_cleand[['regio1', 'heatingType']].dropna().groupby('heatingType').size().reset_index(name='count')
    total=df_grouped['count'].sum()
    df_grouped['percent']=(df_grouped['count']/total)*100

    main_types = df_grouped[df_grouped['percent'] >= 3]
    others_types=df_grouped[df_grouped['percent']<3].sum().to_frame().T
    others_types['heatingType']='Sonstiges'
    final_data=pd.concat([main_types,others_types])
    final_data['heatingType'] = final_data['heatingType'].str.replace('_', ' ').str.capitalize()

    colors = ['#66b1cf','#99ff99','#ffcc99','#c2c2f0','#c2f0c2','#99b3ff']

    plt.pie(final_data['count'], labels=final_data['heatingType'],colors=colors, autopct='%1.1f%%')
    plt.show()












