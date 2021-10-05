from flask import Flask, render_template
from pylinac import PicketFence


app = Flask(__name__)
  
@app.route('/')
def img():
    pf_img = r'.\static\img\RI.OCA_QA_Semanal_Tri_2020.Picket_Fence-1_1_0005.dcm'
    pf = PicketFence(pf_img)
    pf.analyze(tolerance=0.15, action_tolerance=0.03)
    pf.plot_analyzed_image()
    pf.save_analyzed_image('./static/img/pick.png')
    
    return render_template  ('pickfence.html', url='./static/img/pick.png')



if __name__ == '__main__':
    app.run(debug=True)