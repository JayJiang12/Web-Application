from flask import Flask, request, json
from flask import render_template
import vesta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPoints', methods=["POST"])
def getPoints():
    col_slider = request.form['param_col_slider']
    temp_min = request.form['param_temp_min']
    temp_max = request.form['param_temp_max']
    pop = request.form['param_pop']

    searcher = vesta.UserSearch(temp_min, temp_max, pop)    
    #databases = {"cDB" : CensusDB(user), "ncdcDB" : NcdcDB(user), "eGDB" : ElectionGitDB(user), "blsDB" : BlsDB(user)}
    #results = vesta.NcdcDB(searcher).askDB(searcher)
    results = vesta.CensusDB(searcher).askDB(searcher)
    #results = databases['ncdcDB'].askDB()
    # finalResult = Set()
    # for key, db in databases.items():
    #     db.buildQuery()
    #     db.askDB()
    #     finalResult.intersection_update(db.results)
    # print("Final Result: ", finalResult, "\n")
    
    #return results
    #return json.dumps(col_slider);
    results = [['Baltimore', [39.260261, -76.711508]], ['Detroit', [42.3180632,-83.32022]]]
    return json.dumps(results)

if __name__ == "__main__":
    app.run()
