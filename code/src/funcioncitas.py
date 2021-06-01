import pandas as pd 
import re
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


#LIMPIEZA DATA TRIPADVISOR 

def porcentageCOL(dataframe):
    return dataframe.isnull().sum(axis=1).apply(lambda x: x/dataframe.shape[1]).sort_values(ascending=False)

def porcentageROW(dataframe):
    return dataframe.isnull().sum().apply(lambda x: x/dataframe.shape[0]).sort_values(ascending=False)

def dropping_col(dataframe):
    delete = ['working_shifts_per_week', 'city','open_hours_per_week', 'terrible', 'excellent', 'very_good', 'average', 'poor', 'keywords', 'awards', 'open_days_per_week']
    return dataframe.drop( axis=1, columns= delete, inplace=True)







#TABLAS TOTALES  SUMA TOTALES 

def dosistotal_Spain_Farma(df1):
    Moderna = df1.dosisEntregadasModerna.sum()
    Janssen = df1.dosisEntregadasJanssen.sum()
    Astrazeneca = df1.dosisEntregadasAstrazeneca.sum()
    Pfizer = df1.dosisEntregadasPfizer.sum()

    dic_farma = [ ('Dosis etregadas Moderna', Moderna), ('Dosis etregadas Janssen', Janssen), 
           ('Dosis etregadas Astrazeneca', Astrazeneca),('Dosis etregadas Pfizer', Pfizer)]

    dosis_Spain_Farma = pd.DataFrame(dic_farma)
    return dosis_Spain_Farma


def dosistotal_unadosis_dosiscompleta(df1):
    unadosis = df1.dosisPrimeraDosis.sum()
    pautacompleta = df1.dosisPautaCompletada.sum()

    list_dosis = [ ('Una dosis', unadosis), ('Dosis Completa', pautacompleta)]
    dosis_Spain_total = pd.DataFrame(list_dosis)
    return dosis_Spain_total















# GRÁFICAS  DOSIS X CCAA


def grafica_pfizer_moderna(df1):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

    ax1 = sns.barplot(y =df1.ccaa, x=df1.dosisEntregadasPfizer, ax= ax1, palette='dark:salmon_r')
    ax1.set_title('Dosis Entregadas PFISER - MILLONES', fontsize=14)
    ax1.set_ylabel('CCAA', fontsize=12)
    #ax1.set_xlabel(xmin=df1.dosisEntregadasPfizer[0], xmax=df1.dosisEntregadasPfizer[-1])

    ax2= sns.barplot(y =df1.ccaa, x=df1.dosisEntregadasModerna, ax= ax2, palette='mako')
    ax2.set_title('Dosis Entregadas MODERNA - MILES(vacunas)', fontsize=14)
    ax2.set_ylabel(' ')


    fig.suptitle('DOSIS ENTREGADAS DISTRIBUIDAS', fontsize=18)
    plt.show()


def grafica_aztrazeneca_janssen(df1):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

    ax1 = sns.barplot(y =df1.ccaa, x=df1.dosisEntregadasAstrazeneca, ax= ax1, palette='dark:salmon_r')
    ax1.set_title('Dosis Entregadas AZTRAZENECA - MILLONES', fontsize=14)
    ax1.set_ylabel('CCAA', fontsize=12)
    #ax1.set_xlabel(xmin=df1.dosisEntregadasPfizer[0], xmax=df1.dosisEntregadasPfizer[-1])

    ax2= sns.barplot(y =df1.ccaa, x=df1.dosisEntregadasJanssen, ax= ax2, palette='mako')
    ax2.set_title('Dosis Entregadas JANSSEN - MILES', fontsize=14)
    ax2.set_ylabel(' ')


    fig.suptitle('DOSIS ENTREGADAS DISTRIBUIDAS', fontsize=18)
    plt.show()   


