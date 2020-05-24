#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pandas as pd
import json
here = os.path.dirname(os.path.abspath(__file__))

result = pd.read_csv("{}/{}".format(here, "estados.csv"),sep=";")
country_list = list()
for index, row in result.iterrows():
    country_list.append({"{#NOME_ESTADO}": row['Estado'],
                        "{#ESTADO_IBAN}": row['Codigo'] })

    data = json.dumps({"data": country_list}, indent=4).decode('unicode-escape').encode('utf8')

print(data)