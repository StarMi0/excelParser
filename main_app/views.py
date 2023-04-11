from django.db.models import Sum
import random
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import Company
from datetime import datetime


def load_data(request):
    # Load data from Excel file
    df = pd.read_excel('data/Приложение_к_заданию_бек_разработчика.xlsx', sheet_name='Лист1', header=1)

    # Add date column
    df['date'] = pd.to_datetime(datetime(2022, 6, 1) + pd.to_timedelta(random.sample(range(30), len(df)), unit='d'))

    # Convert data to list of dictionaries
    data = df.to_dict('records')

    # Insert data into database
    for d in data:
        try:
            company = Company(company=d['Unnamed: 1'], fact_qliq=d['Qliq'], fact_qoil=d['Qoil'],
                              fact_qliq_2=d['Unnamed: 3'], fact_qoil_2=d['Unnamed: 5'],
                              forecast_qliq=d['Qliq.1'], forecast_qoil=d['Unnamed: 7'],
                              forecast_qliq_2=d['Qoil.1'], forecast_qoil_2=d['Unnamed: 9'],
                              date=d['date'])
            company.save()
        except:
            print(d)
    return HttpResponse('Data loaded successfully')


def calculate_total(request):
    # Calculate total by date
    total_by_date = Company.objects.values('date').annotate(total_qliq=Sum('fact_qliq') + Sum('forecast_qliq'),
                                                            total_qoil=Sum('fact_qoil') + Sum('forecast_qoil'))
    # Render template with data
    return render(request, 'imported.html', {'total_by_date': total_by_date})
