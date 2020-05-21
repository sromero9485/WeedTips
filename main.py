from flask import Flask
from flask import render_template
from flask import request
from flask import Markup


import io
import os


import numpy as np
from numpy import genfromtxt
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


# necesario en pythonanywhere
PATH=os.path.dirname(os.path.abspath(__file__))
    
# default inicial

Condicion1='Stress'
Condicion2='Depression'
Efecto1='Happy'
Efecto2='Relaxed'
Efecto3='Creative'
Efecto4='Energetic'
Sabor1='Sweet'
Sabor2='Pine'
Sabor3='Lavender'




# modelo 
tf = TfidfVectorizer(analyzer='word', stop_words='english')
nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')



# flask app
app=Flask(__name__)



# antes del primer request...
@app.before_first_request
def startup():
    global tasa_media, logreg
    
    data=genfromtxt(PATH+'/data/data_weed.csv', delimiter=',') # fuera de jupyter
    
    matrix1 = tf.fit_transform(data['EFA'])   
    nn.fit(matrix1)  # se entrena una vez antes de arrancar
    
    

    
# main app
@app.route("/", methods=['POST', 'GET'])
def main():
    ideal_strain = []
    
    if request.method=='POST':
        s_condition1=request.form['s_condition1']
        s_condition2=request.form['s_condition2']
        s_efecto1=request.form['s_efecto1']
        s_efecto2=request.form['s_efecto2']
        s_efecto3=request.form['s_efecto3']
        s_efecto4=request.form['s_efecto4']
        s_flavor1=request.form['s_flavor1']
        s_flavor2=request.form['s_flavor2']
        s_flavor3=request.form['s_flavor3']

   
        
        # Condition1
        if (s_condition1 == 'Stress'):
            ideal_strain.append('Stress')
        if (s_condition1 == 'Depression'):
            ideal_strain.append('Depression')
        if (s_condition1 == 'Insomnia'):
            ideal_strain.append('Insomnia')
        if (s_condition1 == 'Nausea'):
            ideal_strain.append('Nausea')
        if (s_condition1 == 'Inflamation'):
            ideal_strain.append('Inflamation')
        if (s_condition1 == 'Muscle Spasms'):
            ideal_strain.append('Muscle')    
        if (s_condition1 == 'Seizures'):
            ideal_strain.append('Seizures')    
        if (s_condition1 == 'Anxiety'):
            ideal_strain.append('Anxious')
        if (s_condition1 == 'Lack of apetite'):
            ideal_strain.append('Lack')    

        # Condition2
        if (s_condition2 == 'Stress'):
            ideal_strain.append('Stress')
        if (s_condition2 == 'Depression'):
            ideal_strain.append('Depression')
        if (s_condition2 == 'Insomnia'):
            ideal_strain.append('Insomnia')
        if (s_condition2 == 'Nausea'):
            ideal_strain.append('Nausea')
        if (s_condition2 == 'Inflamation'):
            ideal_strain.append('Inflamation')
        if (s_condition2 == 'Muscle Spasms'):
            ideal_strain.append('Muscle')    
        if (s_condition2 == 'Seizures'):
            ideal_strain.append('Seizures')    
        if (s_condition2 == 'Anxiety'):
            ideal_strain.append('Anxious')
        if (s_condition2 == 'Lack of apetite'):
            ideal_strain.append('Lack')  

        #Efecto1
        if (s_efecto1 == 'Happy'):
            ideal_strain.append('Happy')
        if (s_efecto1 == 'Dry Mouth'):
            ideal_strain.append('Dry')
        if (s_efecto1 == 'Relaxed'):
            ideal_strain.append('Relaxed')
        if (s_efecto1 == 'Euphoric'):
            ideal_strain.append('Euphoric')
        if (s_efecto1 == 'Uplifted'):
            ideal_strain.append('Uplifted')
        if (s_efecto1 == 'Paranoid'):
            ideal_strain.append('Paranoid')
        if (s_efecto1 == 'Sleepy'):
            ideal_strain.append('Sleepy')
        if (s_efecto1 == 'Creative'):
            ideal_strain.append('Creative')
        if (s_efecto1 == 'Energetic'):
            ideal_strain.append('Energetic')
        if (s_efecto1 == 'Hungry'):
            ideal_strain.append('Hungry')
        if (s_efecto1 == 'Focus'):
            ideal_strain.append('Focus')
        if (s_efecto1 == 'Tingly'):
            ideal_strain.append('Tingly')
        if (s_efecto1 == 'Talkative'):
            ideal_strain.append('Talkative')
        if (s_efecto1 == 'Horny'):
            ideal_strain.append('Horny')

        #Efecto2
        if (s_efecto2 == 'Happy'):
            ideal_strain.append('Happy')
        if (s_efecto2 == 'Dry Mouth'):
            ideal_strain.append('Dry')
        if (s_efecto2 == 'Relaxed'):
            ideal_strain.append('Relaxed')
        if (s_efecto2 == 'Euphoric'):
            ideal_strain.append('Euphoric')
        if (s_efecto2 == 'Uplifted'):
            ideal_strain.append('Uplifted')
        if (s_efecto2 == 'Paranoid'):
            ideal_strain.append('Paranoid')
        if (s_efecto2 == 'Sleepy'):
            ideal_strain.append('Sleepy')
        if (s_efecto2 == 'Creative'):
            ideal_strain.append('Creative')
        if (s_efecto2 == 'Energetic'):
            ideal_strain.append('Energetic')
        if (s_efecto2 == 'Hungry'):
            ideal_strain.append('Hungry')
        if (s_efecto2 == 'Focus'):
            ideal_strain.append('Focus')
        if (s_efecto2 == 'Tingly'):
            ideal_strain.append('Tingly')
        if (s_efecto2 == 'Talkative'):
            ideal_strain.append('Talkative')
        if (s_efecto2 == 'Horny'):
            ideal_strain.append('Horny')

        #Efecto3
        if (s_efecto3 == 'Happy'):
            ideal_strain.append('Happy')
        if (s_efecto3 == 'Dry Mouth'):
            ideal_strain.append('Dry')
        if (s_efecto3 == 'Relaxed'):
            ideal_strain.append('Relaxed')
        if (s_efecto3 == 'Euphoric'):
            ideal_strain.append('Euphoric')
        if (s_efecto3 == 'Uplifted'):
            ideal_strain.append('Uplifted')
        if (s_efecto3 == 'Paranoid'):
            ideal_strain.append('Paranoid')
        if (s_efecto3 == 'Sleepy'):
            ideal_strain.append('Sleepy')
        if (s_efecto3 == 'Creative'):
            ideal_strain.append('Creative')
        if (s_efecto3 == 'Energetic'):
            ideal_strain.append('Energetic')
        if (s_efecto3 == 'Hungry'):
            ideal_strain.append('Hungry')
        if (s_efecto3 == 'Focus'):
            ideal_strain.append('Focus')
        if (s_efecto3 == 'Tingly'):
            ideal_strain.append('Tingly')
        if (s_efecto3 == 'Talkative'):
            ideal_strain.append('Talkative')
        if (s_efecto3 == 'Horny'):
            ideal_strain.append('Horny')

        #Efecto4
        if (s_efecto4 == 'Happy'):
            ideal_strain.append('Happy')
        if (s_efecto4 == 'Dry Mouth'):
            ideal_strain.append('Dry')
        if (s_efecto4 == 'Relaxed'):
            ideal_strain.append('Relaxed')
        if (s_efecto4 == 'Euphoric'):
            ideal_strain.append('Euphoric')
        if (s_efecto4 == 'Uplifted'):
            ideal_strain.append('Uplifted')
        if (s_efecto4 == 'Paranoid'):
            ideal_strain.append('Paranoid')
        if (s_efecto4 == 'Sleepy'):
            ideal_strain.append('Sleepy')
        if (s_efecto4 == 'Creative'):
            ideal_strain.append('Creative')
        if (s_efecto4 == 'Energetic'):
            ideal_strain.append('Energetic')
        if (s_efecto4 == 'Hungry'):
            ideal_strain.append('Hungry')
        if (s_efecto4 == 'Focus'):
            ideal_strain.append('Focus')
        if (s_efecto4 == 'Tingly'):
            ideal_strain.append('Tingly')
        if (s_efecto4 == 'Talkative'):
            ideal_strain.append('Talkative')
        if (s_efecto4 == 'Horny'):
            ideal_strain.append('Horny') 
            
         #Flavor1
        if (s_flavor1 == 'Earthy'):
            ideal_strain.append('Earthy')
        if (s_flavor1 == 'Sweet'):
            ideal_strain.append('Sweet')
        if (s_flavor1 == 'Pepper'):
            ideal_strain.append('Pepper')
        if (s_flavor1 == 'Euphoric'):
            ideal_strain.append('Euphoric')
        if (s_flavor1 == 'Berry'):
            ideal_strain.append('Berry')
        if (s_flavor1 == 'Pine'):
            ideal_strain.append('Pine')
        if (s_flavor1 == 'Lemon'):
            ideal_strain.append('Lemon')
        if (s_flavor1 == 'Grape'):
            ideal_strain.append('Grape')
        if (s_flavor1 == 'Blueberry'):
            ideal_strain.append('Blueberry')
        if (s_flavor1 == 'Lime'):
            ideal_strain.append('Lime')
        if (s_flavor1 == 'Orange'):
            ideal_strain.append('Orange')
        if (s_flavor1 == 'Mango'):
            ideal_strain.append('Mango')
        if (s_flavor1 == 'Pineapple'):
            ideal_strain.append('Pineapple')
        if (s_flavor1 == 'Lavender'):
            ideal_strain.append('Lavender')   

         #Flavor2
        if (s_flavor2 == 'Earthy'):
            ideal_strain.append('Earthy')
        if (s_flavor2 == 'Sweet'):
            ideal_strain.append('Sweet')
        if (s_flavor2 == 'Pepper'):
            ideal_strain.append('Pepper')
        if (s_flavor2 == 'Euphoric'):
            ideal_strain.append('Euphoric')
        if (s_flavor2 == 'Berry'):
            ideal_strain.append('Berry')
        if (s_flavor2 == 'Pine'):
            ideal_strain.append('Pine')
        if (s_flavor2 == 'Lemon'):
            ideal_strain.append('Lemon')
        if (s_flavor2 == 'Grape'):
            ideal_strain.append('Grape')
        if (s_flavor2 == 'Blueberry'):
            ideal_strain.append('Blueberry')
        if (s_flavor2 == 'Lime'):
            ideal_strain.append('Lime')
        if (s_flavor2 == 'Orange'):
            ideal_strain.append('Orange')
        if (s_flavor2 == 'Mango'):
            ideal_strain.append('Mango')
        if (s_flavor2 == 'Pineapple'):
            ideal_strain.append('Pineapple')
        if (s_flavor2 == 'Lavender'):
            ideal_strain.append('Lavender'

         #Flavor3
        if (s_flavor3 == 'Earthy'):
            ideal_strain.append('Earthy')
        if (s_flavor3 == 'Sweet'):
            ideal_strain.append('Sweet')
        if (s_flavor3 == 'Pepper'):
            ideal_strain.append('Pepper')
        if (s_flavor3 == 'Euphoric'):
            ideal_strain.append('Euphoric')
        if (s_flavor3 == 'Berry'):
            ideal_strain.append('Berry')
        if (s_flavor3 == 'Pine'):
            ideal_strain.append('Pine')
        if (s_flavor3 == 'Lemon'):
            ideal_strain.append('Lemon')
        if (s_flavor3 == 'Grape'):
            ideal_strain.append('Grape')
        if (s_flavor3 == 'Blueberry'):
            ideal_strain.append('Blueberry')
        if (s_flavor3 == 'Lime'):
            ideal_strain.append('Lime')
        if (s_flavor3 == 'Orange'):
            ideal_strain.append('Orange')
        if (s_flavor3 == 'Mango'):
            ideal_strain.append('Mango')
        if (s_flavor3 == 'Pineapple'):
            ideal_strain.append('Pineapple')
        if (s_flavor3 == 'Lavender'):
            ideal_strain.append('Lavender'
            
            
        
       
        
        # prediccion
        new = tf.transform(ideal_strain)
        results = nn.kneighbors(new.todense())
        
        name = [data['name'][results[1][0][i]] for i in range(5)]
        EFA = [data['EFA'][results[1][0][i]] for i in range(5)]
        thc = [data['thc_input'][results[1][0][i]] for i in range(5)]
        typ = [data['type'][results[1][0][i]] for i in range(5)]

    
        recommend1 = name[0] + ' - ' + typ[0] + ' - ' + EFA[0] +' - ' + thc[0]
        recommend2 = name[1] + ' - ' + typ[1] + ' - ' + EFA[1] +' - ' + thc[1]
        recommend3 = name[2] + ' - ' + typ[2] + ' - ' + EFA[2] +' - ' + thc[2]
        recommend4 = name[3] + ' - ' + typ[3] + ' - ' + EFA[3] +' - ' + thc[3]
        recommend5 = name[4] + ' - ' + typ[4] + ' - ' + EFA[4] +' - ' + thc[4]

        return render_template('index.html', 
            model_results = recommend1, 
                        recommend2,
                        recommend3, 
                        recommend4, 
                        recommend5)
            
        
        
    else:
        # parametros por defecto
        return render_template('index.html',
            model_results = '',
            s_condition1=Condicion1,
            s_condition1=Condicion1,
            s_efecto1=Efecto1,
            s_efecto2=GEfecto2,
            s_efecto3=Efecto3,
            s_efecto4=Efecto4,
            s_flavor1=Sabor1,
            s_flavor2=Sabor2,
            s_flavor3=Sabor3)
    

# solo en local
if __name__=='__main__':
    app.run(debug=False)
    
