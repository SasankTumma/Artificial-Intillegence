from core.chromosome import Chromosome
from core.population import Population
from core.genetic_algorithm import GeneticAlgorithm
import core.settings as settings
import pandas as pd

if __name__ == "__main__":
    generation_number = 0
    MAX_FITNESS = 1
    population = Population(settings.POPULATION_SIZE)
    population.print_population(generation_number)

    while population[0].get_fitness() < MAX_FITNESS and generation_number < settings.MAX_GENERATION_NUMBER:
        generation_number += 1
        population = GeneticAlgorithm.evolve(population)
        population.print_population(generation_number)

    # Generate HTML page with improved styling
    html_content = """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 20px;
            }
            
            h2 {
                color: #333;
            }

            table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }

            th {
                background-color: #12086F;
                color: white;
            }

            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
    """

    for class_name in settings.RAW_DATA["classes"]:
        html_content += f'<h2>Timetable for {class_name}</h2>'
        timetable = population[0].get_time_table(class_name)
        html_content += timetable.to_html(classes='table')

    html_content += '</body></html>'

    with open("timetables_styled.html", "w") as html_file:
        html_file.write(html_content)

    print("Styled HTML page with timetables generated: timetables_styled.html")