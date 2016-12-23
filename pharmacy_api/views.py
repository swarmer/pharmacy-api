""" Cornice services.
"""
from cornice import Service


cors_policy = {
    'origins': ['*'],
    'expose_all_headers': True,
}


drugs = Service(
    name='drugs', path='/drugs', description='Drugs resource',
    cors_policy=cors_policy,
)


DRUGS = []
PHARMACIES = []


@drugs.get()
def get_drugs(request):
    return DRUGS


@drugs.put()
def put_drugs(request):
    DRUGS[:] = request.json_body
    return {'status': 'ok'}


pharmacies = Service(
    name='pharmacies', path='/pharmacies', description='Pharmacies resource',
    cors_policy=cors_policy,
)


@pharmacies.get()
def get_pharmacies(request):
    return PHARMACIES


@pharmacies.put()
def put_pharmacies(request):
    PHARMACIES[:] = request.json_body
    return {'status': 'ok'}
