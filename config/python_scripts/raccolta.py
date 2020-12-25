""" Raccolta differenziata V0.9.b1 by Mattia(xxKira) for HassioHelp 
    For Question ask in forum.hassiohelp.eu or in Group Telegram """

""" < V0.4 Fix Bugs """
""" V0.4 Added the ability to specify multiple notification services """
""" V0.5 Added support for Google TTS """
""" V0.6 Added support for Alexa TTS """
""" V0.7 Fix Bug: Service not found """
""" V0.8 Added support for Script Notify """
""" V0.9 Added support for ToDay, Tomorrow """
""" V0.9.b1 Added place card for Lovelace Support """
""" V0.9.b2 Added support for New Service Google Tanslate TTS and alexa_media (custom component) -Modified by Caio-"""
""" V0.9.b3 Added title for Script Notify -Modified by Caio-"""

argomento = data.get('argomento')
set_settimana = data.get('set_settimana')
servizio_notifica = data.get('servizio_notifica')
titolo_notifica = data.get('titolo_notifica')
messaggio_notifica = data.get('messaggio_notifica')
entity_google_tts = data.get('entity_google_tts')
entity_alexa_tts = data.get('entity_alexa_tts')
entity_script_tts = data.get('entity_script_tts')

get_day = hass.states.get('input_boolean.giorno_notifica_hp').state
get_verde = (hass.states.get('input_text.verde_hp').state).lower().replace(' ', '')
get_umido = (hass.states.get('input_text.umido_hp').state).lower().replace(' ', '')
get_vetro = (hass.states.get('input_text.vetro_hp').state).lower().replace(' ', '')
get_plastica = (hass.states.get('input_text.plastica_hp').state).lower().replace(' ', '')
get_secco = (hass.states.get('input_text.secco_hp').state).lower().replace(' ', '')
get_carta = (hass.states.get('input_text.carta_hp').state).lower().replace(' ', '')

attributi_input = {'min': 0, 'max': 255, 'mode': 'text', 'Package:': 'Raccolta Differenziata', 'Creato da:': 'Mattia(xxKira)', 'Creato per:': 'HassioHelp'}

for x in range(1, 7):
  hass.states.remove('raccolta_hp.bidone_' + str(x) + '_hp')
  hass.states.remove('raccolta_hp.nome_bidone_' + str(x) + '_hp')
  hass.states.remove('raccolta_hp.giorni_bidone_' + str(x) + '_hp')

if get_verde is None:
  hass.states.set('input_text.verde_hp', '-', attributi_input )
else:
  get_verde = get_verde.split('-')
if get_umido is None:
  hass.states.set('input_text.umido_hp', '-', attributi_input )
else:
  get_umido = get_umido.split('-')
if get_vetro is None:
  hass.states.set('input_text.vetro_hp', '-', attributi_input )
else:
  get_vetro = get_vetro.split('-')
if get_plastica is None:
  hass.states.set('input_text.plastica_hp', '-', attributi_input )
else:
  get_plastica = get_plastica.split('-')
if get_secco is None:
  hass.states.set('input_text.secco_hp', '-', attributi_input )
else:
  get_secco = get_secco.split('-')
if get_carta is None:
  hass.states.set('input_text.carta_hp', '-', attributi_input)
else:
  get_carta = get_carta.split('-')

prima_settimana = True if set_settimana is None or set_settimana == "True" else False
days = {0:'lun', 1:'mar', 2:'mer', 3:'gio', 4:'ven', 5:'sab', 6:'dom'}
date = datetime.datetime.now()
logger.info(date)
data_riferimento = datetime.datetime(2019, 1, 1)
logger.info(data_riferimento)
giorno_riferimento_n = (data_riferimento - datetime.datetime(data_riferimento.year, 1, 1)).days + 1
logger.info(giorno_riferimento_n)
giorno_riferimento_s = data_riferimento.weekday()
oggi_n = (date - datetime.datetime(date.year, 1, 1)).days + 1
oggi_s = date.weekday()
domani_n = oggi_n + 1

if oggi_s == 6:
  domani_s = 0
else:
  domani_s = date.weekday() + 1

domani_s = days[domani_s]
logger.info(domani_s)
oggi_s = days[oggi_s]
logger.info(oggi_s)
logger.info(oggi_n)

