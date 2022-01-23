# convert to
def convert(money):
    ryb_to_usd = 0.013039
    ryb_to_eur = 0.011507
    ryb_to_chf = 0.011922
    ryb_to_gbp = 0.009615
    ryb_to_cny = 0.082664
    usd = int(money * ryb_to_usd)
    eur = int(money * ryb_to_eur)
    chf = int(money * ryb_to_chf)
    gbp = int(money * ryb_to_gbp)
    cny = int(money * ryb_to_cny)
    return usd, eur, chf, gbp, cny
