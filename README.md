# 📊 Service Time Distribution Analysis

This project analyzes and models service time data to determine which statistical distribution best fits the observed values.  
It uses **Python**, **SciPy**, and **Seaborn** to perform distribution fitting and Chi-square goodness-of-fit testing.

---

## ⚙️ Features

- Reads service time data from a CSV file (`full_data.csv`).
- Fits multiple candidate distributions:
  - Erlang  
  - Gamma  
  - Exponential  
  - Log-normal  
  - Double Gamma
- Calculates and compares **Chi-square statistics** for each distribution.
- Optionally visualizes data distribution using histograms and density plots.

---

## 🧠 Methodology

1. Load data from `full_data.csv`.  
2. Compute **percentile bins** and observed frequencies.  
3. For each distribution:
   - Fit distribution parameters using `scipy.stats.<dist>.fit()`.  
   - Compute expected frequencies from the cumulative distribution function (CDF).  
   - Perform a **Chi-square goodness-of-fit** test.  
4. Identify the distribution with the lowest Chi-square value.

---

## 🚀 Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/service_times_in_sys_dist.git
cd service_times_in_sys_dist
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Script
```bash
python service_times_in_sys_dist.py
```

Make sure your dataset file is named **`full_data.csv`** and located in the same directory as the script.

---

## 🧩 File Structure
```
📂 service_times_in_sys_dist/
 ├── service_times_in_sys_dist.py   # Main analysis script
 ├── full_data.csv                  # Input data (not included)
 ├── requirements.txt               # Dependencies
 └── README.md                      # Project documentation
```

---

## 🧪 Example Output

When running the script, you’ll see outputs like:
```
<scipy.stats._continuous_distns.gamma_gen object>
(1.95, 0.01, 2.03)

<scipy.stats._continuous_distns.lognorm_gen object>
(0.42, 0.03, 1.85)
```

These represent the fitted parameters for each candidate distribution.

---

## 📦 Dependencies

- pandas  
- numpy  
- scipy  
- seaborn  
- matplotlib

---

## 🧑‍💻 Author

**Triston Aloyssius Marta**  
📧 tristonmarta@yahoo.com.sg
Data Analysis
