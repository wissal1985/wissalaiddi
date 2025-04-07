import pandas as pd 
import matplotlib.pyplot as plt

# 1. Importation des données

# Charger les données à partir d'un fichier CSV
data_frame = pd.read_csv('employees.csv', encoding="ISO-8859-1")

# 2. Exploration des données
# Afficher les 5 premières lignes du DataFrame
print(data_frame.head())

# Vérifier les informations générales sur le DataFrame
print(data_frame.info())

# Vérifier la présence de valeurs manquantes
print(data_frame.isnull().sum())

# Nettoyer la colonne 'Annual Salary' pour enlever les symboles de devise et les virgules
data_frame['Annual Salary'] = data_frame['Annual Salary'].replace({r'\$': '', r',': ''}, regex=True)

# Convertir la colonne 'Annual Salary' en type numérique, en remplaçant les valeurs non numériques par NaN
data_frame['Annual Salary'] = pd.to_numeric(data_frame['Annual Salary'], errors='coerce')

# Remplir les NaN avec la moyenne
data_frame['Annual Salary'] = data_frame['Annual Salary'].fillna(data_frame['Annual Salary'].mean())


# 3. Manipulation des données
# Sélectionner des colonnes ou des lignes spécifiques

# Sélectionner des colonnes spécifiques
data_frame_selected = data_frame[['Full Name', 'Annual Salary', 'Gender']]

print(data_frame_selected)

# Sélectionner des lignes spécifiques, par exemple les 10 premières lignes
data_frame_first_10 = data_frame.head(10)
print(data_frame_first_10)


# Filtrer les employés ayant un salaire annuel supérieur à 100 000
data_frame_high_salary = data_frame[data_frame['Annual Salary'] > 100000]
print(data_frame_high_salary[['Full Name', 'Annual Salary', 'Gender']])


# Extraire l'âge de l'année de recrutement et créer une nouvelle colonne 'Years at Company'
data_frame['Years at Company'] = 2025 - pd.to_datetime(data_frame['Hire Date']).dt.year
print(data_frame[['Full Name', 'Annual Salary', 'Gender', 'Years at Company']])


# Trier les données par salaire annuel en ordre décroissant
data_frame_sorted = data_frame.sort_values(by='Annual Salary', ascending=False)
print(data_frame_sorted[['Full Name', 'Annual Salary', 'Gender', 'Years at Company']])


# 4. Analyse statistique
# Calculer des statistiques descriptives pour les colonnes numériques
print(data_frame.describe())

# Calculer la moyenne, médiane et écart-type de la colonne 'Annual Salary'
mean_salary = data_frame['Annual Salary'].mean()
median_salary = data_frame['Annual Salary'].median()
std_salary = data_frame['Annual Salary'].std()

print(f"Moyenne: {mean_salary}, Médiane: {median_salary}, Ecart-type: {std_salary}")

# Grouper par 'Department' et calculer la moyenne du salaire annuel pour chaque département
grouped_salary = data_frame.groupby('Department')['Annual Salary'].mean()
print(grouped_salary)


# 5. Visualisation des données
# Histogramme des salaires annuels
plt.hist(data_frame['Annual Salary'], bins=20)
plt.title('Distribution des salaires annuels')
plt.xlabel('Salaire annuel')
plt.ylabel('Fréquence')
plt.show()

# Tracer un boxplot pour les salaires annuels
plt.boxplot(data_frame['Annual Salary'])
plt.title('Boxplot des salaires annuels')
plt.ylabel('Salaire annuel')
plt.show()