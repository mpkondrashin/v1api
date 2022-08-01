import requests
import json

url_base = 'https://api.eu.xdr.trendmicro.com'
url_path = '/v3.0/response/tasks'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJjaWQiOiJiZTg0OTU0NS1lNjc0LTQwZjAtOTlkYy1mYjU2NWYzMjQ3NjAiLCJjcGlkIjoic3ZwIiwicHBpZCI6ImN1cyIsIml0IjoxNjU5MzU3ODYzLCJ1aWQiOiJta29uZHJhc2hpbkBnbWFpbC5jb20iLCJwbCI6IiIsImV0IjoxNjkwODkzODYzfQ.AhWwdZEWp4BwEXl4Mukd3baVIAm848c6Y3TqhvIyhxjsAPMxqdmOV0RXYxeItdoFWt5ljxIS5LdsPtjERYq8QaB9CYD-tVd886KknUpxQ8llceo_wDKcKGRDIkrQU6UkHJeI4yeYvEZCKrkMPHTLG5-1xjClOK1IfzGHA-t_nNLYx3pFJS_VohKEDaPmKRM9Lnc6OQPju6k8wt-QxQ0ksq_qNu0ba0XL_cTe02lkLTt3TGYZgPwhkVPrH7_4Pe_vsIuF3r-r9VVYIPGmfqYuddnkLJopZ8heNOoal1WdtlFp_p-ckzcSAjWS9mxZDVp6W4HIr3heONzyebGVXMbTttWAe-V_b75VjcN6HLAjI4OxGiiU9Pm_ZOntlBIBNldncOsxl29WpZShIli_qh4PJilXPmpHRW4pxL9soSIMTRI7H5ALqVEK_6QxEEKR2dexvoB4uYG0wss5e1c9RMQveJqQ8soYfB0y0WyJ5vS2KzeU5EOlIR3Ql4XDIphxZkGMtfUKK3AKPY2J7QSHnyBKiJYo12Q03ZdDJAtveDwr0ADyWkwrmDqaHB86_PEbyWJtfIIBgG848g1R0YcRAow76_944U_mGcomU1N5PK2_SZOr6n9-HQz_99vmn23S2TPHB-R2oEN2snB3aXaI9VTdQWNqrtwQBQOFIcTJgIEwS_8'
query_params = {}
headers = {'Authorization': 'Bearer ' + token}

r = requests.get(url_base + url_path, params=query_params, headers=headers)

print(r.status_code)
if 'application/json' in r.headers.get('Content-Type', '') and len(r.content):
    print(json.dumps(r.json(), indent=4))
else:
    print(r.text)