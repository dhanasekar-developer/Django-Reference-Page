from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import xml.etree.ElementTree as ET
import logging
import xmltodict, json
from lxml import etree
import json

# Create your views here.

url = "http://www.templiveservice.com/service.asmx"

headers = {
    "Content-Type": "text/xml; charset=utf-8",
}

# root = ET.fromstring(response.text)
logger = logging.getLogger("TESTING")

def employee_view(request):
    query = "select * from Trandata.employee_office@Tcscentr where empcode in (18491)"

    payload = f'''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
    <GetData_Json xmlns="http://tempuri.org/">
    <str>{query}</str>
    <B_Code>Centra</B_Code>
    <C_Mode>TCS</C_Mode>
    </GetData_Json>
</soap:Body>
</soap:Envelope>'''
    try:
        response = requests.post(url, data = payload, headers=headers)
        # logger.debug(f'Api Data Is : {response.text}')
        if response.status_code == 200:
            soap_response = response.text
        else:
            soap_response = f'Error:{response.status_code}'
    except Exception as e:
        soap_response = f'Error:{str(e)}'

    root = ET.fromstring(soap_response)

    for child in root.iter():
        res = child.text
        # logger.debug(f'for loop response: {res}')
    datas = json.loads(res)
    for data in datas:
        name = data['EMPNAME']
        empcode = data['EMPCODE']
        return render(request, 'api/api_view.html', { 'name': name, 'empcode': empcode })

    # logger.debug(f'data is : {data}')
def response_view(request):

    
    if request.method == 'POST':
        empcode = request.POST.get('empcode')
        query = f"Select E.Empcode,E.Empname,p.PHONE,P.EMAIL From Trandata.Employee_office@Tcscentr E, Trandata.Employee_Personal@Tcscentr P where P.Empsrno = E.Empsrno and E.Empcode in ({empcode})"

        payload = f'''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
    <GetData_Json xmlns="http://tempuri.org/">
    <str>{query}</str>
    <B_Code>Centra</B_Code>
    <C_Mode>TCS</C_Mode>
    </GetData_Json>
</soap:Body>
</soap:Envelope>'''
        try:
            empcode = request.POST.get('empcode')
            logger.debug(f'emp code is : {empcode}')
            response = requests.post(url, data=payload, headers=headers)

            if response.status_code == 200:
                soap_response = response.text
            else:
                soap_response = f'Error : {response.status_code}'

            root = ET.fromstring(soap_response)

            for child in root.iter():
                response = child.text
            datas = json.loads(response)
            # datas = list(datas)
            logger.debug(f'list data is : {datas}')
            # return render(request, 'api/api_view.html', { 'datas':datas })
            
            # for data in datas:
            #     name = data["EMPNAME"]
            #     empcode = data["EMPCODE"]
            #     mobileNO = data["PHONE"]
            #     email = data["EMAIL"]
           
            table = '''<table>
    <thead>
        <tr>
            <th>Empcode</th>
            <th>Name</th>
            <th>Mobile No</th>
            <th>Email ID</th>
        </tr>
    </thead>
    <tbody id="tbody">'''
            for data in datas:
                table += f'''<tr>
        <td>{data["EMPCODE"]}</td>
        <td>{data["EMPNAME"]}</td>
        <td>{data["PHONE"]}</td>
        <td>{data["EMAIL"]}</td>
    </tr>'''
            table += '''
    </tbody>
</table>'''
            return HttpResponse(table)
        except ValueError as ve:
            return JsonResponse({ "employee_code": ve }, status=400)
        

    

        
# for child in root.iter("*"):
#     print(child)

#from api.views import getEmployee
#getEmployee()