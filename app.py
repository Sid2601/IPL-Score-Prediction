from flask import Flask, redirect, url_for, request, render_template
import pickle

import numpy as np
app = Flask(__name__)

s='ipl_model.pkl'
model = pickle.load(open(s,'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('input.html')


@app.route("/predict",methods=['POST'])
def pred():
   tp=[]
   
   if request.method == 'POST':
       
      if request.form['venue']=='Brabourne Stadium':
          tp=tp+[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Dr DY Patil Sports Academy':
          tp=tp+[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Eden Gardens':
          tp=tp+[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Feroz Shah Kotla':
          tp=tp+[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='M Chinnaswamy Stadium':
          tp=tp+[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='MA Chidambaram Stadium, Chepauk':
          tp=tp+[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Maharashtra Cricket Association Stadium':
          tp=tp+[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
      elif request.form['venue']=='Narendra Modi Stadium, Motera':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
          
      elif request.form['venue']=='Other':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
      elif request.form['venue']=='Punjab Cricket Association Stadium, Mohali':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
      elif request.form['venue']=='Rajiv Gandhi International Stadium, Uppal':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
      elif request.form['venue']=='Sawai Mansingh Stadium':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
      elif request.form['venue']=='Wankhede Stadium':
          tp=tp+[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
      
                  

      if request.form['batting-team']=='Chennai Super Kings':
         tp=tp+[1, 0, 0, 0, 0, 0, 0, 0]
         bat='Chennai Super Kings'
      elif request.form['batting-team']=='Delhi Daredevils':
         tp = tp + [0, 1, 0, 0, 0, 0, 0, 0]
         bat='Delhi Daredevils'
      elif request.form['batting-team']=='Kings XI Punjab':
         tp = tp + [0, 0, 1, 0, 0, 0, 0, 0]
         bat='Kings XI Punjab'
      elif request.form['batting-team']=='Kolkata Knight Riders':
         tp = tp + [0, 0, 0, 1, 0, 0, 0, 0]
         bat='Kolkata Knight Riders'
      elif request.form['batting-team']=='Mumbai Indians':
         tp = tp + [0, 0, 0, 0, 1, 0, 0, 0]
         bat='Mumbai Indians'
      elif request.form['batting-team']=='Rajasthan Royals':
         tp = tp + [0, 0, 0, 0, 0, 1, 0, 0]
         bat='Rajasthan Royals'
      elif request.form['batting-team']=='Royal Challengers Bangalore':
         tp = tp + [0, 0, 0, 0, 0, 0, 1, 0]
         bat='Royal Challengers Bangalore'
      elif request.form['batting-team']=='Sunrisers Hyderabad':
         tp = tp + [0, 0, 0, 0, 0, 0, 0, 1]
         bat='Sunrisers Hyderabad'


      if request.form['bowling-team']=='Chennai Super Kings':
         tp=tp+[1, 0, 0, 0, 0, 0, 0, 0]
         bowl='CSK'
      elif request.form['bowling-team']=='Delhi Daredevils':
         tp = tp + [0, 1, 0, 0, 0, 0, 0, 0]
         bowl='DC'
      elif request.form['bowling-team']=='Kings XI Punjab':
         tp = tp + [0, 0, 1, 0, 0, 0, 0, 0]
         bowl='PBKS'
      elif request.form['bowling-team']=='Kolkata Knight Riders':
         tp = tp + [0, 0, 0, 1, 0, 0, 0, 0]
         bowl='KKR'
      elif request.form['bowling-team']=='Mumbai Indians':
         tp = tp + [0, 0, 0, 0, 1, 0, 0, 0]
         bowl='MI'
      elif request.form['bowling-team']=='Rajasthan Royals':
         tp = tp + [0, 0, 0, 0, 0, 1, 0, 0]
         bowl='RR'
      elif request.form['bowling-team']=='Royal Challengers Bangalore':
         tp = tp + [0, 0, 0, 0, 0, 0, 1, 0]
         bowl='RCB'
      elif request.form['bowling-team']=='Sunrisers Hyderabad':
         tp = tp + [0, 0, 0, 0, 0, 0, 0, 1]
         bowl='SRH'


      runs=int(request.form['runs'])
      wickets=int(request.form['wickets'])
      overs=float(request.form['overs'])
      runs_last_5=int(request.form['runs_in_prev_5'])
      wickets_last_5 = int(request.form['wickets_in_prev_5'])

      tp= tp + [runs, wickets, overs, runs_last_5, wickets_last_5]

      p=np.array([tp])
      print(p)

      score=(int(model.predict(p)[0]))
      lw=score-5
      up=score+5

      #return redirect(url_for('final_score',score=score))

      return render_template('input.html',score="{} will need to chase runs between {}-{} to win the match".format(bowl,lw,up))
      #return render_template('input.html',score="Expected score is between {}-{}".format(lw, up))

if __name__ == '__main__':
   app.run(debug = True)

