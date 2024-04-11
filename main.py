from flask import Flask, make_response, render_template, request
import sqlite3
import pdfkit
import computations as cm
import numpy as np

company_list = []
energy_list = []
travel_list = []
waste_list = []
def query_carbonfootprint():
    conn = sqlite3.connect("Carbon.db")
    c = conn.cursor()
    c.execute("""
    SELECT * FROM carbonfootprint
    """)
    return c.fetchall()

def convert_to_tuple(list):
    return tuple(list)

def get_graph_data():
    company_list.clear()
    energy_list.clear()
    travel_list.clear()
    waste_list.clear()
    data = query_carbonfootprint()

    for c in data:
        company_list.append(c[1])
        energy_list.append(c[2])
        waste_list.append(c[3])
        travel_list.append(c[4])

    company = convert_to_tuple(company_list)
    carbon = {
        "Energy": np.array(energy_list),
        "Waste": np.array(waste_list),
        "Travel": np.array(travel_list)
    }

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    carbondata = query_carbonfootprint()
    return render_template("home.html", carbondata=carbondata)


@app.route("/report")
def report_page():
    get_graph_data()
    labels = company_list
    energy = energy_list
    waste = waste_list
    travel = travel_list
    return render_template("report.html", labels=labels, energy=energy, travel=travel, waste=waste)


@app.route("/add", methods=["GET", "POST"])
def add_carbon():
    if request.method == "GET":
        return render_template("add_carbondata.html")
    else:
        organization = request.form["organization"]
        monthly_elec_bill = request.form["monthlyelectricbill"]
        natural_gas_bill = request.form["naturalgasbill"]
        monthly_fuel_bill = request.form["monthlyfuelbill"]
        monthly_waste = request.form["wastegenerated"]
        waste_recycled = request.form["wasterecycled"]
        km_travelled = request.form["kilometertravelled"]
        fuel_eff = request.form["fuelefficiency"]

        energy = cm.energy_usage(float(monthly_elec_bill), float(natural_gas_bill), float(monthly_fuel_bill))
        waste = cm.waste(float(monthly_waste), float(waste_recycled))
        travel = cm.travel(float(km_travelled), float(fuel_eff))

        carbon = (organization, energy, waste, travel)

        insert_carbon(carbon)

        return render_template("add_success.html")


def insert_carbon(carbon):
    conn = sqlite3.connect("Carbon.db")
    c = conn.cursor()
    sql = "INSERT INTO carbonfootprint (organization, energyusage, waste, travel) VALUES(?,?,?,?)"
    c.execute(sql, carbon)
    conn.commit()
    conn.close()


def convert_html_to_pdf(html_page, save_name):
    pdfkit.from_file(html_page, save_name)


if __name__ == "__main__":
    app.run()
