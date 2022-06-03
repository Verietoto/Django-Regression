import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
from firstapp.models import regression_db
import numpy as np
from sklearn.linear_model import LinearRegression
matplotlib.use('Agg')
def empty_graph():
    fig, ax = plt.subplots()
    xs = []
    ys = []
    if len(regression_db.objects.all()) >= 1:
        for obj in regression_db.objects.all():
            x = obj.x_val
            y = obj.y_val
            xs.append(x)
            ys.append(y)
    
    if len(xs) >= 2:
        print("True")
        xsr = np.array(xs).reshape(len(xs),-1)
        ysr = np.array(ys).reshape(len(xs),-1)
        reg  = LinearRegression()
        reg.fit(xsr,ysr)
        
        pred = reg.predict(np.array(xs).reshape(len(xs),1))
        ax.plot(xs,pred)

    ax.scatter(xs,ys) 
    dir = "static/gambar.png"
    fig.savefig(dir, pad_inches = 0.3, bbox_inches='tight')
    plt.close()