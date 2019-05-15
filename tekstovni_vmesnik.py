import model
lojtre = '#################################################################\n'

def izpis_zmage(igra):
    tekst = lojtre + 'Uganili ste geslo {0}\n'.format(igra.geslo)
    return tekst

def izpis_poraza(igra):
    tekst = lojtre + 'Obešeni ste! Pravilno geslo je bilo {0}\n'.format(igra.geslo)
    return tekst

def izpis_igre(igra):
    tekst = lojtre + igra.pravilni_del_gesla() + '\n' + ('Napačni ugibi: {0}\nPreostalo število poizkusov: {1}').format(igra.nepravilni_ugibi(), model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1) + '\n' + lojtre
    return tekst

def zahtevaj_vnos():
    return input('Ugibaj črko: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        if igra.poraz():
            print(izpis_poraza(igra))
            break
        elif igra.zmaga():
            print(izpis_zmage(igra))
            break
        else:
            pass
    return None

pozeni_vmesnik()