def set_rifiuti(hass, day, day_n, prima_settimana, get_vetro, get_verde, get_umido, get_plastica, get_secco, get_carta):
  global attributi_sensor
  attributi_sensor = {'Package:': 'Raccolta Differenziata', 'Creato da:': 'Mattia(xxKira)', 'Creato per:': 'HassioHelp'}

  global domani_ritirano
  domani_ritirano = []

  vetro = get_vetro[0]
  verde = get_verde[0]
  umido = get_umido[0]
  plastica = get_plastica[0]
  secco = get_secco[0]
  carta = get_carta[0]
  vetro = vetro.split(",")
  verde = verde.split(",")
  umido = umido.split(",")
  plastica = plastica.split(",")
  secco = secco.split(",")
  carta = carta.split(",")

  try:
    verde_bis = get_verde[1]
    verde_bis = verde_bis.split(',')
  except:
    verde_bis = []
  try:
    vetro_bis = get_vetro[1]
    vetro_bis = vetro_bis.split(',')
  except:
    vetro_bis = []
  try:
    umido_bis = get_umido[1]
    umido_bis = umido_bis.split(',')
  except:
    umido_bis = []
  try:
    plastica_bis = get_plastica[1]
    plastica_bis = plastica_bis.split(',')
  except:
    plastica_bis = []
  try:
    secco_bis = get_secco[1]
    secco_bis = secco_bis.split(',')
  except:
    secco_bis = []
  try:
    carta_bis = get_carta[1]
    carta_bis = carta_bis.split(',')
  except:
    carta_bis = []

  try:
    verde_bis_dis = get_verde[2]
    verde_bis_dis = verde_bis_dis.split(',')
  except:
    verde_bis_dis = []
  try:
    vetro_bis_dis = get_vetro[2]
    vetro_bis_dis = vetro_bis_dis.split(',')
  except:
    vetro_bis_dis = []
  try:
    umido_bis_dis = get_umido[2]
    umido_bis_dis = umido_bis_dis.split(',')
  except:
    umido_bis_dis = []
  try:
    plastica_bis_dis = get_plastica[2]
    plastica_bis_dis = plastica_bis_dis.split(',')
  except:
    plastica_bis_dis = []
  try:
    secco_bis_dis = get_secco[2]
    secco_bis_dis = secco_bis_dis.split(',')
  except:
    secco_bis_dis = []
  try:
    carta_bis_dis = get_carta[2]
    carta_bis_dis = carta_bis_dis.split(',')
  except:
    carta_bis_dis = []

  if prima_settimana is True:
    lun_bis = 0
    mar_bis = 1
    mer_bis = 2
    gio_bis = 3
    ven_bis = 4
    sab_bis = 5
    dom_bis = 6
  else:
    lun_bis = 7
    mar_bis = 8
    mer_bis = 9
    gio_bis = 10
    ven_bis = 11
    sab_bis = 12
    dom_bis = 13

  lun_bis = day_n - lun_bis
  lun_bis = lun_bis / 14

  mar_bis = day_n - mar_bis
  mar_bis = mar_bis / 14

  mer_bis = day_n - mer_bis
  mer_bis = mer_bis / 14

  gio_bis = day_n - gio_bis
  gio_bis = gio_bis / 14

  ven_bis = day_n - ven_bis
  ven_bis = ven_bis / 14

  sab_bis = day_n - sab_bis
  sab_bis = sab_bis / 14 

  dom_bis = day_n - dom_bis
  dom_bis = dom_bis / 14

  bool_bis = (lun_bis == int(lun_bis) or mar_bis == int(mar_bis) or mer_bis == int(mer_bis) or gio_bis == int(gio_bis) or ven_bis == int(ven_bis) or sab_bis == int(sab_bis) or dom_bis == int(dom_bis))

  # VERDE
  if day in verde or ((day in verde_bis) and bool_bis) or ((day in verde_bis_dis) and not bool_bis) :
    hass.states.set('raccolta_hp.verde', 'on', attributi_sensor)
    domani_ritirano = domani_ritirano + ["verde"]
  else:
    hass.states.set('raccolta_hp.verde', 'off', attributi_sensor)

  # VETRO
  if day in vetro or ((day in vetro_bis) and bool_bis) or ((day in vetro_bis_dis) and not bool_bis):
    hass.states.set('raccolta_hp.vetro', 'on', attributi_sensor)
    domani_ritirano = domani_ritirano + ["vetro"]
  else:
    hass.states.set('raccolta_hp.vetro', 'off', attributi_sensor)

  # UMIDO
  if day in umido or ((day in umido_bis) and bool_bis) or ((day in umido_bis_dis) and not bool_bis):
    hass.states.set('raccolta_hp.umido', 'on', attributi_sensor)
    domani_ritirano = domani_ritirano + ["umido"]
  else:
    hass.states.set('raccolta_hp.umido', 'off', attributi_sensor)

  # PLASTICA
  if day in plastica or ((day in plastica_bis) and bool_bis) or ((day in plastica_bis_dis) and not bool_bis):
    hass.states.set('raccolta_hp.plastica', 'on', attributi_sensor)
    domani_ritirano = domani_ritirano + ["plastica"]
  else:
    hass.states.set('raccolta_hp.plastica', 'off', attributi_sensor)

  # SECCO
  if day in secco or ((day in secco_bis) and bool_bis) or ((day in secco_bis_dis) and not bool_bis):
    hass.states.set('raccolta_hp.secco', 'on', attributi_sensor)
    domani_ritirano = domani_ritirano + ["secco"]
  else:
    hass.states.set('raccolta_hp.secco', 'off', attributi_sensor)

  # CARTA
  if day in carta or ((day in carta_bis) and bool_bis) or ((day in carta_bis_dis) and not bool_bis):
    hass.states.set('raccolta_hp.carta', 'on', attributi_sensor)
    domani_ritirano = domani_ritirano + ["carta"]
  else:
    hass.states.set('raccolta_hp.carta', 'off', attributi_sensor)

