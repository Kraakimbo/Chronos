"""French Wikipedia links for the "Pour aller plus loin" section.

One URL per event slug (matches app.data.EVENTS), sourced via web search.
Not every event has an article dedicated to the exact event -- some link
to the closest available article (a biography, a broader topic) when no
precise one exists; see the research notes in the PR that added this for
which ones are approximate.
"""

LEARN_MORE_LINKS = {
    'prise-de-la-bastille': 'https://fr.wikipedia.org/wiki/Prise_de_la_Bastille',
    'chute-mur-berlin': 'https://fr.wikipedia.org/wiki/Chute_du_mur_de_Berlin',
    'arrivee-christophe-colomb': 'https://fr.wikipedia.org/wiki/Christophe_Colomb',
    'chute-de-constantinople': 'https://fr.wikipedia.org/wiki/Chute_de_Constantinople',
    'attaque-pearl-harbor': 'https://fr.wikipedia.org/wiki/Attaque_de_Pearl_Harbor',
    'discours-i-have-a-dream': 'https://fr.wikipedia.org/wiki/Martin_Luther_King',
    'lancement-spoutnik': 'https://fr.wikipedia.org/wiki/Spoutnik_1',
    'siege-de-bagdad-1258': 'https://fr.wikipedia.org/wiki/Bataille_de_Bagdad_(1258)',
    'restauration-meiji': 'https://fr.wikipedia.org/wiki/Restauration_de_Meiji',
    'chute-de-tenochtitlan': 'https://fr.wikipedia.org/wiki/Si%C3%A8ge_de_Tenochtitlan',
    'prise-de-jerusalem-par-saladin': 'https://fr.wikipedia.org/wiki/Si%C3%A8ge_de_J%C3%A9rusalem_(1187)',
    'independance-du-ghana': 'https://fr.wikipedia.org/wiki/Dominion_du_Ghana',
    'prise-des-tuileries': 'https://fr.wikipedia.org/wiki/Journ%C3%A9e_du_10_ao%C3%BBt_1792',
    'debarquement-normandie': 'https://fr.wikipedia.org/wiki/D%C3%A9barquement_de_Normandie',
    'armistice-1918': 'https://fr.wikipedia.org/wiki/Armistice_du_11_novembre_1918',
    'declaration-independance-americaine': "https://fr.wikipedia.org/wiki/D%C3%A9claration_d'ind%C3%A9pendance_des_%C3%89tats-Unis",
    'nuit-du-4-aout': 'https://fr.wikipedia.org/wiki/Nuit_du_4_ao%C3%BBt_1789',
    'bataille-de-waterloo': 'https://fr.wikipedia.org/wiki/Bataille_de_Waterloo',
    'sacre-napoleon': 'https://fr.wikipedia.org/wiki/Sacre_de_Napol%C3%A9on_Ier',
    'signature-magna-carta': 'https://fr.wikipedia.org/wiki/Jean_sans_Terre',
    'eruption-vesuve': 'https://fr.wikipedia.org/wiki/%C3%89ruption_du_V%C3%A9suve_en_79',
    'krach-de-1929': 'https://fr.wikipedia.org/wiki/Krach_de_1929',
    'bombardement-hiroshima': "https://fr.wikipedia.org/wiki/Bombardements_atomiques_d'Hiroshima_et_de_Nagasaki",
    'assassinat-cesar': 'https://fr.wikipedia.org/wiki/Assassinat_de_Jules_César',
    'alunissage-apollo-11': 'https://fr.wikipedia.org/wiki/Apollo_11',
    'capitulation-allemande-1945': 'https://fr.wikipedia.org/wiki/Actes_de_capitulation_du_Troisième_Reich',
    'vol-de-gagarine': 'https://fr.wikipedia.org/wiki/Vostok_1',
    'revolution-doctobre': "https://fr.wikipedia.org/wiki/Révolution_d'Octobre",
    'these-de-luther': 'https://fr.wikipedia.org/wiki/95_thèses',
    'liberation-mandela': 'https://fr.wikipedia.org/wiki/Nelson_Mandela',
    'chute-empire-romain-occident': "https://fr.wikipedia.org/wiki/Déclin_de_l'Empire_romain_d'Occident",
    'invention-machine-vapeur-watt': 'https://fr.wikipedia.org/wiki/Machine_de_Watt',
    'decouverte-tombe-toutankhamon': 'https://fr.wikipedia.org/wiki/Tombeau_de_Toutânkhamon',
    'mort-de-barbe-noire': 'https://fr.wikipedia.org/wiki/Barbe_Noire',
    'mort-de-gengis-khan': 'https://fr.wikipedia.org/wiki/Gengis_Khan',
    'traite-de-nankin': 'https://fr.wikipedia.org/wiki/Trait%C3%A9_de_Nankin',
    'independance-de-linde': 'https://fr.wikipedia.org/wiki/Jour_de_l%27Ind%C3%A9pendance_(Inde)',
    'bataille-dadoua': 'https://fr.wikipedia.org/wiki/Bataille_d%27Adoua',
    'conference-de-berlin': 'https://fr.wikipedia.org/wiki/Conf%C3%A9rence_de_Berlin',
    'capture-datahualpa': 'https://fr.wikipedia.org/wiki/Bataille_de_Cajamarca',
    'cook-a-botany-bay': 'https://fr.wikipedia.org/wiki/Premier_voyage_de_James_Cook',
    'fondation-de-sydney': 'https://fr.wikipedia.org/wiki/Histoire_de_Sydney',
    'prise-de-grenade': 'https://fr.wikipedia.org/wiki/Prise_de_Grenade',
    'bataille-de-lepante': 'https://fr.wikipedia.org/wiki/Bataille_de_L%C3%A9pante',
    'bataille-de-panipat': 'https://fr.wikipedia.org/wiki/Premi%C3%A8re_bataille_de_Panipat',
}