def grafica_unadosis_dosiscompleta(df1):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(25, 13))

    ax1 = sns.barplot(x =df1.ccaa, y=df1.dosisPrimeraDosis, ax= ax1, palette='Spectral')
    ax1.set_title('Spain - CCAA', fontsize=14)
    ax1.set_ylabel('PRIMERA DOSIS - MILLONES', fontsize=12)

    ax2= sns.barplot(x =df1.ccaa, y=df1.dosisPautaCompletada, ax= ax2, palette='coolwarm')
    ax2.set_title('Spain - CCAA', fontsize=14)
    ax2.set_ylabel('DOSIS COMPLETA - MILLONES', fontsize=12)

    fig.suptitle('DOSIS ADMINISTRADAS', fontsize=18)
    plt.show()

    




#GRAFICA DE TRIPADVISOR
def grafica_ccaa_total_tripAD(df):
    fig, ax = plt.subplots(1, 1, figsize=(27, 8))

    ax = sns.countplot(x=df.region, palette='viridis', )
    ax.set_title('CCAA', fontsize=14)
    fig.suptitle('NUMÉRO DE RESTAURANTES POR CCAA QUE APARECE EN TRIPADVISOR', fontsize=18)
    plt.show()



def grafica_comparativa_CCAA_tripYvacu(df_tablatotal_region_tripAd, df_tablatotal_region_vacunas):
    gridsize = (1, 2)
    fig = plt.figure(figsize=(20, 7))

    ax1 = plt.subplot2grid(gridsize, (0, 0))
    ax2 = plt.subplot2grid(gridsize, (0, 1))

    ax1= sns.barplot(y=('region'), x=('total restaurantes'), data=df_tablatotal_region_tripAd, ax= ax1)
    ax1.set_title('TOTAL RESTAURANTES')

    ax2 = sns.barplot(y=('ccaa'), x=('dosisAdministradas'), data=df_tablatotal_region_vacunas, ax= ax2)
    ax2.set_title('DOSIS ADMINISTRADAS (MILL)', fontsize=14)
    ax2.set_ylabel('CCAA', fontsize=12 )


    fig.suptitle('CCAA - COMPARATIVA TOTAL RESTAURANTES y TOTAL VACUNADOS', fontsize=18)
    plt.show()






def graficas_ratings(df):
    gridsize = (2,1 )
    fig = plt.figure(figsize=(20, 30))

    ax1 = plt.subplot2grid(gridsize, (0, 0))
    ax2 = plt.subplot2grid(gridsize, (1, 0))

    ax1= sns.countplot(y=df.region, hue=df.avg_rating, palette='Set1' ,ax= ax1)
    ax1.set_title('AVG RATING RESTAURANTS')
    ax1.legend(loc= 'center right', fontsize= 'xx-large')

    ax2 = sns.countplot(y=df.region, hue=df.food, palette='Set3' ,ax= ax2)
    ax2.set_title('FOOD SPAIN', fontsize=14)
    ax2.legend(loc= 'center right',fontsize= 'xx-large' )  #bbox_to_anchor=(0.5, 0.5), se queda en medio del todo

    plt.show()





#CARGA DATA


def data1():
    df1 = pd.read_csv('df1_farmaDosis.csv')
    return df1
def data2():
    df2 = pd.read_csv('df2_dosisEntregadas.csv')
    return df2
def data3():
    df3 = pd.read_csv('df3_unadosis.csv')
    return df3
def data4():
    df4 = pd.read_csv('df4_dosiscompleta.csv')
    return df4
def data5():
    df5 = pd.read_csv('df5_edades_unadosis.csv')
    return df5
def data6():
    df6 = pd.read_csv('df6_edades_unadosis.csv')
    return df6
def data():
    df = pd.read_csv('df_tripAd_Spain_Restaurants.csv') 
    return df
def table_trip():
    df_tablatotal_ccaa_tripAd = pd.read_csv('df_tablatotal_region_restaurant.csv')
    return df_tablatotal_ccaa_tripAd
def table_trip():
    df_tablatotal_ccaa_vacunas = pd.read_csv('df_tablatotal_region_vacunas.csv.csv')
    return df_tablatotal_ccaa_vacunas



    