if get_day == 'on':
  hass.states.set('input_boolean.giorno_notifica_hp', 'on', {'friendly_name': 'Notifica Oggi', 'icon': 'mdi:update', 'Package:': 'Raccolta Differenziata', 'Creato da:': 'Mattia(xxKira)', 'Creato per:': 'HassioHelp'})
  set_rifiuti(hass, oggi_s, oggi_n, prima_settimana, get_vetro, get_verde, get_umido, get_plastica, get_secco, get_carta)
else:
  hass.states.set('input_boolean.giorno_notifica_hp', 'off', {'friendly_name': 'Notifica Giorno Prima', 'icon': 'mdi:update', 'Package:': 'Raccolta Differenziata', 'Creato da:': 'Mattia(xxKira)', 'Creato per:': 'HassioHelp'})
  set_rifiuti(hass, domani_s, domani_n, prima_settimana, get_vetro, get_verde, get_umido, get_plastica, get_secco, get_carta)

domani_ritirano = ", ".join(domani_ritirano)
try:
  message = messaggio_notifica + " " + domani_ritirano
except:
  message = "Domani ritirano: " + domani_ritirano
title = titolo_notifica

if argomento == 'notifica' and len(domani_ritirano) != 0:
  servizio_notifica = servizio_notifica.replace(' ', '').split(',')
  entity_google_tts = entity_google_tts.replace(' ', '').split(',')
  entity_alexa_tts = entity_alexa_tts.replace(' ', '').split(',')

  try:
    entity_script_tts = entity_script_tts.replace(' ', '').split(',')
  except:
    pass

   #try:
   #  for entity_alexa in entity_alexa_tts:
   #    hass.services.call('media_player', 'alexa_tts', {'entity_id': 'media_player.' + entity_alexa, 'message': message}) #"message":"test", "data":{"type":"tts"},
  try:
    for entity_alexa in entity_alexa_tts:
      hass.services.call('notify','alexa_media', {'target': entity_alexa, 'data': {'type':'tts'}, 'title': title, 'message': message})
  except:
    pass

  try:
    for entity_google in entity_google_tts:
      hass.services.call('tts', 'google_translate_say', {'entity_id': 'media_player.' + entity_google, 'message': message})
  except:
    pass

  try:
    for service in servizio_notifica:
      hass.services.call('notify', service, {'title': title, 'message': message})
  except:
    pass
  
  try:
    for entity_script in entity_script_tts:
      hass.services.call('script', entity_script, {'title': title, 'message': message})
  except:
    pass

if len(domani_ritirano) != 0:
  i = 0
  try:
    bidoni_on = domani_ritirano.replace(' ','').split(',')
  except:
    bidoni_on = domani_ritirano

  for x in bidoni_on:
    i = i + 1
    y = (hass.states.get('input_text.' + x + '_hp').state).lower().replace(',', ' ')
    hass.states.set('raccolta_hp.bidone_' + str(i) + '_hp', 'on', attributi_sensor)
    hass.states.set('raccolta_hp.nome_bidone_' + str(i) + '_hp', x, attributi_input)
    hass.states.set('raccolta_hp.giorni_bidone_' + str(i) + '_hp', y, attributi_input)
    #.capitalize()